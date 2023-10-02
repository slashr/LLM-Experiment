# Introduction
- This Model is based on Facebook's bart-large-mnli pretrained model provided by HuggingFace https://huggingface.co/facebook/bart-large-mnli
- It is a simple zero-shot-classification for sentiment analysis of a given text
- Providing custom labels is also supported

# Run Instructions
1. `docker build . -t zeroshot`
2. `docker run -p 5050:5050 zeroshot`
3. `curl -X POST -H "Content-Type: application/json" -d '{"text": "I love Hugging Face Transformers!", "labels": ["positive", "negative", "neutral"]}' http://localhost:5050/classify`

# Architecture
1. `app/`: Contains the application code
    - app.py: Flask App that serves the model at port 5050
    - model.py: Prepares the model and creates a zero-shot-classification pipeline
2. `model/`: Contains the model files cloned from https://huggingface.co/facebook/bart-large-mnli
    - model.safetensors: This is the model weights file that is downloaded by the Docker image and stored inside this directory. This is done so that the weights don't have to be downloaded everytime the docker image is run
