// LLM 페르소나 기반 A/B 테스트 피드백 시뮬레이터
const personas = [
    { id: 1, role: "성격 급한 개발자", trait: "효율성 중시" },
    { id: 2, role: "디자인 전공 대학생", trait: "심미성 중시" },
    { id: 3, role: "보수적인 사무직", trait: "익숙함 선호" },
    { id: 4, role: "모바일 헤비 유저", trait: "엄지 클릭 편의성 중시" },
    { id: 5, role: "시각 장애인", trait: "명도 대비 및 접근성 중시" },
    { id: 6, role: "데이터 분석가", trait: "명확한 정보 전달 선호" },
    { id: 7, role: "초보 스마트폰 사용자", trait: "친절한 설명 필요" },
    { id: 8, role: "마케터", trait: "CTA(콜투액션) 눈에 띄는 것 선호" },
    { id: 9, role: "보안 전문가", trait: "안전해 보이는 UI 선호" },
    { id: 10, role: "웹 퍼블리셔", trait: "레이아웃 일관성 중시" }
];

console.log("🚀 [Lean Startup] LLM 기반 10명 사용자 피드백 수집 시작...\n");

let variantAVotes = 0;
let variantBVotes = 0;

personas.forEach(p => {
    // LLM이 생성했다고 가정하는 가상의 피드백 로직 (Variant B 선호도를 70%로 설정)
    const prefersB = Math.random() > 0.3; 
    const assignedVariant = prefersB ? "Variant B (신규 UI)" : "Variant A (기존 UI)";
    
    if (prefersB) variantBVotes++;
    else variantAVotes++;

    console.log(`[페르소나 ${p.id}] ${p.role} (${p.trait})`);
    console.log(`- 할당 및 선호: ${assignedVariant}`);
    console.log(`- 피드백 요약: "${prefersB ? '새로운 버전이 목적을 달성하기에 더 적합합니다.' : '기존 방식이 더 편안합니다.'}"\n`);
});

console.log("📊 [최종 피드백 집계]");
console.log(`Variant A 선호: ${variantAVotes}명 | Variant B 선호: ${variantBVotes}명`);