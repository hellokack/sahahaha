# ADR-001: Final Submission Architecture

## Status

Accepted

## Context

The final capstone submission needs a public GitHub repository, a working AI feature, a PR gate, health checks, rollback guidance, and observability evidence. The original team repository was not suitable for an individual submission, so the project needed a personal-repository mirror without secrets.

## Decision

We keep the final application in the `Week14_Final_SahahaAI` folder inside this repository and treat the repository root as the submission and operations layer.

Key decisions:

- Use FastAPI for the web server and chat API.
- Keep the RAG pipeline in Python with official Saha-gu data as the only answer source.
- Use the official Saha-gu staff directory as the source of truth for department contacts.
- Provide a lightweight PR gate through GitHub Actions using syntax checks and unit tests.
- Expose `GET /healthz` for health checks and `GET /api/stats` for operational metrics.
- Document rollback and deployment procedure in `RUNBOOK.md`.

## Consequences

- The repository satisfies the course OSS checklist more clearly than the original team repository.
- Secrets remain external because `.env` is excluded.
- The project is easier to review because submission documents live at the repository root and the executable app lives in one dedicated folder.
