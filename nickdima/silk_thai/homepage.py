from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for

bp = Blueprint('homepage', __name__, url_prefix='/thai/home', static_folder='static', template_folder='template')

@bp.route('/', methods=['GET'])
def home():

    return render_template('homepage/home.html')

@bp.route('/about', methods=['GET'])
def about():

    return render_template('homepage/about.html')

@bp.route('/contact', methods=['GET'])
def contact():

    return render_template('homepage/feedback_form.html')
