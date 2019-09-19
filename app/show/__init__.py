from flask import Blueprint

test = Blueprint('show', __name__)

from . import views