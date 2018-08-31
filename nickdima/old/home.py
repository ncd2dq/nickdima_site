import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from dbmysq import get_db

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/')
def home_index():
    if g.user is not None:
        username = g.user['username']

    return render_template('home/home2.html')

@bp.route('/about')
def about():

    return render_template('home/about.html')