from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, abort
import sqlite3

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecretkey"

def query_db(sql):
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    except Exception as e:
        print("SQL ERROR:", e)
        return []
    finally:
        conn.close()

@app.before_request
def require_login():
    public_routes = ["index", "login", "static", "logout"]
    if request.endpoint not in public_routes and "username" not in session:
        abort(404)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username","")
        password = request.form.get("password","")

        sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("LOGIN SQL:", sql)

        rows = query_db(sql)
        if rows:
            user = rows[0]
            session["username"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid login")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        abort(404)

    username = session.get("username")
    role = session.get("role")

    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = dict(cur.fetchone() or {})
    conn.close()

    flag = None
    if user.get("role") == "admin":
        flag = "LZS{SQL_IS_COOL}"

    return render_template("dashboard.html", user=user, flag=flag)

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("login"))

@app.route("/search", methods=["POST"])
def search():
    if "username" not in session:
        abort(404)
    search_term = request.form.get("search","")
    sql = f"SELECT name, role FROM users WHERE name LIKE '%{search_term}%'"
    print("SEARCH SQL:", sql)

    rows = query_db(sql)
    return jsonify({"results": rows})

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
