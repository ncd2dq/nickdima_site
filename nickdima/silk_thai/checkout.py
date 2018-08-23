from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for

bp = Blueprint('checkout', __name__, url_prefix='/thai/order')

@bp.route('/summary', methods=['GET', 'POST'])
def summary():
    items = session['cart']
    if request.method == 'POST':
        return redirect(url_for('checkout.confirmation'))

    return render_template('silk_thai/checkout/order_summary.html', items=items)

@bp.route('/confirmation', methods=['GET'])
def confirmation():

    return render_template('silk_thai/checkout/order_confirmation.html')
#change where the form sends people in the static>assets>formoid>formoid.min.js
