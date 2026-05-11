from app import socketIO
from flask_socketio import emit
from flask_login import current_user

@socketIO.on("connect")
def handle_connect():
    print(f"Client connected")
    emit("notification",{"message":"Connected to real time updates."})
    
@socketIO.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected")

@socketIO.on("task_status_change")
def handle_status_change(data):
    emit("notification", {
        "message": f"Task '{data.get('title')}' status changed to {data.get('status')}"
    }, broadcast=True)