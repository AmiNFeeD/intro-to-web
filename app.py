from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from flask import redirect, url_for
import db

app = Flask(__name__)
socketio = SocketIO(app)

db.init_db()

@app.route("/clear", methods=["POST"])
def clear_history():
    db.clear_messages()
    return ("", 204)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/history")
def history():
    return jsonify(db.latest_messages())

@socketio.on("newuser")
def on_newuser(username):
    emit("history", db.latest_messages()[::-1], to=request.sid)
    emit("update", f"{username} joined", broadcast=True)

@socketio.on("chat")
def on_chat(data):
    db.save_message(data["username"], data["text"])
    emit("chat", data, broadcast=True, include_self=False)

@socketio.on("exituser")
def on_exit(username):
    emit("update", f"{username} left", broadcast=True)

if __name__ == "__main__":
    socketio.run(app, port=5001)
