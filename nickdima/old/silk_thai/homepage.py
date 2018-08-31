from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for

bp = Blueprint('homepage', __name__, url_prefix='/thai/home')

@bp.route('/', methods=['GET'])
def home():

    return render_template('silk_thai/homepage/home.html')

@bp.route('/about', methods=['GET'])
def about():

    return render_template('silk_thai/homepage/about.html')

@bp.route('/contact', methods=['GET'])
def contact():

    return render_template('silk_thai/homepage/feedback_form.html')
