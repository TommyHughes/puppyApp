from flask import Blueprint

bp = Blueprint("owners",__name__)

from puppyApp.owners import views