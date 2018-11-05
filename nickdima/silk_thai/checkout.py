from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from datetime import datetime
from pytz import timezone
from functools import wraps

bp = Blueprint('checkout', __name__, url_prefix='/thai/order', static_folder='static', template_folder='template')

@bp.route('/cart_remover', methods=['POST'])
def cart_remover():
    remove_id = request.form.get('remove_id')

    if remove_id:
        # [item, item, item]
        cur_cart = session['cart']

        # [total, quantity]
        cur_total = session['total']

        if cur_total[1] == 1:
            session.clear()
            return redirect(url_for('checkout.summary'))

        for item in cur_cart:

            if item['Id'] == int(remove_id):
                cur_total[0] = float(cur_total[0])
                cur_total[0] -= item['Total']
                cur_total[0] = round(cur_total[0], 2)
                cur_total[0] = str(cur_total[0])
                if cur_total[0][-2] == '.':
                    cur_total[0] += '0'

                cur_total[1] -= 1
                session['total'] = cur_total

                print(cur_cart)
                # Remove item
                cur_cart.remove(item)
                print(cur_cart, 'AFTER REMOVAL')
                session['cart'] = cur_cart

    return redirect(url_for('checkout.summary'))

@bp.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        session['from_summary'] = True
        return redirect(url_for('checkout.confirmation'))

    try:
        items = session['cart']
    except KeyError:
        return render_template('checkout/order_summary.html', empty_cart='No items in cart!')

    return render_template('checkout/order_summary.html', items=items)


def is_open(view):
    '''
    Ensures that users can only proceed to checkout from the summary page if the store is open
    '''

    # Must use wraps or Flask doesn't know the correct name of the wrapped view function
    @wraps(view)
    def wrapped(*args, **kwargs):
        # Monday = 0, Sunday = 6
        # Hour in 1 - 24
        tz = timezone('EST')
        week_day, day_hour, day_minute = datetime.now(tz).weekday(), datetime.now(tz).time().hour, datetime.now(tz).time().minute    

        # Sunday - Thursday
        if week_day >= 0 and week_day <= 3 or week_day == 6:
            if day_hour <= 10:
                return redirect(url_for('menu.menu'))
            if day_hour >= 22:
                return redirect(url_for('menu.menu'))
            if day_hour == 21:
                if day_minute >= 30:
                    return redirect(url_for('menu.menu'))
        # Friday - Saturday
        elif week_day >= 4 and week_day <= 5:
            if day_hour <= 10:
                return redirect(url_for('menu.menu'))
            if day_hour >= 23:
                return redirect(url_for('menu.menu'))
            if day_hour == 22:
                if day_minute >= 30:
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


