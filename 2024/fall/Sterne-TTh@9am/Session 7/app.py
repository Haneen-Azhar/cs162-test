from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from .forms import TaskForm, LoginForm, SignupForm
from .models import Task, User
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Kanban Board Route
@app.route('/', methods=['GET', 'POST'])
@login_required
def kanban():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('kanban'))

    tasks = Task.query.all()
    to_do_tasks = [task for task in tasks if task.status == 'To Do']
    in_progress_tasks = [task for task in tasks if task.status == 'In Progress']
    done_tasks = [task for task in tasks if task.status == 'Done']
    
    return render_template('kanban.html', form=form, to_do_tasks=to_do_tasks, 
                           in_progress_tasks=in_progress_tasks, done_tasks=done_tasks)

# Move Task Route
@app.route('/move_task/<int:task_id>/<string:new_status>')
@login_required
def move_task(task_id, new_status):
    task = Task.query.get(task_id)
    if task:
        task.status = new_status
        db.session.commit()
        flash('Task moved successfully!', 'success')
    return redirect(url_for('kanban'))

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('kanban'))
        else:
            flash('Login failed. Please check your email and password', 'danger')
    return render_template('login.html', form=form)

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
