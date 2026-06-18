# 사하하 AI 최종 제출 저장소

이 저장소는 `사하하(Sahaha)` 캡스톤 AI OSS 프로젝트의 개인 최종 제출용 저장소입니다.

## 최종 제출 링크

- GitHub 저장소: [hellokack/sahahaha](https://github.com/hellokack/sahahaha)
- 시연 영상: [구글드라이브 시연영상](https://drive.google.com/file/d/13rXOmVOlGu4-uUfxlnP-5Lz28X6Q1rHd/view?usp=sharing)
- 공개 웹 URL: `배포 후 추가 예정`

## 프로젝트 개요

- 프로젝트명: `사하하 AI`
- 최종 앱 위치: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- 목적: 사하구청 관련 민원성 질문에 대해 AI 채팅 UI와 공식 부서/연락처 안내를 제공
- 핵심 방식: 사하구 공식 데이터를 기반으로 한 RAG와 직원안내 페이지 기반 부서/전화번호 조회

## 최종 제출 요구사항 점검표

| 요구사항 | 상태 | 근거 |
| --- | --- | --- |
| 공개 GitHub 저장소 | 완료 | 본 저장소 |
| `README / CONTRIBUTING / CODE_OF_CONDUCT / LICENSE` | 완료 | [README.md](./README.md), [CONTRIBUTING.md](./CONTRIBUTING.md), [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md), [LICENSE](./LICENSE) |
| 동작 가능한 AI 기능(UI/API) | 완료 | [Week14_Final_SahahaAI](./Week14_Final_SahahaAI), [`/api/chat`](./Week14_Final_SahahaAI/app.py) |
| PR 게이트 CI | 완료 | [week14-final-ci.yml](./.github/workflows/week14-final-ci.yml) |
| 메인 배포 준비 | 완료 | [render.yaml](./render.yaml), [DEPLOYMENT.md](./DEPLOYMENT.md) |
| 헬스체크 | 완료 | [`GET /healthz`](./Week14_Final_SahahaAI/app.py) |
| 롤백 계획 | 완료 | [RUNBOOK.md](./RUNBOOK.md) |
| 관측성(로그/메트릭/대시보드 소스) | 완료 | [RUNBOOK.md](./RUNBOOK.md), [`/api/stats`](./Week14_Final_SahahaAI/app.py) |
| 테스트 근거 | 완료 | [test_submission.py](./Week14_Final_SahahaAI/tests/test_submission.py) |
| 보안 자동화 | 완료 | [week14-final-security.yml](./.github/workflows/week14-final-security.yml), [dependabot.yml](./.github/dependabot.yml) |
| 문서 산출물 | 완료 | [ADR.md](./ADR.md), [MODEL_CARD.md](./MODEL_CARD.md), [CHANGELOG.md](./CHANGELOG.md), [RUNBOOK.md](./RUNBOOK.md) |
| 릴리스 태그 `v1.0.0` 이상 | 완료 | `v1.0.0` |
| 회고문 | 완료 | [RETROSPECTIVE.md](./RETROSPECTIVE.md) |
| 3분 이내 데모 대본 | 완료 | [DEMO.md](./DEMO.md) |
| 데모 영상 URL | 완료 | [구글드라이브 영상 링크](https://drive.google.com/file/d/13rXOmVOlGu4-uUfxlnP-5Lz28X6Q1rHd/view?usp=sharing) |
| 공개 웹 URL | 배포 계정 필요 | [DEPLOYMENT.md](./DEPLOYMENT.md) |

## 앱이 하는 일

- FastAPI 기반 채팅 UI와 API 제공
- 사하구 주민 관점의 행정/민원 질문 응답
- 사하구청 공식 직원안내 페이지를 기준으로 부서명과 전화번호 안내
- 개인정보 입력 차단 및 응답 내 민감정보 마스킹
- 핵심 답변 문장을 채팅 UI에서 강조 표시

## 제출 문서 목록

- 최종 앱 소스: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- 배포 안내: [DEPLOYMENT.md](./DEPLOYMENT.md)
- 운영/롤백 문서: [RUNBOOK.md](./RUNBOOK.md)
- 아키텍처 결정 문서: [ADR.md](./ADR.md)
- 변경 이력: [CHANGELOG.md](./CHANGELOG.md)
- 모델 카드: [MODEL_CARD.md](./MODEL_CARD.md)
- 회고문: [RETROSPECTIVE.md](./RETROSPECTIVE.md)
- 데모 대본 및 영상 정보: [DEMO.md](./DEMO.md)

## 실행 방법

### 1. 최초 준비

`Week14_Final_SahahaAI` 폴더에서 `.env.example`을 참고해 `.env` 파일을 만들어야 합니다.

필수 환경변수:

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

포트 `5000`이 이미 사용 중이면:

```bash
set FLASK_PORT=5001
python main.py --mode web
```

## 실행 영상 촬영용 순서

1. PowerShell을 열고 저장소 루트로 이동합니다.
2. `cd Week14_Final_SahahaAI`
3. `pip install -r requirements.txt`
4. `.env` 파일이 없다면 `.env.example`을 복사해 `.env`로 만든 뒤 값 입력
5. `python main.py --mode web`
6. 브라우저에서 `http://127.0.0.1:5000` 접속
7. 일반 질문 1개, 부서/연락처 질문 1개, 개인정보 차단 질문 1개를 시연
8. 마지막에 `http://127.0.0.1:5000/healthz`도 보여주기

자세한 멘트와 화면 순서는 [DEMO.md](./DEMO.md)에 정리되어 있습니다.

## 배포

### Render

- 설정 파일: [render.yaml](./render.yaml)
- 앱 루트 디렉터리: `Week14_Final_SahahaAI`
- 헬스체크 경로: `/healthz`

### Railway

- [Week14_Final_SahahaAI/Dockerfile](./Week14_Final_SahahaAI/Dockerfile) 기준 배포 가능
- 서비스 루트를 `Week14_Final_SahahaAI`로 지정하거나 해당 Dockerfile을 사용

세부 절차는 [DEPLOYMENT.md](./DEPLOYMENT.md)에 정리했습니다.

## 검증한 내용

```bash
cd Week14_Final_SahahaAI
python -m py_compile app.py main.py config.py chatbot/dept_directory.py crawler/staff_directory.py
python -m unittest discover -s tests -v
```

## 현재 남은 수동 작업

- 실제 공개 배포 URL 발급

## 비고

- `.env`와 `.mp4` 파일은 의도적으로 버전 관리에서 제외했습니다.
- 최종 코드는 팀 저장소에서 개인 제출 저장소로 정리해 옮겼습니다.
- 과제 제출 직전에는 공개 웹 URL만 추가하면 됩니다.
