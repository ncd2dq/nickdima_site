from flask import Blueprint, render_template, request, session, redirect, url_for
from silk_thai.food_db import get_db
from silk_thai.utilities import is_lunch, is_not_summary_page, is_not_checkout_page, CustomCurrency

bp = Blueprint('food', __name__, url_prefix='/thai/food', static_folder='static', template_folder='template')


@bp.route('/<string:item>/<string:portion>', methods=['GET', 'POST'])
@is_not_summary_page
@is_not_checkout_page
def food_pdp(item, portion):
    '''
    Food selection page where customers are presented all options for their food

    Get Request:
    Ensure that the food options shown are all currently available

    Post Request:
    Parse all forms and add the correct food item to the users cart 
    as well as update cart total price
    '''
    #TODO only pull items that are available
    #TODO remove the item's choices if the choices are unavailable
    db = get_db()
    
    if request.method == 'POST':
        spice, base, extra_rice, notes, topping, extra, portion_type = ensure_exists(get_all_pdp_forms())
        topping, extra = remove_pricing_symbol(topping, extra)
        #
        # Parse form data and compare to exisitng items in the food_db. Additionally, take pricing values
        # from the food database so that the client side doesn't send along price
        # this ensures safety and legitimacy of final order price
        #

        # TODO make new_item a class instead of all these different methods
        new_item = create_new_item()
        new_item = get_title_base_img_price(db, base, portion, new_item)
        new_item = get_topping(db, topping, portion, new_item)
        new_item = get_extra(db, extra, new_item)
        new_item = get_spice_rice_portion_notes(spice, extra_rice, portion_type, notes, new_item)

        # TODO CONTINUE PEP8-ING BELOW HERE
        # Get the total
        total_price = get_total_price(new_item)
        new_item['Total'] = total_price
        # total_price = CustomCurrency(0)
        # for key in new_item.keys():
        #     if new_item[key] is not False:
        #         if type(new_item[key]) == tuple:
        #             # ['name', str('3.00')]
        #             print('OH WOULD YOU LOOK HERE')
        #             print(total_price)
        #             print(new_item[key][1])
        #             total_price += CustomCurrency(new_item[key][1])
        #         elif key == 'Extra_Rice':
        #             total_price += CustomCurrency(2 * int(new_item[key]) * 100)
        # total_price = total_price.export_string()


        if 'cart' not in session:
            new_item['Id'] = 1
            session['cart'] = [new_item]

            session['total'] = [total_price, 1]
        else:
            #For some reason session['cart'].append(new_item) does not work across requests,
            #need to alter the list, then reasign to the session
            #otherwise some data drops
            #session['total'] = [str('3.00'), int]
            total = session['total']
            total[0] = CustomCurrency(total[0])
            total[0] += CustomCurrency(total_price)
            total[0] = total[0].export_string()

            total[1] += 1
            session['total'] = total

            cur_cart = session['cart']
            
            # Determine unique id for item
            all_ids = []
            for cur_item in cur_cart:
                all_ids.append(cur_item['Id'])
            new_item['Id'] = max(all_ids) + 1

            cur_cart.append(new_item)
            session['cart'] = cur_cart

        # This was indented too much so it didn't work before the cart had an item in it
        if request.form.get('modal-dest') == 'to_cart':
            print("TRIED TO GO TO CART")
            return redirect(url_for('checkout.summary'))
        elif request.form.get('modal-dest') == 'to_menu':
            print("TRIED TO GO TO MENU")
            return redirect(url_for('menu.menu'))

    #
    # Get Request
    #

    # Determine if the food item exists
    try:

        selected_item = db[item]
        selected_item = convert_all_prices_to_strings(selected_item)

    except KeyError:

        return "<h1>Our Apologies, that food item does not exist</h1>"

    lunch_time = is_lunch()
    if selected_item['Lunch_Version'] == False:
        lunch_time = False

    if portion == 'lunch' and selected_item['Lunch_Version'] == False:

        return redirect(url_for('food.food_pdp', item=item, portion='dinner'))

    if portion == 'dinner' and selected_item['Lunch_Only'] == True:

        return redirect(url_for('food.food_pdp', item=item, portion='lunch'))

    return render_template('productpage/pdp.html', selected_item=selected_item, portion=portion, lunch_time=lunch_time)


