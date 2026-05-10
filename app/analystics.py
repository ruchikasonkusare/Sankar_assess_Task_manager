from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Task
import pandas as pd
import numpy as np

analytics = Blueprint("analytics", __name__)

@analytics.route("/analytics", methods=["GET"])
@login_required
def get_analytics():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()

    if not user_tasks:
        return jsonify({
            "success": True,
            "analytics": {
                "total_tasks":         0,
                "completed_tasks":     0,
                "pending_tasks":       0,
                "in_progress_tasks":   0,
                "completion_percent":  0,
                "priority_breakdown":  {},
            }
        })

    # Convert to DataFrame using Pandas
    data = pd.DataFrame([t.to_dict() for t in user_tasks])

    total_tasks        = int(len(data))
    completed_tasks    = int(np.sum(data["status"] == "Completed"))
    pending_tasks      = int(np.sum(data["status"] == "Pending"))
    in_progress_tasks  = int(np.sum(data["status"] == "In Progress"))
    completion_percent = round(float(np.mean(data["status"] == "Completed") * 100), 2)

    priority_breakdown = data["priority"].value_counts().to_dict()

    return jsonify({
        "success": True,
        "analytics": {
            "total_tasks":        total_tasks,
            "completed_tasks":    completed_tasks,
            "pending_tasks":      pending_tasks,
            "in_progress_tasks":  in_progress_tasks,
            "completion_percent": completion_percent,
            "priority_breakdown": priority_breakdown,
        }
    }), 200