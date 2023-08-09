FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl

RUN pip install torch flask transformers

#ENV PATH="${PATH}:/root/.poetry/bin"

COPY app/ /app

RUN python app/model.py

CMD ["python", "app/api.py"]
