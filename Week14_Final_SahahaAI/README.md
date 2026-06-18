# Week14 사하하 AI 최종 앱

이 폴더는 사하하 AI 캡스톤 프로젝트의 최종 실행 애플리케이션입니다.

## 주요 기능

- FastAPI 기반 채팅 UI 및 API
- 사하구청 공공정보 질의응답
- 사하구청 공식 직원안내 페이지 기반 부서/연락처 조회
- 개인정보 입력 차단 및 응답 정제
- 벡터 검색 + BM25 기반 하이브리드 검색

## 주요 엔드포인트

- `GET /`
- `GET /widget`
- `GET /healthz`
- `POST /api/chat`
- `POST /api/clear`
- `GET /api/stats`

## 로컬 실행 방법

### 1. 환경변수 준비

`.env.example`을 참고해 `.env` 파일을 생성하고 필수 값을 채웁니다.

### 2. 실행

```bash
pip install -r requirements.txt
python main.py --mode web
```

접속 주소:

```text
http://127.0.0.1:5000
```

포트 `5000`이 이미 사용 중이면:

```bash
set FLASK_PORT=5001
python main.py --mode web
```

## 제출용 간단 검증

```bash
pip install -r requirements-ci.txt
python -m py_compile app.py main.py config.py chatbot/dept_directory.py crawler/staff_directory.py
python -m unittest discover -s tests -v
```

## 배포 관련 메모

- 헬스체크 경로: `/healthz`
- 필수 환경변수는 `.env.example` 참고
- 운영/롤백 문서는 저장소 루트의 [RUNBOOK.md](../RUNBOOK.md)에 정리
