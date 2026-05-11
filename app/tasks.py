from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from app import db, socketIO
from app.models import Task

tasks = Blueprint('tasks', __name__)

# ---------------- DASHBOARD ----------------
@tasks.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ---------------- GET TASKS ----------------
@tasks.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()

    return jsonify({
        "success": True,
        "tasks": [t.to_dict() for t in user_tasks]
    }), 200


# ---------------- CREATE TASK ----------------
@tasks.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()

    if not data.get('title'):
        return jsonify({
            "success": False,
            "message": "Title is required"
        }), 400

    task = Task(
        title=data.get('title'),
        description=data.get('description', ""),
        priority=data.get('priority', 'Medium'),
        status=data.get('status', 'Pending'),
        user_id=current_user.id
    )

    db.session.add(task)
    db.session.commit()

    # Socket event
    socketIO.emit('task_added', task.to_dict(), broadcast=True)

    return jsonify({
        "success": True,
        "message": "Task created successfully",
        "task": task.to_dict()
    }), 201


# ---------------- UPDATE TASK ----------------
@tasks.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):

    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()

    if not task:
        return jsonify({
            "success": False,
            "message": "Task not found"
        }), 404

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.priority = data.get('priority', task.priority)
    task.status = data.get('status', task.status)

    db.session.commit()

    socketIO.emit('task_updated', task.to_dict(), broadcast=True)

    return jsonify({
        "success": True,
        "message": "Task updated successfully",
        "task": task.to_dict()
    }), 200


# ---------------- DELETE TASK ----------------
@tasks.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):

    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()

    if not task:
        return jsonify({
            "success": False,
            "message": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    socketIO.emit('task_deleted', {"id": task_id}, broadcast=True)

    return jsonify({
        "success": True,
        "message": "Task deleted successfully"
    }), 200