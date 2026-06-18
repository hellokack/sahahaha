# Week14 Final Sahaha AI

This folder contains the final capstone deliverable for the Sahaha AI public-service assistant.

## Features

- FastAPI chat UI and API for Saha-gu public-service questions
- Official staff-directory lookup using the Saha-gu staff page
- Privacy-input blocking and response sanitization
- Hybrid retrieval with vector search and BM25

## Main Endpoints

- `GET /`
- `GET /widget`
- `GET /healthz`
- `POST /api/chat`
- `POST /api/clear`
- `GET /api/stats`

## Local Run

```bash
pip install -r requirements.txt
python main.py --mode web
```

Open `http://127.0.0.1:5000`.

If port `5000` is already in use, set a different port before starting:

```bash
set FLASK_PORT=5001
python main.py --mode web
```

## Lightweight Submission Checks

```bash
pip install -r requirements-ci.txt
python -m py_compile app.py main.py config.py chatbot/dept_directory.py crawler/staff_directory.py
python -m unittest discover -s tests -v
```

## Deployment Notes

- Health check path: `/healthz`
- Required environment variables are listed in `.env.example`
- Rollback and operations notes are documented in the repository root `RUNBOOK.md`
