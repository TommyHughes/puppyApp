from flask import render_template
from puppyApp.main import bp

@bp.route('/')
def index():
    return render_template('home.html')