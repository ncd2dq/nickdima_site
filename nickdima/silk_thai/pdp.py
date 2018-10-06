from flask import Blueprint, render_template, request
from silk_thai.food_db import get_db

bp = Blueprint('food', __name__, url_prefix='/thai/food', static_folder='static', template_folder='template')

@bp.route('/<string:item>')
def food_pdp(item):
    db = get_db()

    if request.method == 'POST':
        #Post will put the item will all descriptions in their cart (cookie or local storage)
        pass

    if db[item]:
        selected_item = db[item]
    else:
        # Or flash the error
        return "<h1>Our Apologies, that food item does not exist</h1>"

    return render_template('productpage/pdp.html', selected_item=selected_item)