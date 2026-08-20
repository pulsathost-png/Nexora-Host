from flask import Flask, jsonify
from flask_cors import CORS

from database import init_db
from auth import register, login
from servers import create_server, get_servers


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


# Аккаунты
@app.route("/api/register", methods=["POST"])
def register_user():
    return register()


@app.route("/api/login", methods=["POST"])
def login_user():
    return login()


# Серверы
@app.route("/api/server/create", methods=["POST"])
def server_create():
    return create_server()


@app.route("/api/server/list", methods=["GET"])
def server_list():
    return get_servers()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
