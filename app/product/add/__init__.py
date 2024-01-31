from flask import Blueprint

bp = Blueprint("product", __name__, url_prefix="/add")

from app.routes.product import add