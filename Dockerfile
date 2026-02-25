FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files
COPY pyproject.toml .

# Install dependencies using uv
# --system flag to install into global site-packages since it's a container
RUN uv pip install --system --requirement pyproject.toml

# Copy source code
COPY . .

# Default port for Streamlit
EXPOSE 8501