import json
import datetime
import os

# 1. 가상의 DORA 메트릭 데이터 수집 (실제로는 GitHub API 등과 연동하는 부분)
data = {
    "report_date": str(datetime.date.today()),
    "metrics": {
        "Lead_Time_for_Changes": "24 hours",
        "Deployment_Frequency": "5 times/week",
        "Mean_Time_to_Restore_MTTR": "4 hours",
        "Change_Failure_Rate": "10%"
    },
    "status": "Healthy"
}

# 2. 저장할 경로 지정 (Week02 폴더 안)
save_path = os.path.join(os.path.dirname(__file__), 'dora_metrics.json')

# 3. JSON 파일로 저장 (아티팩트용)
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ DORA 메트릭 수집 완료! [{save_path}] 저장 성공")