from flask import Flask, request, jsonify
from safetensors import safe_open
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

app = Flask(__name__)

# Load tensors from the model.safetensors file
tensors = {}
with safe_open("../model/model.safetensors", framework="pt", device="cpu") as f:
    for k in f.keys():
        tensors[k] = f.get_tensor(k)

# Assume tensors contains the necessary weights for your model.
# Load your model (replace 'your-model-name' with the actual name or path of your model)
local_bart_large_mnli_model = AutoModelForSequenceClassification.from_pretrained('../model')

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-mnli')

# Use the model and tokenizer with Hugging Face's classifier function.
classifier = pipeline('zero-shot-classification', model=local_bart_large_mnli_model, tokenizer=tokenizer)
