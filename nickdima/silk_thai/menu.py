from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from silk_thai.food_db import get_db

bp = Blueprint('menu', __name__, url_prefix='/thai/menu', static_folder='static', template_folder='template')

@bp.route('/', methods=['GET'])
def menu():
    db = get_db()
    session['from_summary'] = False
    return render_template('menu/menu.html', all_items_dict=db)
