from flask import request, jsonify
from database import connect
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    data = request.json

    username = data.get("username")
    email = data.get("email")
    password = hash_password(data.get("password"))

    db = connect()
    cursor = db.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, password)
        )

        db.commit()
        return jsonify({
            "message": "Аккаунт создан"
        })

    except:
        return jsonify({
            "error": "Email уже используется"
        })


def login():
    data = request.json

    email = data.get("email")
    password = hash_password(data.get("password"))

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT id, username, balance, role
        FROM users
        WHERE email=? AND password=?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        return jsonify({
            "id": user[0],
            "username": user[1],
            "balance": user[2],
            "role": user[3]
        })

    return jsonify({
        "error": "Неверные данные"
    })
