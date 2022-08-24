from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort
from .auth import login_required

from clientfocus_app.db import get_database

bp = Blueprint('trainer', __name__)

@bp.route('/')
@login_required
def index():
    database = get_database()
    trainer = g.user['id']
    clients = database.execute(
        """SELECT id, first_name, last_name
        FROM client
        WHERE trainer_id = ?
        ORDER BY last_name ASC
        LIMIT 5""", (trainer,)
    ).fetchall()
    
    return render_template('trainer/index.html', clients=clients, trainer=trainer)

@bp.route('/addclient', methods=('GET', 'POST'))
@login_required
def addclient():
    if request.method == 'POST':
        trainer_id = g.user['id']
        first_name = request.form['first_name'].capitalize()
        last_name = request.form['last_name'].capitalize()
        age = request.form['age']
        goals = request.form['goals']
        notes = request.form['notes']
        error = None

        if not first_name:
            error = 'Client first name is required!'
        if not last_name:
            error = 'Client last name is required!'
        if not age:
            error = 'Client age is required!'
        
        if error is not None:
            flash(error)
        else:
            database = get_database()
            database.execute(
                """INSERT INTO client (trainer_id, first_name, last_name, age, goals, notes)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (trainer_id, first_name, last_name, age, goals, notes)
            )
            database.commit()
            flash('New client added successfully!')
            return redirect(url_for('trainer.index'))

    return render_template('trainer/addclient.html')