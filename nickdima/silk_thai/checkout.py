from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for

bp = Blueprint('checkout', __name__, url_prefix='/thai/order', static_folder='static', template_folder='template')

@bp.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        return redirect(url_for('checkout.confirmation'))

    try:
        items = session['cart']
    except KeyError:
        items = ['In Cart', 'No Items']
        return render_template('checkout/order_summary.html', items=items)

    return render_template('checkout/order_summary.html', items=items)

@bp.route('/confirmation', methods=['GET'])
def confirmation():

    return render_template('checkout/order_confirmation.html')
#change where the form sends people in the static>assets>formoid>formoid.min.js