def convert_all_prices_to_strings(food_item_dict):
    '''
    Convert all prices within selected food object to strings to simplify front end
    '''
    food_item_dict['Base Price'] = CustomCurrency(food_item_dict['Base Price']).export_string()

    if food_item_dict['Toppings'] is not False:
        new_toppings_list = []

        for index, elm in enumerate(food_item_dict['Toppings']):
            new_elm = (elm[0], CustomCurrency(elm[1]).export_string())
            new_toppings_list.append(new_elm)

        food_item_dict['Toppings'] = new_toppings_list

    if food_item_dict['Extra'] is not False:
        new_extra_list = []

        for index, elm in enumerate(food_item_dict['Extra']):
            new_elm = (elm[0], CustomCurrency(elm[1]).export_string())
            new_extra_list.append(new_elm)

        food_item_dict['Extra'] = new_extra_list

    if food_item_dict['Lunch_Version'] is not False:
        food_item_dict['Lunch_Version']['Base Price'] = CustomCurrency(food_item_dict['Lunch_Version']['Base Price']).export_string()
        
        if food_item_dict['Lunch_Version']['Toppings'] is not False:
            new_lunch_toppings_list = []

            for index, elm in enumerate(food_item_dict['Lunch_Version']['Toppings']):
                new_elm = (elm[0], CustomCurrency(elm[1]).export_string())
                new_lunch_toppings_list.append(new_elm)

            food_item_dict['Extra'] = new_lunch_toppings_list

    return food_item_dict


def get_all_pdp_forms():
    '''
    Retrieves all forms from the PDP page
    '''
    spice = request.form.get('spice')
    base = request.form.get('base')
    extra_rice = request.form.get('extra_rice')
    notes = request.form.get('custom_modify')
    topping = request.form.get('topping')
    extra = request.form.get('extra')
    portion_type = request.form.get('portion_type')

    return spice, base, extra_rice, notes, topping, extra, portion_type


def ensure_exists(*args):
    '''
    Make sure that a form value exists or is False

    Note - *args puts all arguments inside a tuple and i'm already being passed a tuple
    tuple(tuple(form_val, form_val, form_val))

    '''
    form_val_list = []
    for form_val in args[0]:
        if form_val is None:
            form_val_list.append(False)

        elif form_val == '':
            form_val_list.append(False)

        else:
            form_val_list.append(form_val)

    return form_val_list


def remove_pricing_symbol(*args):
    '''Remove the "+$2" part of string from form values'''

    form_vals = []
    for form_val in args:

        if form_val is False:
            form_vals.append(False)

        elif '+$' in form_val:
            new_val = form_val.split('+')[0]
            form_vals.append(new_val)

        else:
            form_vals.append(form_val)

    return form_vals


#
# Functions for building new_item for cart from form submission ##############
#
# TODO make a class that recieves everything as an input in the __init__ and 'export' method spits out new_item
def create_new_item():
    '''
    Returns a new item template in the expected format for the cart

    {
    'Base': ('Pad_see_ew', '10.95'), 
    'Spice': 'Normal', 
    'Topping': ('Shrimp', '2.00'), 
    'Extra': ('Pork', '3.00'), 
    'Extra_Rice': '2', 
    'Notes': 'Hello Test'
    }
    '''
    new_item = {'Id': False, 'Title': False, 'Base':False, 'Spice':False, 'Topping':False, 'Extra':False, 'Extra_Rice':False, 'Portion_Type':False, 'Notes':False, 'Img_url':False, 'Total':False}

    return new_item


