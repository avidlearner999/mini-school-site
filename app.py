from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("school.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/announcements")
def announcements():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM announcements ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("announcements.html", announcements=rows)

@app.route("/add-announcement", methods=["GET", "POST"])
def add_announcement():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO announcements (title, content, created_at) VALUES (?, ?, datetime('now'))",
            (title, content)
        )
        conn.commit()
        conn.close()

        return redirect("/announcements")

    return render_template("add_announcement.html")

if __name__ == "__main__":
    app.run(debug=True)
