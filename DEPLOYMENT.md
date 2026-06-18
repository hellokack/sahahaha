# DEPLOYMENT

## Current Status

The repository is deployment-ready, but the final public URL still requires deployment-platform authentication.

## Render Deployment

This repository includes [render.yaml](./render.yaml) for Render Blueprint deployment.

### Required Settings

- Repository: `hellokack/sahahaha`
- Root directory: `Week14_Final_SahahaAI`
- Health check path: `/healthz`

### Required Environment Variables

- `SECRET_KEY`
- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_SERVICE_KEY`
- `ADMIN_API_KEY`
- Optional: `CORS_ALLOWED_ORIGINS`

### Expected Start Behavior

The app now respects the platform `PORT` environment variable.

## Railway Deployment

Railway deployment is also prepared through [Week14_Final_SahahaAI/Dockerfile](./Week14_Final_SahahaAI/Dockerfile).

### Railway Steps

1. Create a new project from the GitHub repository.
2. Select the service source from `Week14_Final_SahahaAI`, or point Railway to the included Dockerfile.
3. Set the required environment variables.
4. Generate a public domain.
5. Confirm `/healthz` returns `status=ok`.

## Why the Live URL Is Still Pending

Creating the final public URL requires a logged-in Render or Railway account and deployment permission on that platform.
That account-level action cannot be completed automatically from this local workspace alone.

## Final Manual Output To Record After Deployment

- Live URL: `TBD`
- Health check URL: `TBD/healthz`
- Demo video URL: `TBD`
