from flask import render_template
from app.home import bp
from app.routes.product import get_all_product


@bp.route('/')
def index():
    products = get_all_product()
    return render_template('index.html', products=products)
