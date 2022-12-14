import sqlalchemy.exc
from flask import render_template, redirect, url_for

from .forms import AddUser, AddTask
from .models import User, Task, Link
from .extensions import db


def remove_user(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    users = db.session.query(Link).filter_by(user_id=user_id).all()
    db.session.delete(user)
    for i in users:
        db.session.delete(i)
    db.session.commit()

    return redirect(url_for("main.admin"))


def remove_task(task_id):
    task = db.session.query(Task).filter_by(id=task_id).first()
    tasks = db.session.query(Link).filter_by(task_id=task_id).all()
    db.session.delete(task)
    for i in tasks:
        db.session.delete(i)
    db.session.commit()

    return redirect(url_for("main.admin"))


def assign_task(user_id, task_id):
    link = Link(user_id, task_id)
    db.session.add(link)

    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return redirect(url_for("main.admin"))

    return redirect(url_for("main.admin"))
