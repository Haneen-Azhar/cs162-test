from flask import Flask, jsonify
from models import db, Task  # Import db and Task from models

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Root route to check if the app is running
@app.route('/')
def home():
    return 'Flask API is running!'

# Route to return tasks as a Python dictionary
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks_in_progress = [
        {'id': task.id, 'title': task.title, 'description': task.description}
        for task in Task.query.filter_by(status='In Progress').all()
    ]
    done_tasks = [
        {'id': task.id, 'title': task.title, 'description': task.description}
        for task in Task.query.filter_by(status='Done').all()
    ]

    return jsonify({
        'in_progress_tasks': tasks_in_progress,
        'done_tasks': done_tasks
    })

if __name__ == '__main__':
    app.run(debug=True)
