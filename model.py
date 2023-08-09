import pprint
from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

classifier = pipeline(
    task="zero-shot-classification", device="1", model="facebook/bart-large-mnli"
)

# S = "I am not able to focus on my work"
# L = ["News", "Disease", "Attention"]

# predictions = classifier(S, L)
# pprint.pprint(predictions)


@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    text = data.get("text")
    labels = data.get("labels", [])

    if not text:
        return jsonify({"error": "Missing 'text' parameter"}), 400

    # Perform zero-shot classification
    predictions = classifier(text, labels)

    return jsonify({"Predictions": predictions})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
