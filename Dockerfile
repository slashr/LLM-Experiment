FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl

COPY app/ /app

RUN pip install --no-cache-dir -r app/requirements.txt

RUN python app/model.py

CMD ["python", "app/api.py"]
