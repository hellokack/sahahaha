# Week09/Dockerfile
FROM node:20-alpine

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 파일 복사 및 모듈 설치
COPY package.json ./
RUN npm install

# 소스 코드 복사
COPY index.js ./

# 앱 실행 명령어
CMD ["node", "index.js"]