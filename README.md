# Sahaha AI Final Submission

This repository is the personal final-submission repository for the Sahaha capstone AI OSS project.

## Project Summary

- Project name: `Sahaha AI`
- Final app location: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- Purpose: answer Saha-gu Office public-service questions with a working AI chat UI and official department/contact guidance
- Core AI behavior: retrieval-augmented generation over Saha-gu public data plus official staff-directory lookup

## Final Submission Status

| Requirement | Status | Evidence |
| --- | --- | --- |
| Public GitHub repository | Ready | This repository |
| README / CONTRIBUTING / CODE_OF_CONDUCT / LICENSE | Ready | [README.md](./README.md), [CONTRIBUTING.md](./CONTRIBUTING.md), [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md), [LICENSE](./LICENSE) |
| Working AI feature (UI/API) | Ready | [Week14_Final_SahahaAI](./Week14_Final_SahahaAI), [`/api/chat`](./Week14_Final_SahahaAI/app.py) |
| PR gate CI | Ready | [week14-final-ci.yml](./.github/workflows/week14-final-ci.yml) |
| Main deployment flow | Ready to deploy | [render.yaml](./render.yaml), [DEPLOYMENT.md](./DEPLOYMENT.md) |
| Health check | Ready | [`GET /healthz`](./Week14_Final_SahahaAI/app.py) |
| Rollback plan | Ready | [RUNBOOK.md](./RUNBOOK.md) |
| Observability (logs / metrics / dashboard source) | Ready | [RUNBOOK.md](./RUNBOOK.md), [`/api/stats`](./Week14_Final_SahahaAI/app.py) |
| Test evidence | Ready | [test_submission.py](./Week14_Final_SahahaAI/tests/test_submission.py) |
| Security automation | Ready | [week14-final-security.yml](./.github/workflows/week14-final-security.yml), [dependabot.yml](./.github/dependabot.yml) |
| Documentation artifact | Ready | [ADR.md](./ADR.md), [MODEL_CARD.md](./MODEL_CARD.md), [CHANGELOG.md](./CHANGELOG.md), [RUNBOOK.md](./RUNBOOK.md) |
| Release tag `v1.0.0+` | Ready | `v1.0.0` |
| Retrospective | Ready | [RETROSPECTIVE.md](./RETROSPECTIVE.md) |
| 3-minute demo script | Ready | [DEMO.md](./DEMO.md) |
| Public live URL | Pending platform login | [DEPLOYMENT.md](./DEPLOYMENT.md) |
| Recorded demo video URL | Pending recording/upload | [DEMO.md](./DEMO.md) |

## What the Final App Does

- Provides a working FastAPI chat UI and API
- Answers public-service questions from Saha-gu residents
- Uses official Saha-gu staff-directory data for department and phone-number answers
- Blocks personal-information input and sanitizes replies
- Shows highlighted key answer text in the chat UI

## Repository Artifacts

- Final app source: [Week14_Final_SahahaAI](./Week14_Final_SahahaAI)
- Deployment guide: [DEPLOYMENT.md](./DEPLOYMENT.md)
- Runbook and rollback plan: [RUNBOOK.md](./RUNBOOK.md)
- Architecture decision record: [ADR.md](./ADR.md)
- Changelog: [CHANGELOG.md](./CHANGELOG.md)
- Model card: [MODEL_CARD.md](./MODEL_CARD.md)
- Retrospective: [RETROSPECTIVE.md](./RETROSPECTIVE.md)
- Demo script: [DEMO.md](./DEMO.md)

## Deployment

### Render

- Blueprint file: [render.yaml](./render.yaml)
- App root directory: `Week14_Final_SahahaAI`
- Health check path: `/healthz`

### Railway

- Docker deployment is supported through [Week14_Final_SahahaAI/Dockerfile](./Week14_Final_SahahaAI/Dockerfile)
- Set the service root to `Week14_Final_SahahaAI` or point Railway to that Dockerfile

See [DEPLOYMENT.md](./DEPLOYMENT.md) for the exact steps.

## Validation Performed

```bash
cd Week14_Final_SahahaAI
python -m py_compile app.py main.py config.py chatbot/dept_directory.py crawler/staff_directory.py
python -m unittest discover -s tests -v
```

## Current Submission Risk Check

- Repository requirements: satisfied
- CI / test / security / documentation requirements: satisfied
- Live deployment URL: not automatically completable from this local workspace because platform account authentication is required
- Demo video: not automatically completable because recording and upload require user/platform action

## Notes

- `.env` is intentionally excluded from version control.
- The final code was migrated from the team repository into this personal submission repository.
- For the course portal, the last remaining manual items are the public deployment URL and the uploaded demo video URL.
