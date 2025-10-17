from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello from Flask! 🐍 Host: {socket.gethostname()}"

@app.route('/app1')
def app1():
    return jsonify({
        "app": "App1",
        "host": socket.gethostname(),
        "region": os.getenv("REGION", "unknown")
    })

@app.route('/app2')
def app2():
    return jsonify({
        "app": "App2",
        "host": socket.gethostname(),
        "region": os.getenv("REGION", "unknown")
    })

@app.route('/health')
def health():
    return "Healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
