FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    git \
    curl \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN pip install uv
RUN uv pip install --no-cache --system torch --index-url https://download.pytorch.org/whl/cpu
RUN uv pip install --no-cache --system -r pyproject.toml --extra-index-url https://download.pytorch.org/whl/cpu --index-strategy unsafe-best-match
RUN uv pip install --no-cache --system "pydantic[email]"

COPY backend/app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
