from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from silk_thai.food_db import get_db
from silk_thai.utilities import is_lunch, is_not_checkout_page, is_not_summary_page

bp = Blueprint('menu', __name__, url_prefix='/thai/menu', static_folder='static', template_folder='template')

@bp.route('/', methods=['GET'])
@is_not_checkout_page
@is_not_summary_page
def menu():
    db = get_db()
    session['from_summary'] = False

    lunch_time = is_lunch()

    print('IS IT LUNCH TIME', lunch_time)
    return render_template('menu/menu.html', all_items_dict=db, lunch_time=lunch_time)
