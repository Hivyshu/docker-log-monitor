from flask import Flask, render_template, request
import os

app = Flask(__name__)
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# All logs page
@app.route("/logs")
def logs():
    keyword = request.args.get("search", "")
    with open(LOG_FILE) as f:
        lines = f.readlines()
    if keyword:
        lines = [line for line in lines if keyword.lower() in line.lower()]
    return render_template("logs.html", logs=lines, keyword=keyword)

# Error logs page
@app.route("/errors")
def errors():
    keyword = request.args.get("search", "")
    with open(LOG_FILE) as f:
        lines = [line for line in f if "ERROR" in line]
    if keyword:
        lines = [line for line in lines if keyword.lower() in line.lower()]
    return render_template("errors.html", logs=lines, keyword=keyword)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
