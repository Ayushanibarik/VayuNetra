FROM python:3.11-slim

# Create non-root user with UID 1000 (Required for Hugging Face Spaces)
RUN useradd -m -u 1000 user
WORKDIR /home/user/app

# Install system libraries for OpenCV and PyTorch
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY --chown=user:user backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=user:user . /home/user/app

USER user
ENV HOME=/home/user \
    PYTHONUNBUFFERED=1 \
    PORT=7860

EXPOSE 7860

# Start FastAPI Uvicorn server on Hugging Face Spaces default port 7860
CMD ["python", "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "7860"]
