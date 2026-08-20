import sqlite3
from config import DATABASE


def connect():
    return sqlite3.connect(DATABASE)


def init_db():
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT UNIQUE,
        password TEXT,
        balance INTEGER DEFAULT 0,
        role TEXT DEFAULT 'user'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER,
        name TEXT,
        plan TEXT,
        status TEXT DEFAULT 'stopped'
    )
    """)

    db.commit()
    db.close()


if __name__ == "__main__":
    init_db()
    print("Database created!")
