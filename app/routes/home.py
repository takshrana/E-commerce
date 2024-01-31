from flask import render_template
from app.home import bp
from app.routes.update import get_active_product


@bp.route('/')
def index():
    products = get_active_product()
    return render_template('index.html', products=products)
