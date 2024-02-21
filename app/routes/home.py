from flask import render_template
from app.home import bp
from app.extensions import db
from app.models.product import Product
from app.routes.product.update import get_active_product


@bp.route('/')
def index():
    products = get_active_product()
    return render_template('index.html', products=products)

@bp.route('/product/<int:p_id>')
def display_product(p_id):
    product = db.session.execute(db.select(Product).filter_by(id=p_id)).scalar()
    return render_template('product/product-page.html', product=product)