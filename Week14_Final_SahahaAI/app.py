"""
Sahaha AI FastAPI application.

- Keeps cold start light for deployment health checks
- Lazily initializes the chatbot on the first chat request
- Skips warmup and background scheduler in lightweight deployment mode
"""

import logging
import uuid
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.concurrency import run_in_threadpool
from starlette.middleware.sessions import SessionMiddleware

from config import (
    ADMIN_API_KEY,
    CORS_ALLOWED_ORIGINS,
    FLASK_HOST,
    FLASK_PORT,
    LIGHTWEIGHT_DEPLOYMENT,
    RATE_LIMIT_CHAT,
    SECRET_KEY,
)

logger = logging.getLogger(__name__)
APP_VERSION = "1.0.0"


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)


class Source(BaseModel):
    title: str
    url: str
    category: str = ""
    service_type: str = "기타"
    department: str = ""
    contact: str = ""


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
    is_clarification: bool
    degraded: bool = False
    degraded_reason: Optional[str] = None


class ClearResponse(BaseModel):
    status: str = "ok"


def get_health_payload() -> dict:
    """Small health payload used by smoke checks and deployments."""
    return {
        "status": "ok",
        "service": "sahaha-ai",
        "version": APP_VERSION,
    }


_chatbot = None
_db = None
_vector_store = None
_scheduler = None


def get_chatbot():
    global _chatbot
    if _chatbot is None:
        from chatbot.conversation import ChatBot

        _chatbot = ChatBot()
    return _chatbot


def get_db():
    global _db
    if _db is None:
        from database_db.database import Database

        _db = Database()
    return _db


def get_vector_store():
    global _vector_store
    if _vector_store is None:
        bot = get_chatbot()
        _vector_store = bot.retriever.vs
    return _vector_store


def _init_scheduler():
    global _scheduler
    from apscheduler.schedulers.background import BackgroundScheduler
    from config import CONVERSATION_TTL_DAYS
    from main import cleanup_old_conversations_job, run_incremental

    _scheduler = BackgroundScheduler()
    _scheduler.add_job(
        func=run_incremental,
        trigger="cron",
        hour=3,
        minute=0,
        id="incremental_crawl",
        misfire_grace_time=3600,
    )
    _scheduler.add_job(
        func=cleanup_old_conversations_job,
        trigger="cron",
        hour=4,
        minute=0,
        id="conversation_ttl_cleanup",
        misfire_grace_time=3600,
    )
    _scheduler.start()
    logger.info(
        "Scheduler enabled: incremental crawl 03:00, conversation cleanup %s days at 04:00",
        CONVERSATION_TTL_DAYS,
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup/shutdown hook."""
    logger.info("Starting Sahaha AI service")

    if LIGHTWEIGHT_DEPLOYMENT:
        logger.info("Lightweight deployment mode enabled: skipping warmup and scheduler")
    else:
        logger.info("Preloading chatbot resources during startup")
        try:
            await run_in_threadpool(get_chatbot)
            logger.info("Chatbot warmup completed")
        except Exception as exc:
            logger.warning("Chatbot warmup failed; will retry on first request: %s", exc)

        try:
            _init_scheduler()
        except Exception as exc:
            logger.error("Scheduler initialization failed: %s", exc)

    yield

    if _scheduler is not None:
        try:
            _scheduler.shutdown(wait=False)
            logger.info("Scheduler stopped")
        except Exception as exc:
            logger.warning("Scheduler shutdown failed: %s", exc)


limiter = Limiter(key_func=get_remote_address, default_limits=["200 per hour"])

app = FastAPI(
    title="사하구청 AI 상담",
    description="사하구청 공식 정보 기반 AI 상담 서비스",
    version=APP_VERSION,
    lifespan=lifespan,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY, same_site="lax")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def security_headers(request: Request, call_next):
    """Attach baseline security headers."""
    response = await call_next(request)
    allowed = " ".join(CORS_ALLOWED_ORIGINS) if CORS_ALLOWED_ORIGINS else "'self'"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        f"frame-ancestors 'self' {allowed}; "
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https:; "
        "connect-src 'self'"
    )
    return response


async def require_admin(x_admin_key: Optional[str] = Header(default=None)):
    """Validate admin API access."""
    if not ADMIN_API_KEY:
        logger.warning("ADMIN_API_KEY is missing; admin endpoints disabled")
        raise HTTPException(status_code=503, detail="관리자 기능이 비활성화되어 있습니다")
    if x_admin_key != ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="인증이 필요합니다")
    return True


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the main chat page."""
    if "session_id" not in request.session:
        request.session["session_id"] = str(uuid.uuid4())
    return templates.TemplateResponse(request, "index.html")


@app.get("/healthz")
async def healthz():
    """Simple process health endpoint for smoke checks."""
    return get_health_payload()


@app.get("/widget", response_class=HTMLResponse)
async def widget(request: Request):
    """Render embeddable widget page."""
    if "session_id" not in request.session:
        request.session["session_id"] = str(uuid.uuid4())
    return templates.TemplateResponse(request, "widget.html")


@app.post("/api/chat", response_model=ChatResponse)
@limiter.limit(RATE_LIMIT_CHAT)
async def chat(request: Request, payload: ChatRequest):
    """Chat API endpoint."""
    user_message = payload.message.strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="빈 메시지는 보낼 수 없습니다")

    session_id = request.session.get("session_id") or str(uuid.uuid4())
    request.session["session_id"] = session_id

    try:
        bot = get_chatbot()
        result = await run_in_threadpool(bot.chat, session_id, user_message)
        return ChatResponse(**result)
    except Exception as exc:
        logger.error("Chat request failed: %s", exc, exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "answer": "죄송합니다. 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요.",
                "sources": [],
                "is_clarification": False,
                "degraded": True,
                "degraded_reason": "internal_error",
            },
        )


@app.post("/api/clear", response_model=ClearResponse)
async def clear_chat(request: Request):
    """Clear the current conversation session."""
    session_id = request.session.get("session_id")
    if session_id:
        try:
            bot = get_chatbot()
            await run_in_threadpool(bot.clear_session, session_id)
        except Exception as exc:
            logger.error("Conversation clear failed: %s", exc)

    request.session["session_id"] = str(uuid.uuid4())
    return ClearResponse()


@app.get("/api/stats")
@limiter.limit("30 per minute")
async def stats(request: Request, _auth: bool = Depends(require_admin)):
    """Admin stats endpoint."""
    try:
        db = get_db()
        db_stats = await run_in_threadpool(db.stats)

        vs = get_vector_store()
        if vs is None:
            return {
                **db_stats,
                "total_vectors": 0,
                "lightweight_deployment": True,
            }

        vs_stats = await run_in_threadpool(vs.collection_stats)
        return {
            **db_stats,
            **vs_stats,
            "lightweight_deployment": LIGHTWEIGHT_DEPLOYMENT,
        }
    except Exception as exc:
        logger.error("/api/stats failed: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail="통계 조회 중 오류가 발생했습니다")


def run_server():
    """Run the FastAPI app with Uvicorn."""
    import uvicorn

    uvicorn.run(
        "app:app",
        host=FLASK_HOST,
        port=FLASK_PORT,
        log_level="info",
        reload=False,
    )


if __name__ == "__main__":
    run_server()
