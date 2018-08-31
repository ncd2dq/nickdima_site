from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for

bp = Blueprint('menu', __name__, url_prefix='/thai/menu', static_folder='static', template_folder='template')

@bp.route('/', methods=['GET', 'POST'])
def menu():

    if request.method == 'POST':
        items = []
        keys = request.form.keys()

        for key in keys:
            if request.form[key] != '0':
                items.append((key, request.form[key]))

        session['cart'] = items

        return redirect(url_for('checkout.summary'))

    return render_template('menu/menu.html')
