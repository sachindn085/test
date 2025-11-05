from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/generate-options", methods=["POST", "GET"])
def generate_options():
    # Get input text (works for both JSON or query param)
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        base_text = data.get("input", "").strip()
    else:
        base_text = request.args.get("input", "").strip()

    # Default fallback
    if not base_text:
        base_text = "Option"

    # Generate random options
    random_words = ["Alpha", "Beta", "Gamma", "Delta", "Omega", "Sigma", "Zeta", "Theta"]
    chosen = random.sample(random_words, 4)
    options = [f"{base_text} - {word}" for word in chosen]

    # ✅ Return just the list
    return jsonify(options)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
