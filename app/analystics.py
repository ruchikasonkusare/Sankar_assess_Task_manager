from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Task
import pandas as pd

analytics = Blueprint("analytics", __name__)

@analytics.route("/analytics", methods=["GET"])
@login_required
def get_analytics():

    user_tasks = Task.query.filter_by(user_id=current_user.id).all()

    # EMPTY CASE
    if not user_tasks:
        return jsonify({
            "success": True,
            "analytics": {
                "total_tasks": 0,
                "completed_tasks": 0,
                "pending_tasks": 0,
                "in_progress_tasks": 0,
                "completion_percent": 0,
                "priority_breakdown": {}
            }
        }), 200

    # SAFE DATAFRAME
    data = pd.DataFrame([t.to_dict() for t in user_tasks])

    if "status" not in data.columns:
        data["status"] = ""

    if "priority" not in data.columns:
        data["priority"] = ""

    # CALCULATIONS
    total_tasks = len(data)
    completed_tasks = (data["status"] == "Completed").sum()
    pending_tasks = (data["status"] == "Pending").sum()
    in_progress_tasks = (data["status"] == "In Progress").sum()

    completion_percent = round((completed_tasks / total_tasks) * 100, 2) if total_tasks else 0

    priority_breakdown = data["priority"].value_counts().to_dict()

    return jsonify({
        "success": True,
        "analytics": {
            "total_tasks": total_tasks,
            "completed_tasks": int(completed_tasks),
            "pending_tasks": int(pending_tasks),
            "in_progress_tasks": int(in_progress_tasks),
            "completion_percent": completion_percent,
            "priority_breakdown": priority_breakdown
        }
    }), 200