def get_title_base_img_price(db, base, portion, new_item):
    '''
    Match the base name of the selected food item to one of the food objects
    in the food database.

    ::param db:: python dictionary, food database
    ::param base:: string, name of the food from client matching the db['Green_curry']['Green Curry'] 'Green Curry' string
    ::param portion:: string, either 'lunch' or 'dinner'

    Fill the new item attributes :Title: :Base: :Img_url:
    '''
    for key in db.keys():
        if db[key]['Base'] == base:
            new_item['Title'] = db[key]['Base']
            if portion == 'dinner':
                new_item['Base'] = (key, CustomCurrency(db[key]['Base Price']).export_string())
            elif portion == 'lunch':
                new_item['Base'] = (key, CustomCurrency(db[key]['Lunch_Version']['Base Price']).export_string())
            new_item['Img_url'] = db[key]['Img_URL']

    return new_item


def get_topping(db, topping, portion, new_item):
    '''
    Matches the topping to the food database to determine if topping exists and what price
    it is based on dinner/lunch menu

    ::param db:: python dictionary, food database
    ::param topping:: string, name of a food topping like 'Chicken' 'Shrimp', etc.
    ::param portion:: string, either 'lunch' or 'dinner'

    Fill the new item attribute :Topping: with ('Name', 'X.XX')
    '''
    # Find the correct topping tuple [0] because the new_item['Base'] is a tuple ('Name', 'X.XX')
    if topping is not False:
        if portion == 'dinner':
            for name, price in db[new_item['Base'][0]]['Toppings']:
                if topping == name:
                    new_item['Topping'] = (topping, CustomCurrency(price).export_string())
        elif portion == 'lunch':
            for name, price in db[new_item['Base'][0]]['Lunch_Version']['Toppings']:
                if topping == name:
                    new_item['Topping'] = (topping, CustomCurrency(price).export_string())

    return new_item


def get_extra(db, extra, new_item):
    '''
    Matches the extra topping option to the food database to get the name and price

    ::param db:: python dictionary, food database
    ::param extra:: string, name of an extra food topping like 'Chicken' 'Shrimp', etc.

    Fill the new item attribute :Extra: with ('Name', 'X.XX')
    '''
    if extra is not False:
        for name, price in db[new_item['Base'][0]]['Extra']:
            if extra == name:
                new_item['Extra'] = (extra, CustomCurrency(price).export_string())

    return new_item


def get_spice_rice_portion_notes(spice, extra_rice, portion_type, notes, new_item):
    '''
    Adds the spice/extra_rice/portion_type/notes to the item being preparred
    for the cart

    ::param spice:: string, spice level
    ::param extra_rice:: string, amount of extra rice
    ::param portion_type:: string, 'lunch' or 'dinner'
    ::param notes:: string, any notes a customer has entered for a specific item

    Fill the new item attribute :Spice: :Extra_Rice: :Portion_Type: :Notes:
    '''
    if spice is not False:
        new_item['Spice'] = spice 
    if extra_rice is not False:
        new_item['Extra_Rice'] = extra_rice
    if portion_type is not False:
        new_item['Portion_Type'] = portion_type.capitalize()
    if notes is not False:
        new_item['Notes'] = notes

    return new_item


def get_total_price(new_item):
    '''
    Determine the string representation of the total price of the new_item in cart
    '''
    total_price = CustomCurrency(0)
    for key in new_item.keys():

        if new_item[key] is not False:

            # All toppings and things with prices are tuples of form ('Name', Price)
            if type(new_item[key]) == tuple:
                print('OH WOULD YOU LOOK HERE')
                print(total_price)
                print(new_item[key][1])
                total_price += CustomCurrency(new_item[key][1])

            # Extra_Rice is not a tuple, just a number indication how much extra rice
            elif key == 'Extra_Rice':
                total_price += CustomCurrency(2 * int(new_item[key]) * 100)

    return total_price.export_string()
