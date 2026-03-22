import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!", 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.errorhandler(404)
def not_found(e):
    return "Not Found", 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)
