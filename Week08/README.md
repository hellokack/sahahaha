> 💡 **안내:** 본 README.md 문서는 과제 수행 및 문서화 과정에서 생성형 AI의 도움을 받아 작성되었습니다.

# 🍇 [8주차] 워크플로우 실행 최적화 리포트

## 1. 중복 제거 및 구조화 (Reusable & Composite)
* **Composite Action 도입:** `.github/actions/setup-python-env`를 생성하여 반복되는 Python 세팅 및 의존성 설치, 캐싱 로직을 하나의 모듈로 캡슐화하였습니다.
* **Reusable Workflow 적용:** `.github/workflows/reusable-test.yml`을 구성하여 Matrix 조합 테스트를 별도로 분리하고, 메인 워크플로우에서 호출(`workflow_call`)하도록 설계하여 코드 중복을 제거했습니다.

## 2. 선택적 배포 및 조건부 파이프라인 (Paths & If)
* **변경 파일 감지:** `paths: ['Week08/**']` 조건을 추가하여, 전체 코드가 아닌 해당 폴더에 변경이 발생했을 때만 파이프라인이 실행되도록 컴퓨팅 자원 낭비를 방지했습니다.
* **브랜치/PR 조건 분기:** Pull Request 상황에서는 테스트만 검증하고, `main` 브랜치에 최종 `push` 될 때만 배포(Deploy) Job이 실행되도록 `if: github.event_name == 'push'` 조건을 명시했습니다.

## 3. 캐싱 적용 전후 실행 시간 분석 (Cache hit)
`actions/setup-python`의 `cache: 'pip'` 기능을 Composite Action에 내장하여 테스트를 진행한 결과입니다.
* **최적화 전 (Cache Miss):** 의존성 패키지 전체 다운로드 진행 -> 약 **40초~45초** 소요
* **최적화 후 (Cache Hit):** 캐시된 패키지 활용 -> 약 **10초~15초** 소요
* **개선 결과:** 패키지 설치 단계의 소요 시간을 **약 65% 이상 획기적으로 단축**하여 피드백 루프를 가속화했습니다.