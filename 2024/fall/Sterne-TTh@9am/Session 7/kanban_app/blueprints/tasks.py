from flask import Blueprint, jsonify, request
from app import db
from app import Task

tasks_bp = Blueprint('tasks', __name__)

# API endpoint to get all tasks
@tasks_bp.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "status": task.status} for task in tasks]
    return jsonify(task_list)

# API endpoint to create a new task
@tasks_bp.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(title=data['title'], status="To Do")
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

# API endpoint to update task status
@tasks_bp.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        data = request.json
        task.status = data['status']
        db.session.commit()
        return jsonify({"message": "Task updated"}), 200
    else:
        return jsonify({"message": "Task not found"}), 404
