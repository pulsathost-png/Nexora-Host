from flask import request, jsonify
from database import connect


def create_server():

    data = request.json

    owner_id = data.get("owner_id")
    name = data.get("name")
    plan = data.get("plan")


    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO servers
        (owner_id, name, plan, status)
        VALUES (?, ?, ?, ?)
        """,
        (
            owner_id,
            name,
            plan,
            "stopped"
        )
    )


    db.commit()
    db.close()


    return jsonify({
        "message": "Сервер создан",
        "status": "stopped"
    })



def get_servers():

    owner_id = request.args.get("owner_id")


    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        SELECT id, name, plan, status
        FROM servers
        WHERE owner_id=?
        """,
        (owner_id,)
    )


    servers = cursor.fetchall()

    db.close()


    result = []

    for server in servers:
        result.append({
            "id": server[0],
            "name": server[1],
            "plan": server[2],
            "status": server[3]
        })


    return jsonify(result)
