from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf.csrf import generate_csrf
from app import db
from app.models import Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, csrf_token=generate_csrf())

@main.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description', '')
    task = Task(title=title, description=description, completed=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))