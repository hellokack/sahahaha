# RUNBOOK

## 서비스 정보

- 앱 폴더: `Week14_Final_SahahaAI`
- 로컬 실행 명령어: `python main.py --mode web`
- 기본 포트: `5000`
- 포트 충돌 시 예시: `set FLASK_PORT=5001`
- 헬스체크: `GET /healthz`
- 관리자 통계 API: `GET /api/stats` + `X-Admin-Key`

## 배포 흐름

1. `main` 기준 코드 준비
2. PR 게이트 CI 통과
3. Render 또는 Railway에 환경변수 설정
4. 서비스 배포
5. `/healthz` 확인
6. 메인 화면과 채팅 응답 확인

## 필수 환경변수

- `SECRET_KEY`
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_SERVICE_KEY`
- `ADMIN_API_KEY`

로컬 템플릿은 [Week14_Final_SahahaAI/.env.example](./Week14_Final_SahahaAI/.env.example)을 참고합니다.

## 헬스체크 기대 응답

```json
{
  "status": "ok",
  "service": "sahaha-ai",
  "version": "1.0.0"
}
```

## 롤백 계획

배포 실패 시 다음 순서로 복구합니다.

1. 이전 안정 태그 또는 직전 정상 커밋으로 되돌림
2. 이전 버전 재배포
3. `/healthz` 재확인
4. 메인 UI와 `/api/stats` 정상 동작 확인

권장 롤백 기준:

- `v1.0.0` 또는 그 이후의 최신 안정 태그

## 관측성

- 애플리케이션 로그: 표준 출력 + `Week14_Final_SahahaAI/data/pipeline.log`
- 메트릭 성격의 운영 정보: `/api/stats`
- 대시보드 소스: `/api/stats` JSON을 기반으로 스프레드시트나 Grafana 등에 연결 가능

## 빠른 점검 명령어

```bash
cd Week14_Final_SahahaAI
python main.py --mode web
curl http://127.0.0.1:5000/healthz
```
