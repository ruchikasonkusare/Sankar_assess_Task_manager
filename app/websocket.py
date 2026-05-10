from app import socketio
from flask_socketio import emit
from flask_login import current_user

@socketio.on("connect")
def handle_connect():
    print(f"Client connected")
    emit("notification",{"message":"Connected to real time updates."})
    
@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected")

@socketio.on("task_status_change")
def handle_status_change(data):
    emit("notification", {
        "message": f"Task '{data.get('title')}' status changed to {data.get('status')}"
    }, broadcast=True)