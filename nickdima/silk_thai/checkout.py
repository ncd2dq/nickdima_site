from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from silk_thai.utilities import read_configuration_is_open, is_delivery_minimum_met, is_not_summary_page, is_not_checkout_page, CustomCurrency, is_accepting_delivery_takeout
from functools import wraps


bp = Blueprint('checkout', __name__, url_prefix='/thai/order', static_folder='static', template_folder='template')


def remove_item_from_session(remove_id):
    '''
    ::param remove_id:: string

    Remove an item from the cart by matching the remove_id to an item ID in cart
    '''
    cur_cart, cur_total = session['cart'], session['total']

    if cur_total[1] == 1:
        session.clear()

        return redirect(url_for('checkout.summary'))

    # Match the remove_id to an id from the cart and remove it from cart and total
    for item in cur_cart:

        if item['Id'] == int(remove_id):
            cur_total[0] = CustomCurrency(cur_total[0]) - CustomCurrency(item['Total'])
            cur_total[0] = cur_total[0].export_string()
            cur_total[1] -= 1
            session['total'] = cur_total
            cur_cart.remove(item)
            session['cart'] = cur_cart


@bp.route('/cart_remover', methods=['POST'])
@is_not_summary_page
@is_not_checkout_page
def cart_remover():
    '''
    A post request to this page will remove an item from the cart
    '''
    remove_id = request.form.get('remove_id')

    if remove_id:
        remove_item_from_session(remove_id)

    return redirect(url_for('checkout.summary'))


@bp.route('/summary', methods=['GET', 'POST'])
def summary():
    '''
    Summary page shows all items in cart and allows you to proceed to checkout
    wherein you will give customer information to process order
    '''
    if request.method == 'POST':
        # Securely store in session that user came from summary so a user cannot skip summary page
        session['from_summary'] = True

        if 'total' in session:
            order_type = request.form.get('order_type')

            if order_type == 'delivery' or order_type == 'takeout':
                # TODO validate that we are accepting takeout / delivery, that minimum is met
                session['order_type'] = order_type

            else:

                return redirect(url_for('checkout.summary'))

            return redirect(url_for('checkout.checkout'))

        else:
            # Cannot checkout with no items in cart
            return redirect(url_for('checkout.summary'))

    accept_delivery, accept_takeout = is_accepting_delivery_takeout()
    if read_configuration_is_open() and not accept_delivery and not accept_takeout:

        return render_template('checkout/not_accepting_online.html')
        
    # Check if there are any items in cart
    try:
        items = session['cart']

    except KeyError:

        return render_template('checkout/order_summary.html', 
                            empty_cart='No items in cart!',                            
                            is_currently_open=read_configuration_is_open(),
                            accept_delivery=accept_delivery,
                            accept_takeout=accept_takeout,
                            checkout_summary=True)

    cur_total = session['total']
    delivery_minimum_met = is_delivery_minimum_met(CustomCurrency(cur_total[0]))

    return render_template('checkout/order_summary.html', 
                            items=items, 
                            delivery_minimum_met=delivery_minimum_met, 
                            is_currently_open=read_configuration_is_open(),
                            accept_delivery=accept_delivery,
                            accept_takeout=accept_takeout,
                            checkout_summary=True
                            )


def is_open(view):
    '''
    Ensures that users can only proceed to checkout from the summary page if the store is open
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):

        if not read_configuration_is_open():

            return redirect(url_for('menu.menu'))

        return view(*args, **kwargs)

    return wrapped


def referred_by_summary_page(view):
    '''
    Ensures that users can only get to the checkout page from the summary page
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):
        # request.referrer is the full url 'http://www.nickdima.com/thai/order/summary'
        # url_for is just the end 'thai/order/summary'
        try:
            # If i just used referring urls then someone could spoof the checkout page
            # Need the second part of the if because when you get / post to checkout.checkout, it runs this
            # and post requests were False because request.referrer did not have checkout.summary in it
            if (
                    (
                        url_for('checkout.summary') in request.referrer 
                        and session['from_summary'] == True
                    )
                    or 
                    (
                        url_for('checkout.checkout') in request.referrer 
                        and request.method =='POST' 
                        and session['from_summary'] == True) 
                ):

                return view(*args, **kwargs)

            else:

                return redirect(url_for('menu.menu'))

        except Exception as e:

            return redirect(url_for('menu.menu')) 

    return wrapped


def referred_by_checkout_page(view):
    '''
    Ensures that users can only get to the confirmation page via the checkout page
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):
        # request.referrer is the full url 'http://www.nickdima.com/thai/order/summary'
        # url_for is just the end 'thai/order/summary'
        try:
            # If i just used referring urls then someone could spoof the checkout page
            if (
                    url_for('checkout.checkout') in request.referrer 
                    and session['from_checkout'] == True
                ):

                return view(*args, **kwargs)

            else:

                return redirect(url_for('menu.menu'))

        except Exception as e:

            return redirect(url_for('menu.menu')) 

    return wrapped


@bp.route('/checkout', methods=['GET', 'POST'])
@is_open
@referred_by_summary_page
def checkout():
    session['from_checkout'] = True

    if request.method == 'POST':
        #TODO
        #record customer information / payment information
        #include tip in total
        #charge credit card
        #email receipt to customer
        #email receipt to silk thai

        return redirect(url_for('checkout.confirmation'))

    items = session['cart']

    return render_template('checkout/order_checkout.html', 
                            items=items, 
                            checkout_summary=False, 
                            is_currently_open=read_configuration_is_open(),
                            item_count=1,
                            subtotal=2,
                            tax_total=3,
                            total_with_tax=400,
                            order_type=session['order_type'].capitalize()
                            )


@bp.route('/confirmation', methods=['GET'])
@is_not_summary_page
@referred_by_checkout_page
def confirmation():
    #
    #RECORD STORED CONFIRMATION DETAILS FROM SESSION TO DISPLAY ON THIS PAGE, THEN CLEAR SESSION
    #
    session.clear()

    return render_template('checkout/order_confirmation.html')