# DEPLOYMENT

## 현재 상태

이 저장소는 배포 가능한 상태로 정리되어 있습니다.
다만 최종 공개 URL 생성 자체는 Render 또는 Railway 계정 로그인과 권한이 있어야 완료됩니다.

## Render 배포

이 저장소에는 Render Blueprint용 [render.yaml](./render.yaml)이 포함되어 있습니다.

### 기본 설정

- 저장소: `hellokack/sahahaha`
- 루트 디렉터리: `Week14_Final_SahahaAI`
- 헬스체크 경로: `/healthz`

### 필요한 환경변수

- `SECRET_KEY`
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_SERVICE_KEY`
- `ADMIN_API_KEY`
- 선택: `CORS_ALLOWED_ORIGINS`

### 실행 방식

앱은 플랫폼이 제공하는 `PORT` 환경변수를 읽어 실행되도록 수정되어 있습니다.

## Railway 배포

Railway용으로도 [Week14_Final_SahahaAI/Dockerfile](./Week14_Final_SahahaAI/Dockerfile)을 기준으로 배포할 수 있게 준비했습니다.

### Railway 배포 순서

1. GitHub 저장소로 새 프로젝트 생성
2. 서비스 소스를 `Week14_Final_SahahaAI`로 지정하거나 포함된 Dockerfile 선택
3. 필수 환경변수 입력
4. Public Domain 생성
5. `/healthz`가 `status=ok`를 반환하는지 확인

## 아직 URL이 비어 있는 이유

실제 공개 URL은 배포 플랫폼에 로그인한 계정에서 직접 생성해야 합니다.
이 로컬 작업공간만으로는 계정 권한이 필요한 최종 배포 단계까지 자동 완료할 수 없습니다.

## 배포 후 꼭 적어둘 값

- 서비스 URL: `TBD`
- 헬스체크 URL: `TBD/healthz`
- 데모 영상 URL: [구글드라이브 시연영상](https://drive.google.com/file/d/13rXOmVOlGu4-uUfxlnP-5Lz28X6Q1rHd/view?usp=sharing)
