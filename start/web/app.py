from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

@app.route("/")
def index():
    notes = load_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = {"title": title, "content": content, "timestamp": timestamp}

        notes = load_notes()
        notes.append(note)
        save_notes(notes)
        return redirect(url_for("index"))
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
