from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

# Secret key for sessions (necessary for Flask-Login)
app.config['SECRET_KEY'] = 'mysecretkey'

# Get the absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the SQLite database using the absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'kanban.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect unauthorized users to login page

# Define a Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), default="To Do")

# Define a User model for login purposes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database within application context
def create_tables():
    with app.app_context():
        db.create_all()

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Serve the front-end HTML page
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# API endpoint to get all tasks
@app.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "status": task.status} for task in tasks]
    return jsonify(task_list)

# API endpoint to create a new task
@app.route('/api/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.json
    new_task = Task(title=data['title'], status="To Do")
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created", "id": new_task.id, "title": new_task.title}), 201

# API endpoint to update task status
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        data = request.json
        task.status = data['status']
        db.session.commit()
        return jsonify({"message": "Task updated", "task": {"id": task.id, "title": task.title, "status": task.status}}), 200
    else:
        return jsonify({"message": "Task not found"}), 404

# API endpoint to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200
    else:
        return jsonify({"message": "Task not found"}), 404

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Use pbkdf2 hash method instead of scrypt
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

# User Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    create_tables()  # Call this function to create the tables on startup
    app.run(debug=True)
