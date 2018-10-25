from flask import Blueprint, render_template, request, session, redirect, url_for
from silk_thai.food_db import get_db

bp = Blueprint('food', __name__, url_prefix='/thai/food', static_folder='static', template_folder='template')

@bp.route('/<string:item>', methods=['GET', 'POST'])
def food_pdp(item):
    db = get_db()

    if request.method == 'POST':
        spice = request.form.get('spice')
        base = request.form.get('base')
        topping = request.form.get('topping')
        extra = request.form.get('extra')
        extra_rice = request.form.get('extra_rice')
        notes = request.form.get('custom_modify')

        print(spice, base, topping, extra, extra_rice, notes)

        new_item = {'Base':False, 'Spice':False, 'Topping':False, 'Extra':False, 'Extra_Rice':False, 'Notes':False}
        if 'cart' not in session:
            session['cart'] = []
            session['cart'].append(new_item)
        else:
            session['cart'].append(new_item)
        return redirect(url_for('checkout.summary'))

    # Determine if the food item exists
    if db[item]:
        selected_item = db[item]
    else:
        # Or flash the error
        return "<h1>Our Apologies, that food item does not exist</h1>"

    return render_template('productpage/pdp.html', selected_item=selected_item)

#Item name, spice level, topping + price, extra + price, amount of rice, extra notes


FULL_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2), ('Seafood', 3), ('Crispy Duck', 3)]
EXTRA_DINNER_TOPPINGS = [('None', 0), ('Chicken', 3), ('Pork', 3), ('Beef', 3), ('Veggie', 3), ('Shrimp', 5), ('Seafood', 5), ('Crispy Duck', 4)]
CURRY_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 3), ('Seafood', 3)]
FULL_LUNCH_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2)]
SPICE_RANGE = ['Normal', 0, 1, 2, 3, 4, 5] 

def parseItems(item, rice=False):
    '''
    #Take the form submissions that contain the name and price and return a tuple:
    ('Item name FROM FOOD_DB', Price)
    #If it's for extra rice, return
    ('rice', riceQuantity)
    '''