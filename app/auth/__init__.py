from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix='/auth')

from app.routes import auth