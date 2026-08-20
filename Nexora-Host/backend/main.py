from flask import Flask, jsonify
from flask_cors import CORS

from database import init_db
from auth import register, login


app = Flask(__name__)
CORS(app)


init_db()


@app.route("/")
def home():
    return jsonify({
        "name": "Nexora Host",
        "version": "1.0",
        "status": "online"
    })


@app.route("/api/status")
def status():
    return jsonify({
        "system": "working"
    })


# Регистрация
@app.route("/api/register", methods=["POST"])
def register_user():
    return register()


# Вход
@app.route("/api/login", methods=["POST"])
def login_user():
    return login()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
