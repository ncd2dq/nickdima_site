from flask import Blueprint, render_template, request, session, redirect, url_for
from silk_thai.food_db import get_db

bp = Blueprint('food', __name__, url_prefix='/thai/food', static_folder='static', template_folder='template')

#portion will be /dinner or /lunch
@bp.route('/<string:item>/<string:portion>', methods=['GET', 'POST'])
def food_pdp(item, portion):
    db = get_db()

    if request.method == 'POST':
        spice = request.form.get('spice')
        base = request.form.get('base')
        extra_rice = request.form.get('extra_rice')
        notes = request.form.get('custom_modify')
        topping = request.form.get('topping')
        extra = request.form.get('extra')
        portion = request.form.get('portion_type')

        # Ensure all form values exist
        spice = ensureExists(spice)
        base = ensureExists(base)
        extra_rice = ensureExists(extra_rice)
        notes = ensureExists(notes)
        topping = ensureExists(topping)
        extra = ensureExists(extra)
        portion = ensureExists(portion)

        # These 2 can contain "+$3" in it, and that needs to be removed
        topping = removePricing(topping)
        extra = removePricing(extra)

        # Final value should be:
        # {'Base': ('Pad_see_ew', 10.95), 'Spice': 'Normal', 'Topping': ('Shrimp', 2), 'Extra': ('Pork', 3), 'Extra_Rice': '2', 'Notes': 'Hello Test'}
        new_item = {'Title': False, 'Base':False, 'Spice':False, 'Topping':False, 'Extra':False, 'Extra_Rice':False, 'Portion':False, 'Notes':False, 'Img_url':False, 'Total':False}
        
        #
        # PARSE FORM DATA AND RETRIEVE PRICES FROM FOOD_DB - THIS ENSURES USERS CAN'T HACK PRICING
        #

        # Find the correct dictionary key
        for key in db.keys():
            if db[key]['Base'] == base:
                new_item['Title'] = db[key]['Base']
                if portion == 'dinner':
                    new_item['Base'] = (key, db[key]['Base Price'])
                elif portion == 'lunch':
                    new_item['Base'] = (key, db[key]['Lunch_Version']['Base Price'])
                new_item['Img_url'] = db[key]['Img_URL']

        # Find the correct topping tuple [0] because the new_item['Base'] is a tuple
        if topping is not False:
            if portion == 'dinner':
                for name, price in db[new_item['Base'][0]]['Toppings']:
                    if topping == name:
                        new_item['Topping'] = (topping, price)
            elif portion == 'lunch':
                for name, price in db[new_item['Base'][0]]['Lunch_Version']['Toppings']:
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
        if portion is not False:
            new_item['Portion'] = portion
        if notes is not False:
            new_item['Notes'] = notes

        # Get the total
        total_price = 0
        for key in new_item.keys():
            if new_item[key] is not False:
                if type(new_item[key]) == tuple:
                    total_price += new_item[key][1]
                if key == 'Extra_Rice':
                    total_price += 2 * int(new_item[key])
        new_item['Total'] = total_price


        if 'cart' not in session:
            session['cart'] = [new_item]

            session['total'] = [total_price, 1]
        else:
            #For some reason session['cart'].append(new_item) does not work across requests,
            #need to alter the list, then reasign to the session
            #otherwise some data drops
            total = session['total']
            total[0] = float(total[0])
            total[0] += total_price
            total[0] = round(total[0], 2)
            total[0] = str(total[0])
            if total[0][-2] == '.':
                total[0] += '0'

            total[1] += 1
            session['total'] = total

            cur_cart = session['cart']
            cur_cart.append(new_item)
            session['cart'] = cur_cart

        # This was indented too much so it didn't work before the cart had an item in it
        if request.form.get('modal-dest') == 'to_cart':
            print("TRIED TO GO TO CART")
            return redirect(url_for('checkout.summary'))
        elif request.form.get('modal-dest') == 'to_menu':
            print("TRIED TO GO TO MENU")
            return redirect(url_for('menu.menu'))

    # Determine if the food item exists
    if db[item]:
        selected_item = db[item]
    else:
        # Or flash the error
        return "<h1>Our Apologies, that food item does not exist</h1>"

    # Do not allow users to go to lunch page for item if lunch version doesn't exist
    lunch_time = True
    if selected_item['Lunch_Version'] == False:
        lunch_time = False
    # TODO: replace with lunchtime calculation
    if portion == 'lunch' and selected_item['Lunch_Version'] == False:
        return redirect(url_for('food.food_pdp', item=item, portion='dinner'))

    return render_template('productpage/pdp.html', selected_item=selected_item, portion=portion, lunch_time=lunch_time)


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
