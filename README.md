# 사하하 AI 최종 제출 저장소

이 저장소는 캡스톤 AI OSS 프로젝트 `사하하(Sahaha)`의 개인 최종 제출용 저장소입니다.

## 최종 제출 링크

- GitHub 저장소: [hellokack/sahahaha](https://github.com/hellokack/sahahaha)
- 공개 웹 URL: [https://sahaha-final-ai.onrender.com/](https://sahaha-final-ai.onrender.com/)
- 헬스체크 URL: [https://sahaha-final-ai.onrender.com/healthz](https://sahaha-final-ai.onrender.com/healthz)
- 시연 영상: [Google Drive 링크](https://drive.google.com/file/d/13rXOmVOlGu4-uUfxlnP-5Lz28X6Q1rHd/view?usp=sharing)

## 민감정보 안내

- 이 저장소에는 `.env`, API 키, 비밀번호, 개인 식별 정보 등 민감정보를 포함하지 않았습니다.
- 대용량 시연 영상 파일(`.mp4`)도 저장소에 직접 포함하지 않고 외부 링크로만 제공합니다.

## 프로젝트 개요

- 프로젝트명: `사하하 AI`
- 최종 앱 위치: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- 목적: 사하구청 관련 민원과 행정 질문에 대해 AI 채팅 UI와 공식 부서/연락처 안내를 제공합니다.
- 주요 기능:
  - 사하구청 공식 데이터 기반 답변
  - 직원업무안내 페이지 기반 담당부서 및 전화번호 안내
  - 개인정보 입력 차단
  - 핵심 답변 하이라이트 제공
  - Render 배포 및 헬스체크 지원

## 과제 요구사항 충족표

| 요구사항 | 상태 | 근거 |
| --- | --- | --- |
| 공개 GitHub 저장소 | 완료 | 본 저장소 |
| README / CONTRIBUTING / CODE_OF_CONDUCT / LICENSE | 완료 | 루트 문서 포함 |
| 동작 가능한 AI 기능(API 또는 UI) | 완료 | `Week14_Final_SahahaAI` |
| PR 게이트 기준 CI/CD | 완료 | `.github/workflows/week14-final-ci.yml` |
| main 배포 | 완료 | Render 공개 URL 제공 |
| 헬스체크 | 완료 | `/healthz` |
| 롤백 계획 | 완료 | `RUNBOOK.md` |
| 관측성(로그/메트릭/대시보드) | 완료 | `RUNBOOK.md`, `/api/stats` |
| 테스트(단위/통합/E2E/eval 중 하나) | 완료 | `Week14_Final_SahahaAI/tests/test_submission.py` |
| 보안(Dependabot/스캔/SBOM 중 하나) | 완료 | `.github/dependabot.yml`, 보안 워크플로 |
| 문서(ADR/Runbook/Changelog/Model or Data card 중 하나) | 완료 | `ADR.md`, `RUNBOOK.md`, `CHANGELOG.md`, `MODEL_CARD.md` |
| 릴리스 태그 `v1.0.0` 이상 | 완료 | `v1.0.0` |
| 회고문 | 완료 | `RETROSPECTIVE.md` |
| 3분 이내 영상 데모 | 완료 | Google Drive 영상 링크 |

## 저장소 구성

- 최종 앱: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- 배포 문서: [DEPLOYMENT.md](./DEPLOYMENT.md)
- 운영/롤백 문서: [RUNBOOK.md](./RUNBOOK.md)
- 아키텍처 결정 기록: [ADR.md](./ADR.md)
- 변경 이력: [CHANGELOG.md](./CHANGELOG.md)
- 모델 카드: [MODEL_CARD.md](./MODEL_CARD.md)
- 회고문: [RETROSPECTIVE.md](./RETROSPECTIVE.md)
- 시연 가이드: [DEMO.md](./DEMO.md)

## 로컬 실행 방법

### 1. 환경 변수 준비

`Week14_Final_SahahaAI/.env.example`을 참고해 `.env` 파일을 준비합니다.

필수 환경 변수:

- `SECRET_KEY`
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_SERVICE_KEY`
- `ADMIN_API_KEY`

### 2. 로컬 실행

```bash
cd Week14_Final_SahahaAI
pip install -r requirements.txt
python main.py --mode web
```

브라우저 주소:

```text
http://127.0.0.1:5000
```

헬스체크:

```text
http://127.0.0.1:5000/healthz
```

## 배포 정보

- 플랫폼: Render
- 서비스 URL: [https://sahaha-final-ai.onrender.com/](https://sahaha-final-ai.onrender.com/)
- 헬스체크 응답:

```json
{"status":"ok","service":"sahaha-ai","version":"1.0.0"}
```

## 검증 내용

```bash
cd Week14_Final_SahahaAI
python -m py_compile app.py main.py config.py chatbot/conversation.py chatbot/retriever.py database_db/database.py
python -m unittest discover -s tests -v
```

## 비고

- `.env`, `.mp4` 등 민감정보 또는 대용량 파일은 버전 관리에서 제외했습니다.
- Render 무료 플랜 배포를 위해 경량 배포 모드를 적용했습니다.
- 공개 웹 URL, 시연 영상 URL, GitHub 저장소 URL을 README 상단에 정리했습니다.
