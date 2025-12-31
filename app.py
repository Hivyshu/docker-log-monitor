from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
LOG_DIR = "logs"

# Helper to read logs
def read_logs(file_name, severity=None, keyword=None):
    file_path = os.path.join(LOG_DIR, file_name)
    lines = []
    if not os.path.exists(file_path):
        return lines
    with open(file_path) as f:
        lines = f.readlines()
    if severity:
        lines = [l for l in lines if severity.upper() in l]
    if keyword:
        lines = [l for l in lines if keyword.lower() in l.lower()]
    return lines

# Home page
@app.route("/")
def index():
    files = os.listdir(LOG_DIR)
    return render_template("index.html", files=files)

# View logs
@app.route("/logs")
def logs():
    file_name = request.args.get("file", "app.log")
    severity = request.args.get("severity", "")
    keyword = request.args.get("search", "")
    logs = read_logs(file_name, severity, keyword)
    files = os.listdir(LOG_DIR)
    return render_template("logs.html", logs=logs, files=files, current_file=file_name, severity=severity, keyword=keyword)

# Download logs
@app.route("/download")
def download():
    file_name = request.args.get("file", "app.log")
    file_path = os.path.join(LOG_DIR, file_name)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
