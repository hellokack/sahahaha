// TDD를 통해 구현된 5가지 핵심 유틸리티 함수
const utils = {
    // 1. 덧셈
    add: (a, b) => a + b,
    
    // 2. 뺄셈
    subtract: (a, b) => a - b,
    
    // 3. 이메일 형식 검증
    isEmailValid: (email) => {
        const re = /\S+@\S+\.\S+/;
        return re.test(email);
    },
    
    // 4. 문자열 줄임 (...)
    truncateString: (str, n) => {
        if (str.length <= n) return str;
        return str.slice(0, n) + "...";
    },
    
    // 5. 숫자를 한국 통화 형식(원)으로 변환
    formatCurrency: (num) => {
        return new Intl.NumberFormat('ko-KR', { style: 'currency', currency: 'KRW' }).format(num);
    }
};

module.exports = utils;