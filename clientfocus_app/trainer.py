from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort
from .auth import login_required

from clientfocus_app.db import get_database

from datetime import datetime

bp = Blueprint('trainer', __name__)

@bp.route('/')
@login_required
def index():
    database = get_database()
    trainer = g.user['id']
    clients = database.execute(
        """SELECT client.id, name
        FROM client
        INNER JOIN user on client.trainer_id = ?
        ORDER BY name ASC""", (trainer,)
    ).fetchall()
    return render_template('trainer/index.html', clients=clients, trainer=trainer)

@bp.route('/addclient', methods=('GET', 'POST'))
@login_required
def addclient():
    if request.method == 'POST':
        trainer_id = g.user['id']
        name = request.form['name']
        age = request.form['age']
        date_of_birth = request.form['date_of_birth']
        goals = request.form['goals']
        notes = request.form['notes']
        error = None

        if not name:
            error = 'Client name is required!'
        if not age:
            error = 'Client age is required!'
        if not date_of_birth:
            error = 'Client date of birth is required!'
        try:
            datetime.strptime(date_of_birth, "%m/%d/%Y")
        except ValueError:
            error = 'Client date of birth is not in the correct format!'
        
        if error is not None:
            flash(error)
        else:
            database = get_database()
            database.execute(
                """INSERT INTO client (trainer_id, name, age, date_of_birth, goals, notes)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (trainer_id, name, age, date_of_birth, goals, notes)
            )
            database.commit()
            return redirect(url_for('trainer.index'))

    return render_template('trainer/addclient.html')