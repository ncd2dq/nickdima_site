from flask import Blueprint, render_template, request, session, redirect, url_for
from silk_thai.food_db import get_db

bp = Blueprint('food', __name__, url_prefix='/thai/food', static_folder='static', template_folder='template')

@bp.route('/<string:item>', methods=['GET', 'POST'])
def food_pdp(item):
    db = get_db()

    if request.method == 'POST':
        spice = request.form.get('spice')
        base = request.form.get('base')
        extra_rice = request.form.get('extra_rice')
        notes = request.form.get('custom_modify')

        # These 2 can contain " +$3" in it, and that needs to be removed
        print(topping)
        print(extra)
        topping = request.form.get('topping')
        extra = request.form.get('extra')
        topping = removePricing(topping)
        extra = removePricing(extra)
        print(topping)
        print(extra)

        #Item name, spice level, topping + price, extra + price, amount of rice, extra notes
        new_item = {'Base':False, 'Spice':False, 'Topping':False, 'Extra':False, 'Extra_Rice':False, 'Notes':False}
        
        #
        # PARSE FORM DATA AND RETRIEVE PRICES FROM FOOD_DB - THIS ENSURES USERS CAN'T HACK PRICING
        #

        # Find the correct dictionary key
        for key in db.keys():
            if db[key]['Base'] == base:
                new_item['Base'] = (key, db[key]['Base Price'])

        # Find the correct topping tuple [0] because the new_item['Base'] is a tuple
        for name, price in db[new_item['Base'][0]]['Toppings']:
            if topping == name:
                new_item['Topping'] = (topping, price)

        # Find the correct extra tuple
        for name, price in db[new_item['Base'][0]]['Extra']:
            if extra == name:
                new_item['Extra'] = (extra, price)

        new_item['Spice'] = spice 
        new_item['Extra_Rice'] = extra_rice
        new_item['Notes'] = notes


        if 'cart' not in session:
            session['cart'] = []
            session['cart'].append(new_item)
        else:
            session['cart'].append(new_item)

        print('TEST DATA')
        print(new_item)
        print(session['cart'])
        print('TEST DATA')

        return redirect(url_for('checkout.summary'))

    # Determine if the food item exists
    if db[item]:
        selected_item = db[item]
    else:
        # Or flash the error
        return "<h1>Our Apologies, that food item does not exist</h1>"

    return render_template('productpage/pdp.html', selected_item=selected_item)


def removePricing(form_val):
    '''Remove the " +$2" part of string from form values'''
    # Remove the +$2
    new_str = form_val.split('+')[0]

    # Remove the trailing space
    new_str = new_str[:-1]

    return new_str

