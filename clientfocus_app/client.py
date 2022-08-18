from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort
from .auth import login_required

from clientfocus_app.db import get_database

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

    #if request.method == 'POST':
        #age = 

    #return render_template('client/info.html', client=client)