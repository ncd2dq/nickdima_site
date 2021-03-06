from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from silk_thai.food_db import get_db
from silk_thai.utilities import is_lunch, is_not_checkout_page, is_not_summary_page

bp = Blueprint('menu', __name__, url_prefix='/thai/menu', static_folder='static', template_folder='template')


@bp.route('/', methods=['GET'])
@is_not_checkout_page
@is_not_summary_page
def menu():
    db = get_db()
    # TODO pull items from DB only if they are available
    # Also items that don't have ingredients that are not available
    lunch_time = is_lunch()

    return render_template('menu/menu.html', all_items_dict=db, lunch_time=lunch_time)
