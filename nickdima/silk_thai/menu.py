from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for

bp = Blueprint('menu', __name__, url_prefix='/thai/menu', static_folder='static', template_folder='template')

@bp.route('/', methods=['GET'])
def menu():

    try:
        print("BACK ON THE MENU PAGE AND CART SIZE IS: ", len(session['cart']))
        print('TEST DATA')
        import sys
        print('BYTE SIZE ON MENU PAGE: ',sys.getsizeof(session['cart']))

    return render_template('menu/menu.html')
