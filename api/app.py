from flask import Flask, request, jsonify
from src.predict import predict_one

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "no url sent"}), 400
    return jsonify(predict_one(url))

if __name__ == "__main__":
    app.run(port=5000)
