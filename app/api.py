from flask import Flask, request, jsonify
from model import classifier

app = Flask(__name__)

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