import sqlite3, json

with open("users.json") as f:
    users = json.load(f)

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

for u in users:
    cur.execute(
        "INSERT INTO users (id, name, username, password, role) VALUES (?, ?, ?, ?, ?)",
        (u["id"], u["name"], u["username"], u["password"], u["role"])
    )

conn.commit()
conn.close()
