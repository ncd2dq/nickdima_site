from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from silk_thai.utilities import read_configuration_is_open, is_delivery_minimum_met, is_not_summary_page, CustomCurrency
from functools import wraps

bp = Blueprint('checkout', __name__, url_prefix='/thai/order', static_folder='static', template_folder='template')

def remove_item_from_session(remove_id):
    '''
    Remove an item from the cart by matching the remove_id to an item ID in cart
    '''
    
    # [item, item, item], [total-string, quantity-int]
    cur_cart, cur_total = session['cart'], session['total']

    # If they are removing the last item in the cart, clear whole session
    if cur_total[1] == 1:
        session.clear()
        return redirect(url_for('checkout.summary'))

    # Match the remove_id to an id from the cart
    for item in cur_cart:
        if item['Id'] == int(remove_id):
            # Subtract item price from order total
            cur_total[0] = CustomCurrency(cur_total[0])
            cur_total[0] -= CustomCurrency(item['Total'])
            cur_total[0] = cur_total[0].export_string()

            cur_total[1] -= 1
            session['total'] = cur_total

            # Remove item from cart
            cur_cart.remove(item)
            session['cart'] = cur_cart


@bp.route('/cart_remover', methods=['POST'])
@is_not_summary_page
def cart_remover():
    remove_id = request.form.get('remove_id')

    if remove_id:
        remove_item_from_session(remove_id)

    return redirect(url_for('checkout.summary'))

@bp.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        # Securely store in session that user came from summary so a user cannot skip summary page
        session['from_summary'] = True
        if 'total' in session:
            return redirect(url_for('checkout.confirmation'))
        else:
            # Cannot checkout with no items in cart
            return redirect(url_for('checkout.summary'))
    try:
        items = session['cart']
    except KeyError:
        return render_template('checkout/order_summary.html', empty_cart='No items in cart!')

    # Determine if delivery minimum met
    # session['tota'] -> [total, quantity]
    cur_total = session['total']
    delivery_minimum_met = is_delivery_minimum_met(CustomCurrency(cur_total[0]))

    return render_template('checkout/order_summary.html', items=items, delivery_minimum_met=delivery_minimum_met)


def is_open(view):
    '''
    Ensures that users can only proceed to checkout from the summary page if the store is open
    '''

    # Must use wraps or Flask doesn't know the correct name of the wrapped view function
    @wraps(view)
    def wrapped(*args, **kwargs):

        if not read_configuration_is_open():
            return redirect(url_for('menu.menu'))

        return view(*args, **kwargs)

    return wrapped

def referred_by_summary_page(view):
    '''
    Ensures that users can only get to the 
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):
        #request.referrer is the full url 'http://www.nickdima.com/thai/order/summary'
        #url_for is just the end 'thai/order/summary'
        try:
            # If i just used referring urls then someone could spoof the checkout page
            # TODO: refactor code so that the from_summary session is in a decorator
            if url_for('checkout.summary') in request.referrer and session['from_summary'] == True:
                print('SUCCESSFULLY REFERRED TO SUMMARY PAGE')
                return view(*args, **kwargs)
            else:
                return redirect(url_for('menu.menu'))
        except Exception as e:
            return redirect(url_for('menu.menu')) 

    return wrapped

# The route decorator must come first as it is what registers the function
# if it isn't first you'll register the unwrapped view
@bp.route('/confirmation', methods=['GET'])
@is_open
@referred_by_summary_page
def confirmation():
    session.clear()
    return render_template('checkout/order_confirmation.html')


