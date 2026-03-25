> 💡 **안내:** 본 README.md 문서는 과제 수행 및 문서화 과정에서 생성형 AI의 도움을 받아 작성되었습니다.

# 🍇 [7주차] GitHub Actions 기반 기본 CI/CD 구축

## 1. CI/CD 파이프라인 요약
* **대상 프로젝트:** Python 기반 AI 챗봇 백엔드 코드 (`Week07/app.py`)
* **워크플로우 파일:** `.github/workflows/ci-cd.yml`

## 2. 과제 요구사항 충족 내역
1. **Lint/Test 자동 실행:** `flake8`을 통한 코드 문법 검사 및 `pytest`를 통한 자동화 테스트 수행
2. **Matrix 전략 적용:** `ubuntu-latest`, `windows-latest` OS 환경과 Python `3.10`, `3.11` 버전을 조합하여 총 4가지 환경에서 크로스 테스트 진행
3. **Secrets 민감정보 주입:** GitHub Repository Secrets에 `MY_SECRET_KEY`를 등록하고 deploy 단계에서 환경 변수(env)로 안전하게 주입
4. **복합 워크플로우 구성 (아티팩트):** `build-and-test` 잡이 성공해야만 `deploy` 잡이 실행되도록 의존성(`needs`)을 설정. 빌드 단계에서 생성된 `test-results.txt`를 아티팩트로 업로드하고 배포 단계에서 다운로드하여 활용

## 3. 제출 링크
* **Actions 실행 내역 및 Workflow 파일:** [GitHub Actions 탭에서 링크 복사 후 붙여넣기]