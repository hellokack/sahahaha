// e2e/signup.spec.js
const { test, expect } = require('@playwright/test');

test('회원가입 폼 제출 테스트 (의도적 실패로 스크린샷 생성)', async ({ page }) => {
    // 임의의 사이트로 이동
    await page.goto('https://example.com');
    
    // 화면에 절대 존재할 수 없는 버튼을 클릭하도록 명령합니다.
    // 여기서 에러가 발생하고, Playwright가 실패 스크린샷을 찍습니다!
    await page.click('#this-button-does-not-exist', { timeout: 3000 });
});