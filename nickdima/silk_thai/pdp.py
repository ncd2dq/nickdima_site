from flask import Blueprint, render_template, request, session
from silk_thai.food_db import get_db

bp = Blueprint('food', __name__, url_prefix='/thai/food', static_folder='static', template_folder='template')

@bp.route('/<string:item>')
def food_pdp(item):
    db = get_db()

    if request.method == 'POST':
        spice = request.form.get('spice')
        base = request.form.get('base')
        topping = request.form.get('topping')
        extra = request.form.get('extra')
        extra_rice = request.form.get('extra_rice')
        notes = request.form.get('custom_modify')

        new_item = {'Base':False, 'Spice':False, 'Topping':False, 'Extra':False, 'Extra_Rice':False, 'Notes':False}
        if 'cart' not in session:
            session['cart'] = []
            session['cart'].append(new_item)
        else:
            session['cart'].append(new_item)

    # Determine if the food item exists
    if db[item]:
        selected_item = db[item]
    else:
        # Or flash the error
        return "<h1>Our Apologies, that food item does not exist</h1>"

    return render_template('productpage/pdp.html', selected_item=selected_item)


    if request.method == 'POST':
        items = []
        keys = request.form.keys()

        for key in keys:
            if request.form[key] != '0':
                items.append((key, request.form[key]))

        session['cart'] = items

        return redirect(url_for('checkout.summary'))

#Item name, spice level, topping + price, extra + price, amount of rice, extra notes


FULL_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2), ('Seafood', 3), ('Crispy Duck', 3)]
EXTRA_DINNER_TOPPINGS = [('None', 0), ('Chicken', 3), ('Pork', 3), ('Beef', 3), ('Veggie', 3), ('Shrimp', 5), ('Seafood', 5), ('Crispy Duck', 4)]
CURRY_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 3), ('Seafood', 3)]
FULL_LUNCH_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2)]
SPICE_RANGE = ['Normal', 0, 1, 2, 3, 4, 5] 
