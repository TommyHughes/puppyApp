from flask import Blueprint, render_template

bp = Blueprint('main',__name__)

from puppyApp.main import views
