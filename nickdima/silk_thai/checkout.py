from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from datetime import datetime
from pytz import timezone

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




def is_open(outer_func):

    def wrapped(*args, **kwargs):
        # Monday = 0, Sunday = 6
        # Hour in 1 - 24
        tz = timezone('EST')
        week_day, day_hour, day_minute = datetime.now(tz).weekday(), datetime.now(tz).time().hour, datetime.now(tz).time().minute    
        print(week_day)
        print('TESTING THE WEKDAY FUNCTIONALITY FOR THE DECOATOR ----------------------')
        if week_day == 0:
            return "BRO YOU FAILED THIS TEST"

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

        outer_func(*args, **kwargs)

    return wrapped



@is_open
@bp.route('/confirmation', methods=['GET'])
def confirmation():

    return render_template('checkout/order_confirmation.html')
#change where the form sends people in the static>assets>formoid>formoid.min.js


