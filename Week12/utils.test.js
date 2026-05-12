const utils = require('./utils');

describe('Week12 유틸리티 함수 TDD 테스트', () => {
    test('1. 더하기 기능 테스트', () => {
        expect(utils.add(1, 2)).toBe(3);
    });

    test('2. 빼기 기능 테스트', () => {
        expect(utils.subtract(5, 2)).toBe(3);
    });

    test('3. 이메일 유효성 테스트', () => {
        expect(utils.isEmailValid('test@example.com')).toBe(true);
        expect(utils.isEmailValid('invalid-email')).toBe(false);
    });

    test('4. 문자열 줄임 테스트', () => {
        expect(utils.truncateString('안녕하세요 반갑습니다', 5)).toBe('안녕하세요...');
        expect(utils.truncateString('안녕', 5)).toBe('안녕');
    });

    test('5. 통화 형식 변환 테스트', () => {
        expect(utils.formatCurrency(1000)).toContain('1,000');
    });
});