# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing .pyc files and enable stdout logging
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV CHROMA_PATH=/app/vector_db/chroma_storage/embedding_db

# Install system dependencies for some Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libpq-dev \
        git \
        curl \
        libglib2.0-0 \
        && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies

COPY requirements/ml.txt requirements/ml.txt

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir "pydantic[email]"

# Then install the rest from requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .



CMD ["uvicorn", "api.main:app", "--host=0.0.0.0", "--port=8000"]
