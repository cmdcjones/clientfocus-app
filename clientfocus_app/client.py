from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort
from .auth import login_required

from clientfocus_app.db import get_database

from datetime import datetime

bp = Blueprint('client', __name__, url_prefix='/client')

def get_client(id,):
    client = get_database().execute(
        """SELECT id, name, age, date_of_birth, goals, notes
        FROM client
        WHERE id = ?""",
        (id,)
    ).fetchone()

    if client is None:
        abort(404, f'Sorry, that client does not exist!')

    return client

@bp.route('/<int:id>')
@login_required
def index(id):
    client = get_client(id)

    return render_template('client/index.html', client=client)

@bp.route('<int:id>/info')
@login_required
def info(id):
    client = get_client(id)

    return render_template('client/info.html', client=client)

@bp.route('<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    client = get_client(id)

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        date_of_birth = request.form['date_of_birth']
        goals = request.form['goals']
        notes = request.form['notes']
        error = None

        if not name:
            name = client['name']
        if not age:
            age = client['age']
        if not date_of_birth:
            date_of_birth = client['date_of_birth']
        if not goals:
            goals = client['goals']
        if not notes:
            notes = client['notes']
        try:
            datetime.strptime(date_of_birth, "%m/%d/%Y")
        except ValueError:
            error = 'Client date of birth is not in the correct format!'
        
        if error is not None:
            flash(error)
        else:
            database = get_database()
            database.execute(
                """UPDATE client
                    SET name = ?,
                        age = ?,
                        date_of_birth = ?,
                        goals = ?,
                        notes = ?
                    WHERE id = ?""",
                    (name, age, date_of_birth, goals, notes, client['id'])
            )
            database.commit()
            flash("Information updated successfully!")
            return redirect(url_for('client.update', id=client['id']))

    return render_template('client/update.html', client=client)

@bp.route('<int:id>/confirm_remove', methods=('GET', 'POST'))
@login_required
def confirm_remove(id):
    client = get_client(id)

    if request.method == 'POST':
        confirm = request.form['confirm']
        if confirm == 'Yes':
            return redirect(url_for('client.remove', id=client['id']))
        else:
            return redirect(url_for('client.index', id=client['id']))

    return render_template('client/confirm_remove.html', client=client)

@bp.route('/<int:id>/remove', methods=('GET', 'POST'))
@login_required
def remove(id):
    client = get_client(id)
    database = get_database()
    database.execute('DELETE FROM client WHERE id = ?', (client['id'],))
    database.commit()
    flash('Client removed successfully.')
    return redirect(url_for('trainer.index'))