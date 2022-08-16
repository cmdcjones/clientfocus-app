from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort

from clientfocus_app.db import get_database

bp = Blueprint('trainer', __name__)

mock_clients = ['Trish Regan', 'Peng Chen', 'Tori Jung', 'Hunter Ghobadi']

@bp.route('/')
def index():
    database = get_database()
    clients = database.execute(
        """SELECT name
        FROM client
        INNER JOIN user on user.id = client.trainer_id"""
    ).fetchall()
    return render_template('trainer/index.html', clients=clients)