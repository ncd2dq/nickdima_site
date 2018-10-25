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
        topping = request.form.get('topping')
        extra = request.form.get('extra')

        # Ensure all form values exist
        spice = ensureExists(spice)
        base = ensureExists(base)
        extra_rice = ensureExists(extra_rice)
        notes = ensureExists(notes)
        topping = ensureExists(topping)
        extra = ensureExists(extra)

        # These 2 can contain "+$3" in it, and that needs to be removed
        topping = removePricing(topping)
        extra = removePricing(extra)

        # Final value should be:
        # {'Base': ('Pad_see_ew', 10.95), 'Spice': 'Normal', 'Topping': ('Shrimp', 2), 'Extra': ('Pork', 3), 'Extra_Rice': '2', 'Notes': 'Hello Test'}
        new_item = {'Base':False, 'Spice':False, 'Topping':False, 'Extra':False, 'Extra_Rice':False, 'Notes':False}
        
        #
        # PARSE FORM DATA AND RETRIEVE PRICES FROM FOOD_DB - THIS ENSURES USERS CAN'T HACK PRICING
        #

        # Find the correct dictionary key
        for key in db.keys():
            if db[key]['Base'] == base:
                new_item['Base'] = (key, db[key]['Base Price'])

        # Find the correct topping tuple [0] because the new_item['Base'] is a tuple
        if topping is not False:
            for name, price in db[new_item['Base'][0]]['Toppings']:
                if topping == name:
                    new_item['Topping'] = (topping, price)

        # Find the correct extra tuple
        if extra is not False:
            for name, price in db[new_item['Base'][0]]['Extra']:
                if extra == name:
                    new_item['Extra'] = (extra, price)


        if spice is not False:
            new_item['Spice'] = spice 
        if extra_rice is not False:
            new_item['Extra_Rice'] = extra_rice
        if notes is not False:
            new_item['Notes'] = notes


        if 'cart' not in session:
            session['cart'] = []
            session['cart'].append(new_item)
        else:
            session['cart'].append(new_item)

        print('TEST DATA')
        print(new_item)
        print(session['cart'])
        print("END OF REQUEST SESSION SIZE: ", len(session['cart']))
        print('TEST DATA')
        import sys
        print('BYTE SIZE: ',sys.getsizeof(session['cart']))

        #session['cart'] = [val for val in range(1350)]
        #print(session['cart'])

        return redirect(url_for('checkout.summary'))

    # Determine if the food item exists
    if db[item]:
        selected_item = db[item]
    else:
        # Or flash the error
        return "<h1>Our Apologies, that food item does not exist</h1>"

    return render_template('productpage/pdp.html', selected_item=selected_item)

def ensureExists(form_val):
    '''Make sure that a form value exists'''
    if form_val is None:
        return False
    if form_val == '':
        return False
    return form_val

def removePricing(form_val):
    '''Remove the "+$2" part of string from form values'''
    if form_val is False:
        return False
    if '+$' in form_val:
        # Remove the +$2
        new_str = form_val.split('+')[0]
        return new_str
    return form_val
