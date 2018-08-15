from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for
)

from dbmysq import get_db


bp = Blueprint('lunchbreak', __name__, url_prefix='/lunchbreak')


@bp.route('/')
def home():

    return render_template('lunchbreak/index.html')


@bp.route('/tetris')
def tetris():

    return render_template('lunchbreak/games/tetris/index.html')


@bp.route('/snake')
def snake():

    return render_template('lunchbreak/games/snake/index.html')


@bp.route('/junglerun')
def junglerun():

    return render_template('lunchbreak/games/jungle_run/index.html')