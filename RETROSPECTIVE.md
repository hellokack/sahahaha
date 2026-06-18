# RETROSPECTIVE

## What Went Well

- The project reached a working AI assistant with both UI and API.
- Retrieval quality improved after official staff-directory integration for department and contact answers.
- Privacy handling became safer through front-end blocking and reply masking.
- The project accumulated enough documentation and operational context to be converted into a proper OSS submission.

## What Was Difficult

- Department names and phone numbers were initially inconsistent because free-form content and structured contacts were mixed.
- Korean text encoding and historical files made some edits more fragile than expected.
- The original team repository structure was not optimized for an individual final submission.

## What We Changed Late In The Project

- Added staff-directory crawling and contact enforcement.
- Removed visible HTML fragments from privacy warnings.
- Added dedicated submission documents, PR-gate workflow, and runbook material in the personal repository.

## What I Would Improve Next

- Add a fully automated production deployment target with secrets-managed hosting.
- Add a richer metrics dashboard on top of `/api/stats`.
- Expand automated eval coverage for department-routing and privacy cases.

## Final Reflection

The biggest lesson was that a useful AI feature is not enough by itself. The final submission also needs reproducibility, operational clarity, and safety evidence. Turning the team codebase into a personal OSS-style delivery highlighted how important documentation, release discipline, and testable interfaces are.
