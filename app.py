
from flask import Flask, jsonify
import os

app = Flask(__name__)
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

@app.route("/")
def home():
    return "Log Monitoring App running in Docker 🚀"

@app.route("/logs")
def logs():
    with open(LOG_FILE) as f:
        return jsonify(f.readlines())

@app.route("/errors")
def errors():
    with open(LOG_FILE) as f:
        return jsonify([line for line in f if "ERROR" in line])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
