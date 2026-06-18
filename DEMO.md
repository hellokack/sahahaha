# DEMO

## Demo Metadata

- Live service URL: `TBD after platform login and deploy`
- Video URL: `TBD after recording/upload`
- Target duration: `2 minutes 30 seconds to 3 minutes`

## Demo Goal

Show that the final app is a working AI service with:

1. a functioning chat UI
2. official department and contact lookup
3. privacy-input blocking
4. health-check visibility
5. repository evidence for CI, security, rollback, and documentation

## 3-Minute Demo Script

### 0:00 - 0:20 Intro

Hello. This is our final capstone AI OSS project, `Sahaha AI`.
This service helps answer Saha-gu Office public-service questions through an AI chat interface.
The final deliverable is organized in this personal GitHub repository, and the main application is inside `Week14_Final_SahahaAI`.

### 0:20 - 0:40 Repository Overview

Here are the final submission materials.
The repository includes the README, contributing guide, code of conduct, license, runbook, architecture decision record, model card, changelog, and retrospective.
It also includes GitHub Actions workflows for PR gate CI and security scanning, plus the release tag `v1.0.0`.

### 0:40 - 1:10 App Launch

Now I will open the deployed web service or local running service.
This is the main chat UI for Sahaha AI.
The service is built with FastAPI and supports a public chat interface, chat reset, admin stats, and a health-check endpoint.

### 1:10 - 1:40 Normal Public-Service Question

First, I will ask a normal administrative question such as trash-disposal schedule or a public-facility question.
The chatbot returns a natural-language answer based on the retrieved Saha-gu information, and the key answer text is highlighted for readability.

### 1:40 - 2:10 Department and Contact Lookup

Next, I will ask, "사하구청 AI 담당 부서 알려줘".
The system looks up the official Saha-gu staff directory and returns the matching department context and phone number.
This shows that the answer uses the staff-directory data instead of a guessed phone number.

### 2:10 - 2:35 Privacy-Input Blocking

Now I will enter a privacy-sensitive example such as a phone number or detailed personal information.
The chatbot blocks the request and shows a warning message instead of processing that personal data.
This demonstrates the privacy-protection requirement of the service.

### 2:35 - 2:50 Health Check and Operations

Next, I will open `/healthz`.
The response shows `status: ok`, the service name, and the version.
For operations, the repository also includes a rollback plan in the runbook and observability through logs and the `/api/stats` endpoint.

### 2:50 - 3:00 Closing

In summary, this project delivers a working AI feature, CI and security automation, health check support, rollback documentation, and the final OSS submission documents required for the course.
Thank you.

## Recommended Demo Inputs

- `쓰레기 배출 요일 어케돼`
- `사하구청AI담당 부서 알려줘`
- `123412-1231231`

## Recording Checklist

- Show GitHub repository root
- Show `Week14_Final_SahahaAI`
- Show one normal answer
- Show one department/contact answer
- Show one privacy block
- Show `/healthz`
- Mention CI, security, rollback, and docs once
