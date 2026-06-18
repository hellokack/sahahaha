# RUNBOOK

## Service

- App folder: `Week14_Final_SahahaAI`
- Local start command: `python main.py --mode web`
- Default port: `5000`
- If port `5000` is busy, set `FLASK_PORT` to another value such as `5001`
- Health check: `GET /healthz`
- Metrics / admin stats: `GET /api/stats` with `X-Admin-Key`

## Deployment Plan

The intended release flow is:

1. Open a pull request into `main`
2. Pass the PR gate workflow
3. Merge into `main`
4. Deploy the `Week14_Final_SahahaAI` app with environment variables configured
5. Confirm `GET /healthz` returns `status=ok`

## Required Environment Variables

- `SECRET_KEY`
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_SERVICE_KEY`
- `ADMIN_API_KEY`

See `Week14_Final_SahahaAI/.env.example` for the local template.

## Health Check

Expected response:

```json
{
  "status": "ok",
  "service": "sahaha-ai",
  "version": "1.0.0"
}
```

## Rollback Plan

If a release fails:

1. Roll back to the previous Git tag or previous known-good commit.
2. Re-deploy the previous revision.
3. Re-run the health check on `/healthz`.
4. Confirm `/api/stats` and the chat UI respond normally.

Recommended rollback anchor:

- Latest stable release tag before the new deployment

## Observability

- Application logs: standard output plus `Week14_Final_SahahaAI/data/pipeline.log`
- Metrics endpoint: `/api/stats`
- Dashboard source: `/api/stats` JSON can be wired into a simple Grafana or spreadsheet dashboard

## Smoke Test

```bash
cd Week14_Final_SahahaAI
python main.py --mode web
curl http://127.0.0.1:5000/healthz
```
