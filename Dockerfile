# Use Python 3.11
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose ports: Streamlit and Ollama
EXPOSE 8501 11434

# Entry point: start Ollama in background and then Streamlit
CMD ollama serve --host 0.0.0.0 & streamlit run Frontend.py --server.port 8501 --server.address 0.0.0.0
