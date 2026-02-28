FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV CHROMA_PATH=/app/vector_db/chroma_storage/embedding_db

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    git \
    curl \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy only dependency files first (better caching) ----
COPY pyproject.toml uv.lock ./

# If using uv (recommended)
RUN pip install uv
RUN uv pip install --system

# If using classic requirements instead, use this instead:
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Install torch CPU
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir "pydantic[email]"

# ---- Copy ONLY backend code ----
COPY backend/app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
