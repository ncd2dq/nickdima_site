from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from datetime import datetime
from pytz import timezone
from functools import wraps

bp = Blueprint('checkout', __name__, url_prefix='/thai/order', static_folder='static', template_folder='template')


@bp.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
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

        view(*args, **kwargs)

    return wrapped

def referred_by_summary_page(view):
    '''
    Ensures that users can only get to the 
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):
        if request.referrer != url_for('checkout.summary'):
            print('REFFERED BY TRIED TO REDIRECT')
            print(request.referrer)
            print(url_for('checkout.summary'))
            return redirect(url_for('menu.menu'))
        else:
            print('REFERRED BY TRIED TO RUN ACTUAL VIEW')
            view(*args, **kwargs)

    return wrapped

# The route decorator must come first as it is what registers the function
# if it isn't first you'll register the unwrapped view
@bp.route('/confirmation', methods=['GET'])
@is_open
@referred_by_summary_page
def confirmation():

    return render_template('checkout/order_confirmation.html')


