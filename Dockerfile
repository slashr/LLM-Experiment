FROM python:3.11-slim as base

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl

COPY app/ /app

COPY model/ /model

RUN curl -L -o /model/model.safetensors https://huggingface.co/facebook/bart-large-mnli/resolve/main/model.safetensors

RUN pip install --no-cache-dir -r app/requirements.txt

RUN python app/model.py

CMD ["python", "app/api.py"]
