from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

classifier = pipeline(
    task="zero-shot-classification", model="facebook/bart-large-mnli"
)
