### 🚀 [10주차] 멀티 플랫폼 배포 자동화

**1. 프론트엔드 배포 및 PR 프리뷰 (Vercel)**
* Vercel을 연동하여 `main` 브랜치 프론트엔드 자동 배포 구성 완료
* 새로운 브랜치에서 PR 생성 시 Vercel 봇을 통해 임시 주소를 제공하는 PR 프리뷰 환경 구축 검증 완료

**2. Docker 기반 배포 파이프라인 전략**
* **로컬/빌드 환경:** `Dockerfile`을 통해 로컬 환경과 동일한 Node.js 컨테이너 환경 구성
* **CI/CD 파이프라인:** GitHub `main` 브랜치에 코드가 푸시되면 Render가 이를 감지하여 자동으로 이미지를 빌드하고 컨테이너를 재배포(Redeploy)하도록 자동화 파이프라인 구축
* **운영 (Production):** 외부 클라우드(Render) 환경에 컨테이너를 배포하여 서비스 안정성 확보

**3. 외부 클라우드 컨테이너 배포 및 헬스체크 (Render)**
* Render의 Web Service를 이용해 `Dockerfile` 기반 컨테이너 자동 배포 완료
* 한글 인코딩(`charset=utf-8`) 설정을 적용하여 정상적인 웹 페이지 출력 확인
* 헬스체크(Health Check) 경로를 `/healthz`로 설정하여 서버 생존 여부 지속 모니터링 구성 완료

---

### ✅ 10주차 과제 결과 확인 (Live URL)

🔗 **백엔드 (Render) 컨테이너 실서버 주소:** * [https://aioss-week10-server.onrender.com](https://aioss-week10-server.onrender.com)

🩺 **헬스체크 (Health Check) 테스트 주소:** * [https://aioss-week10-server.onrender.com/healthz](https://aioss-week10-server.onrender.com/healthz) 
*(접속 시 'OK' 문구 출력)*

---
본 문서는 생성형 AI의 도움을 받아 작성되었습니다.