FROM python:3.14-rc-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* README.md /app/

# IMPORTANT : on tolère les wheels manquantes
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi || true

COPY src/ /app/src/

EXPOSE 8000
CMD ["uvicorn", "eventhub.main:app", "--host", "0.0.0.0", "--port", "8000"]
