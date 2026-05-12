### 🚀 [12주차] Shift-Left 테스트 자동화 실습

**1. 단위 테스트(Jest) 및 커버리지 달성**
* 핵심 유틸리티 함수 5종(`add`, `subtract`, `isEmailValid`, `truncateString`, `formatCurrency`) 구현 완료.
* `jest --coverage` 실행 결과, 요구사항(80%)을 초과하는 **코드 커버리지 100%** 달성.

**2. TDD(Red-Green-Refactor) 사이클 적용**
* 실패하는 테스트 코드를 먼저 작성(Red)한 후, 이를 통과시키기 위한 최소한의 로직을 구현(Green)하고, 코드를 다듬는(Refactor) 방식으로 구현함.

**3. CI 자동화 파이프라인 (GitHub Actions)**
* `.github/workflows/week12-ci.yml`을 구성하여, 코드 푸시 및 PR 생성 시 자동으로 Jest 테스트가 실행되도록 Shift-Left 환경 구축.

---

**4. [선택과제] Playwright E2E 시나리오 및 리팩토링 안정성 검증**

* **E2E 테스트 시나리오 설계 (Playwright):** * 사용자가 회원가입 폼에 진입하여 이메일을 입력하고 제출 버튼을 클릭하는 시나리오 작성.
  * 실패 시 스크린샷 아티팩트를 자동 저장하도록 구성하여 디버깅 편의성 확보.
* **리팩토링 안정성 검증:** * 기존 단위 테스트가 뒷받침된 상태에서 내부 로직을 개선하여, 기능의 회귀(Regression) 현상 없이 안정적으로 리팩토링을 완료함.

---

### ✅ 12주차 과제 결과 확인 (CI Success)

🔗 **GitHub Actions 테스트 성공 기록:** [https://github.com/hellokack/sahahaha/actions/runs/25712174834](https://github.com/hellokack/sahahaha/actions/runs/25712174834)

---
본 문서는 생성형 AI의 도움을 받아 작성되었습니다.