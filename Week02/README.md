> 💡 **안내:** 본 README.md 문서는 과제 수행 및 문서화 과정에서 생성형 AI의 도움을 받아 작성되었습니다.

# 📊 [2주차] DORA 메트릭 수집 자동화

## 1. DORA 메트릭 대시보드 시안
Chart.js를 활용하여 구성한 DORA 4대 지표(Lead Time, Deployment Frequency, MTTR, Change Failure Rate) 대시보드 시안입니다.
![DORA Dashboard](./dashboard.png) 

## 2. 수집 자동화 파이프라인 개요 (선택 과제 완벽 구현)
본 프로젝트는 GitHub Actions의 `schedule(cron)` 기능을 활용하여 **매주 월요일 자정**마다 DORA 메트릭을 수집하고 리포트를 자동 갱신하도록 구축되었습니다.

* **데이터 수집 및 아티팩트 저장:** 실행 시 `dora-metrics.json` 데이터가 추출되어 Actions 아티팩트로 보관됩니다.
* **주간 보고서 자동 생성:** 봇(github-actions[bot])이 생성된 지표를 바탕으로 프로젝트 **최상위(Root) 디렉토리**에 `DORA_REPORT.md` 파일을 스스로 생성하고 Commit & Push 합니다.

---

## 3. ✅ 2주차 과제 결과 확인 (채점용 바로가기 링크)
교수님의 원활한 확인을 위해 자동화 실행 내역과 생성된 결과물 링크를 첨부합니다.

🔗 **1. [GitHub Actions 자동화 실행 내역 (클릭)](https://github.com/hellokack/sahahaha/actions)**
* `Week2 DORA Metrics Weekly Report` 워크플로우가 실행된 내역과 **JSON 아티팩트 저장 결과**를 확인하실 수 있습니다.

🔗 **2. [자동 생성된 주간 리포트 확인 (클릭)](https://github.com/hellokack/sahahaha/blob/main/DORA_REPORT.md)**
* Actions 봇이 프로젝트 최상위 경로에 성공적으로 자동 생성한 **`DORA_REPORT.md`** 파일입니다.