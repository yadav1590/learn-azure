from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure Python Web App!"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "python-webapp"
    }
