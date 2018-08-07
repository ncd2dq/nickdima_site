from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for
)

from dbmysq import get_db


bp = Blueprint('lunchbreak', __name__, url_prefix='/lunchbreak')


@bp.route('/')
def home():

    return render_template('lunchbreak/index.html')


