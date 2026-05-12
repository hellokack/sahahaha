// 2주간의 A/B 테스트 핵심 지표 데이터 분석 (클릭률 및 전환율)
const weeks = 2;
const trafficPerVariant = 5000; // 가상 트래픽

const metrics = {
    VariantA: { clicks: 210, errors: 45 },
    VariantB: { clicks: 435, errors: 12 }
};

const ctrA = ((metrics.VariantA.clicks / trafficPerVariant) * 100).toFixed(2);
const ctrB = ((metrics.VariantB.clicks / trafficPerVariant) * 100).toFixed(2);

console.log(`📈 2주간 A/B 테스트 지표 요약 (총 트래픽: ${trafficPerVariant * 2})`);
console.log(`[Variant A] 클릭률(CTR): ${ctrA}% | 에러 발생: ${metrics.VariantA.errors}건`);
console.log(`[Variant B] 클릭률(CTR): ${ctrB}% | 에러 발생: ${metrics.VariantB.errors}건`);
console.log(`\n💡 분석 결과: Variant B의 CTR이 A 대비 약 ${(ctrB/ctrA).toFixed(1)}배 높으며 에러율도 낮습니다.`);