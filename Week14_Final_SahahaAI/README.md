# Week14 사하하 AI 최종 앱

이 폴더는 캡스톤 AI OSS 프로젝트 `사하하(Sahaha)`의 최종 실행 애플리케이션입니다.

## 제출 링크

- GitHub 저장소: [hellokack/sahahaha](https://github.com/hellokack/sahahaha)
- 공개 웹 URL: [https://sahaha-final-ai.onrender.com/](https://sahaha-final-ai.onrender.com/)
- 헬스체크 URL: [https://sahaha-final-ai.onrender.com/healthz](https://sahaha-final-ai.onrender.com/healthz)
- 시연 영상: [Google Drive 링크](https://drive.google.com/file/d/13rXOmVOlGu4-uUfxlnP-5Lz28X6Q1rHd/view?usp=sharing)

## 민감정보 안내

- 이 폴더와 저장소에는 `.env`, API 키, 비밀번호, 개인정보를 포함하지 않았습니다.
- 시연 영상 원본 파일(`.mp4`)은 저장소에 올리지 않고 링크로만 제공합니다.

## 주요 기능

- FastAPI 기반 채팅 UI 및 API
- 사하구청 공식 정보 기반 질의응답
- 사하구청 공식 직원업무안내 기반 담당부서 및 연락처 조회
- 개인정보 입력 차단 및 응답 내 민감정보 정제
- 벡터 검색 + BM25 기반 하이브리드 검색
- Render 배포 및 헬스체크 지원

## 주요 엔드포인트

- `GET /`
- `GET /widget`
- `GET /healthz`
- `POST /api/chat`
- `POST /api/clear`
- `GET /api/stats`

## 로컬 실행 방법

### 1. 환경 변수 준비

`.env.example`을 참고해 `.env` 파일을 만들고 필수 값을 채웁니다.

필수 환경 변수:

- `SECRET_KEY`
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_SERVICE_KEY`
- `ADMIN_API_KEY`

### 2. 실행

```bash
pip install -r requirements.txt
python main.py --mode web
```

접속 주소:

```text
http://127.0.0.1:5000
```

헬스체크:

```text
http://127.0.0.1:5000/healthz
```

## 제출 전 검증

```bash
pip install -r requirements-ci.txt
python -m py_compile app.py main.py config.py chatbot/conversation.py chatbot/retriever.py database_db/database.py
python -m unittest discover -s tests -v
```

## 배포 메모

- 공개 서비스 URL: [https://sahaha-final-ai.onrender.com/](https://sahaha-final-ai.onrender.com/)
- 헬스체크 경로: `/healthz`
- 운영/롤백 문서: [../RUNBOOK.md](../RUNBOOK.md)
- 배포 상세 문서: [../DEPLOYMENT.md](../DEPLOYMENT.md)
