# Sahaha Final Submission Repository

This repository is the personal final-submission mirror for the `Sahaha` capstone AI OSS project.

## Final Project Location

The final deliverable source code lives in [Week14_Final_SahahaAI](./Week14_Final_SahahaAI).

## What This Project Does

Sahaha is a public-service AI assistant for Saha-gu Office. It uses retrieval-augmented generation (RAG) over official Saha-gu website data and provides:

- A working chat UI and API
- Official department and contact lookup based on the Saha-gu staff directory
- Privacy-input blocking and reply sanitization
- Hybrid retrieval with vector search and BM25

## Submission Artifacts

- Final app source: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- Runbook and rollback plan: [RUNBOOK.md](./RUNBOOK.md)
- Architecture decision record: [ADR.md](./ADR.md)
- Changelog: [CHANGELOG.md](./CHANGELOG.md)
- Model card: [MODEL_CARD.md](./MODEL_CARD.md)
- Retrospective: [RETROSPECTIVE.md](./RETROSPECTIVE.md)
- Demo notes: [DEMO.md](./DEMO.md)

## CI / Security / Operations

- PR gate CI: [week14-final-ci.yml](./.github/workflows/week14-final-ci.yml)
- Python dependency update policy: [dependabot.yml](./.github/dependabot.yml)
- Python security scan: [week14-final-security.yml](./.github/workflows/week14-final-security.yml)
- Health check endpoint: `GET /healthz`
- Metrics endpoint: `GET /api/stats`

## Local Run

```bash
cd Week14_Final_SahahaAI
pip install -r requirements.txt
python main.py --mode web
```

Default local URL:

```text
http://127.0.0.1:5000
```

## Release

The final release tag for submission is planned as `v1.0.0`.

## Notes

- `.env` is intentionally excluded from version control.
- The final code was migrated from the team repository into this personal submission repository.
- If a live public deployment URL is required by the course portal, add it to [DEMO.md](./DEMO.md) after deployment secrets are configured.
