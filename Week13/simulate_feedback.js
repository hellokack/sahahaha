// LLM(생성형 AI) 프롬프팅을 통해 추출된 10인의 페르소나별 A/B 테스트 피드백 데이터
// 시나리오: 기존 UI(Variant A) vs CTA 버튼과 디자인이 강조된 신규 UI(Variant B)

const llmGeneratedFeedback = [
    { 
        id: 1, role: "개발자", trait: "성격 급함, 효율성 중시", preferred: "Variant B", 
        comment: "B 버전의 큼직한 CTA 버튼 덕분에 마우스 이동 동선이 줄어들어 클릭 속도가 확실히 빨라졌습니다. 직관적이라 마음에 듭니다." 
    },
    { 
        id: 2, role: "대학생", trait: "디자인 전공, 심미성 중시", preferred: "Variant B", 
        comment: "새롭게 적용된 주황색 배너(Variant B)가 기존 대비 훨씬 세련되고 트렌디합니다. 시각적으로 주목도가 높네요." 
    },
    { 
        id: 3, role: "사무직", trait: "보수적, 익숙함 선호", preferred: "Variant A", 
        comment: "갑자기 화면 레이아웃과 색상이 바뀌어서 낯설고 혼란스럽습니다. 원래 쓰던 기존 A 버전이 눈에 익어서 더 편안합니다." 
    },
    { 
        id: 4, role: "모바일 헤비유저", trait: "엄지 조작 편의성 중시", preferred: "Variant B", 
        comment: "한 손으로 스마트폰을 쥘 때 B 버전의 버튼 위치가 엄지손가락 반경에 딱 맞게 배치되어 있어서 환상적입니다." 
    },
    { 
        id: 5, role: "시각 장애인", trait: "명도 대비 및 접근성 중시", preferred: "Variant A", 
        comment: "B 버전의 배너 색상은 화려하지만, 글자와의 명도 대비가 낮아 스크린 리더 없이 흐릿하게 볼 때 오히려 기존 A 버전이 더 또렷하게 읽힙니다." 
    },
    { 
        id: 6, role: "마케터", trait: "전환 유도(CTA) 중심 사고", preferred: "Variant B", 
        comment: "이벤트 참여를 유도하는 측면에서 B 버전이 압도적으로 우수합니다. 사용자의 시선을 자연스럽게 버튼으로 이끌어줍니다." 
    },
    { 
        id: 7, role: "데이터 분석가", trait: "정보의 명확성 선호", preferred: "Variant B", 
        comment: "Variant B의 구조가 사용자가 어떤 경로로 진입해야 할지 더 명확하게 가이드라인을 제공한다고 판단됩니다." 
    },
    { 
        id: 8, role: "일반 주부", trait: "신뢰감 및 안정감 중시", preferred: "Variant B", 
        comment: "전체적으로 화면이 밝아지고 산뜻해져서 새 버전(B)이 서비스에 대한 신뢰감이 더 생기고 보기 좋습니다." 
    },
    { 
        id: 9, role: "보안 전문가", trait: "보안 안내 및 직관성 중시", preferred: "Variant A", 
        comment: "디자인 변화보다는 개인정보 동의나 보안 관련 안내 문구가 눈에 잘 띄는 기존 A 버전의 투박한 레이아웃이 더 안전하게 느껴집니다." 
    },
    { 
        id: 10, role: "웹 퍼블리셔", trait: "레이아웃 트렌드 중시", preferred: "Variant B", 
        comment: "요즘 유행하는 카드형 레이아웃과 여백 활용이 B 버전에 잘 녹아있어 모던한 느낌을 줍니다. 훌륭한 UI 개선입니다." 
    }
];

console.log("🚀 [Lean Startup] LLM 기반 10명 사용자 피드백 시뮬레이션 결과\n");

let variantAVotes = 0;
let variantBVotes = 0;

llmGeneratedFeedback.forEach(data => {
    if (data.preferred === "Variant B") variantBVotes++;
    else variantAVotes++;

    console.log(`[페르소나 ${data.id}] ${data.role} (${data.trait})`);
    console.log(`- 선호 버전: ${data.preferred}`);
    console.log(`- LLM 추출 피드백: "${data.comment}"\n`);
});

console.log("--------------------------------------------------");
console.log("📊 [최종 피드백 집계 및 결정 요약]");
console.log(`- Variant A (기존) 선호: ${variantAVotes}명`);
console.log(`- Variant B (신규) 선호: ${variantBVotes}명`);
console.log(`\n💡 의사결정: 정성적 피드백의 ${ (variantBVotes / 10) * 100 }%가 Variant B를 지지하므로, 해당 UI로 Persevere(지속)합니다.`);