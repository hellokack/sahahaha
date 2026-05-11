const http = require('http');
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    // 헬스체크(Health Check) 엔드포인트
    if (req.url === '/healthz') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('OK');
    } else {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello! AIOSS 10주차 컨테이너 배포 성공!');
    }
});

server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});