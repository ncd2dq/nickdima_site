from flask import Blueprint, render_template, url_for


bp = Blueprint('Stay_alive', __name__, url_prefix='/stay_alive', static_folder='static', template_folder='templates')

@bp.route('/')
def stay_alive_index():


    return render_template(url_for('Stay_alive.templates.index.html'))