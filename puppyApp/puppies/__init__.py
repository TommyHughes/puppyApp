from flask import Blueprint

bp = Blueprint("puppies",__name__)

from puppyApp.puppies import views