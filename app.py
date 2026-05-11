from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "dev")
BG_COLOR = os.getenv("BG_COLOR", "lightblue")

todos = [
    {"id": 1, "task": "Build Docker image", "done": False},
    {"id": 2, "task": "Push to registry", "done": False},
]

@app.route("/")
def index():
    return render_template("index.html", todos=todos, env=APP_ENV, bg=BG_COLOR)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    if task_text:
        new_id = max((t["id"] for t in todos), default=0) + 1
        todos.append({"id": new_id, "task": task_text, "done": False})
    return redirect(url_for("index"))

@app.route("/check/<int:todo_id>")
def check(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)