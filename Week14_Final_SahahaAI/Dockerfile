FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["sh", "-c", "python -m uvicorn app:app --host 0.0.0.0 --port ${PORT:-5000}"]
