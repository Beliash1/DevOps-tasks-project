from flask import Blueprint, request, jsonify
from app import db
from datetime import datetime

main = Blueprint('main', __name__)

# Task მოდელი (ცხრილის სტრუქტურა)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done,
            'created_at': self.created_at.isoformat()
        }

# Health check — Jenkins/Docker ამით ამოწმებს აპლიკაცია "ცოცხალია" თუ არა
@main.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

# ყველა task-ის წამოღება
@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200

# ახალი task-ის შექმნა
@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'title is required'}), 400

    task = Task(title=data['title'])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

# task-ის განახლება (მაგ. done=True)
@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.done = data.get('done', task.done)
    task.title = data.get('title', task.title)
    db.session.commit()
    return jsonify(task.to_dict()), 200

# task-ის წაშლა
@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204