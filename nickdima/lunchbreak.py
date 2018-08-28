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


@bp.route('/minesweeper')
def minesweeper():

    return render_template('lunchbreak/games/minesweeper/index.html')

@bp.route('/asteroids')
def asteroids():

    return render_template('lunchbreak/games/asteroids/index.html')

@bp.route('/neuro_flappybird')
def neuro_flappybird():

    return render_template('lunchbreak/games/neuro_flappybird/index.html')

@bp.route('/highway_chase')
def highway_chase():

    return render_template('lunchbreak/games/highway_chase/index.html')

@bp.route('/towerdefense')
def towerdefense():

    return render_template('lunchbreak/games/tower_defense/index.html')