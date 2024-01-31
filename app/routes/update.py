from flask import render_template, url_for, redirect
from app.extensions import db
from app.update import bp
from app.models.product import Category, Metal, Color, Style, Product


def get_all_category():
    result = db.session.execute(db.select(Category).order_by(Category.active.desc())).scalars()
    return result


def get_all_metal():
    result = db.session.execute(db.select(Metal).order_by(Metal.active.desc())).scalars()
    return result


def get_all_color():
    result = db.session.execute(db.select(Color).order_by(Color.active.desc())).scalars()
    return result


def get_all_style():
    result = db.session.execute(db.select(Style).order_by(Style.active.desc())).scalars()
    return result


def get_all_product():
    result = db.session.execute(db.select(Product).order_by(Product.active.desc())).scalars()
    return result


def get_active_product():
    result = db.session.execute(db.select(Product).filter_by(active=True)).scalars()
    return result


@bp.route('/category', methods=['GET'])
def display_category():
    items = get_all_category()
    return render_template('update/display.html', items=items)


@bp.route('/metal', methods=['GET'])
def display_metal():
    items = get_all_metal()
    return render_template('update/display.html', items=items)


@bp.route('/style', methods=['GET'])
def display_style():
    items = get_all_style()
    return render_template('update/display.html', items=items)


@bp.route('/color', methods=['GET'])
def display_color():
    items = get_all_color()
    return render_template('update/display.html', items=items)


@bp.route('/product', methods=['GET'])
@bp.route('/product/<int:category_id>/<int:metal_id>/<int:color_id>/<int:style_id>', methods=['GET', 'POST'])
def display_product(category_id=1, metal_id=1, color_id=1, style_id=1):
    items = db.session.execute(db.select(Product).filter_by(category_id=category_id,
                                                            metal_id=metal_id,
                                                            color_id=color_id,
                                                            style_id=style_id,)).scalars()
    category = db.session.execute(db.select(Category)).scalars()
    metals = db.session.execute(db.select(Metal)).scalars()
    colors = db.session.execute(db.select(Color)).scalars()
    styles = db.session.execute(db.select(Style)).scalars()

    return render_template('update/display_product.html', items=items,
                           categories=category, metals=metals, styles=styles, colors=colors,
                           category_id=category_id, metal_id=metal_id, style_id=style_id,
                           color_id=color_id
                           )


@bp.route('/category/availability/<int:item_id>', methods=['GET'])
def update_category(item_id):
    category = db.get_or_404(Category, item_id)
    if category.active:
        category.active = False
        products = db.session.execute(db.select(Product).filter_by(active=True, category_id=item_id)).scalars()
        for product in products:
            product.active = False
    else:
        category.active = True

    db.session.commit()
    return redirect(url_for('update.display_category'))


@bp.route('/product/availability/<int:item_id>', methods=['GET'])
def update_product(item_id):
    product = db.get_or_404(Product, item_id)
    if product.active:
        product.active = False
    else:
        product.active = True
        db.get_or_404(Category, product.category_id).active = True
        db.get_or_404(Metal, product.metal_id).active = True
        db.get_or_404(Style, product.style_id).active = True
        db.get_or_404(Color, product.color_id).active = True

    db.session.commit()
    return redirect(url_for('update.display_product', category_id=product.category_id, metal_id=product.metal_id,
                            style_id=product.style_id, color_id=product.color_id))

