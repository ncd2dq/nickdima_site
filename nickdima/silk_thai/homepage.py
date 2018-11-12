from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from silk_thai.utilities import is_not_summary_page, is_not_checkout_page


bp = Blueprint('homepage', __name__, url_prefix='/thai/home', static_folder='static', template_folder='template')


@bp.route('/', methods=['GET'])
@is_not_summary_page
@is_not_checkout_page
def home():

    return render_template('homepage/home.html')


@bp.route('/about', methods=['GET'])
@is_not_summary_page
@is_not_checkout_page
def about():

    return render_template('homepage/about.html')


@bp.route('/contact', methods=['GET'])
@is_not_summary_page
@is_not_checkout_page
def contact():

    return render_template('homepage/feedback_form.html')
