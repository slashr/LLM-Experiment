FROM python:3.11-slim as base

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    python3-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN mkdir /model

# Download and store the model.safetensors file in model directory
# This prevents the Docker container from dowloading it on every run
RUN curl -L -o /model/model.safetensors https://huggingface.co/facebook/bart-large-mnli/resolve/main/model.safetensors

COPY app/ /app

COPY model/ /model

# Install dependencies and run app/model.py to load the pretrained model
RUN pip install --no-cache-dir -r app/requirements.txt && \
    python app/model.py

CMD ["python", "app/api.py"]
