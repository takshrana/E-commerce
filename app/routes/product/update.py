import os
from flask import render_template, url_for, redirect, request, flash
from app.extensions import db
from flask_login import current_user
from functools import wraps
from app.product.update import bp
from app.models.product import Category, Metal, Color, Style, Product
from app.forms.product import AddCategoryForm, AddMetalForm, AddStyleForm, AddColorForm, AddProductForm
from app.routes.product.add import allowed_file, secure_filename


def admin_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return function(*args, **kwargs)
        else:
            return render_template('404.html')
    return wrapper


@bp.route('/category', methods=['GET'])
@admin_only
def display_category():
    items = get_all_category()
    return render_template('product/update/display.html', items=items)


@bp.route('/metal', methods=['GET'])
@admin_only
def display_metal():
    items = get_all_metal()
    return render_template('product/update/display.html', items=items)


@bp.route('/style', methods=['GET'])
@admin_only
def display_style():
    items = get_all_style()
    return render_template('product/update/display.html', items=items)


@bp.route('/color', methods=['GET'])
@admin_only
def display_color():
    items = get_all_color()
    return render_template('product/update/display.html', items=items)


@bp.route('/product/', methods=['GET'])
@admin_only
def display_all_product(category_id=1, metal_id=1, color_id=1, style_id=1):
    items = get_all_product()

    category = db.session.execute(db.select(Category)).scalars()
    metals = db.session.execute(db.select(Metal)).scalars()
    colors = db.session.execute(db.select(Color)).scalars()
    styles = db.session.execute(db.select(Style)).scalars()

    return render_template('product/update/display_product.html', items=items,
                           categories=category, metals=metals, styles=styles, colors=colors,
                           category_id=category_id, metal_id=metal_id, style_id=style_id,
                           color_id=color_id, all_item=True
                           )


# @bp.route('/product/', methods=['GET'])
@bp.route('/product/<int:category_id>/<int:metal_id>/<int:color_id>/<int:style_id>', methods=['GET'])
@admin_only
def display_product(category_id=1, metal_id=1, color_id=1, style_id=1):
    items = db.session.execute(db.select(Product).filter_by(category_id=category_id,
                                                            metal_id=metal_id,
                                                            color_id=color_id,
                                                            style_id=style_id,)).scalars()
    category = db.session.execute(db.select(Category)).scalars()
    metals = db.session.execute(db.select(Metal)).scalars()
    colors = db.session.execute(db.select(Color)).scalars()
    styles = db.session.execute(db.select(Style)).scalars()

    return render_template('product/update/display_product.html', items=items,
                           categories=category, metals=metals, styles=styles, colors=colors,
                           category_id=category_id, metal_id=metal_id, style_id=style_id,
                           color_id=color_id, all_item=False
                           )


@bp.route('/category/availability/<int:item_id>', methods=['GET'])
@admin_only
def update_category(item_id):
    item = db.get_or_404(Category, item_id)
    if item.active:
        item.active = False
        products = db.session.execute(db.select(Product).filter_by(active=True, category_id=item_id)).scalars()
        for product in products:
            product.active = False
    else:
        item.active = True

    db.session.commit()
    return redirect(url_for('update.display_category'))


@bp.route('/metal/availability/<int:item_id>', methods=['GET'])
@admin_only
def update_metal(item_id):
    item = db.get_or_404(Metal, item_id)
    if item.active:
        item.active = False
        products = db.session.execute(db.select(Product).filter_by(active=True, metal_id=item_id)).scalars()
        for product in products:
            product.active = False
    else:
        item.active = True

    db.session.commit()
    return redirect(url_for('update.display_metal'))


@bp.route('/style/availability/<int:item_id>', methods=['GET'])
@admin_only
def update_style(item_id):
    item = db.get_or_404(Style, item_id)
    if item.active:
        item.active = False
        products = db.session.execute(db.select(Product).filter_by(active=True, style_id=item_id)).scalars()
        for product in products:
            product.active = False
    else:
        item.active = True

    db.session.commit()
    return redirect(url_for('update.display_style'))


@bp.route('/color/availability/<int:item_id>', methods=['GET'])
@admin_only
def update_color(item_id):
    item = db.get_or_404(Color, item_id)
    if item.active:
        item.active = False
        products = db.session.execute(db.select(Product).filter_by(active=True, color_id=item_id)).scalars()
        for product in products:
            product.active = False
    else:
        item.active = True

    db.session.commit()
    return redirect(url_for('update.display_metal'))


@bp.route('/product/availability/<int:item_id>', methods=['GET'])
@admin_only
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


@bp.route('/category/edit/<int:item_id>', methods=['GET', 'POST'])
@admin_only
def edit_category(item_id):
    item = db.get_or_404(Category, item_id)
    form = AddCategoryForm(name=item.name)
    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Category).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
            return redirect(url_for('update.edit_category', item_id=item_id))
        else:
            item.name = name
            db.session.commit()
            return redirect(url_for('update.display_category'))

    return render_template('product/edit/edit_template.html', form=form, item_id=item_id)


@bp.route('/metal/edit/<int:item_id>', methods=['GET', 'POST'])
@admin_only
def edit_metal(item_id):
    item = db.get_or_404(Metal, item_id)
    form = AddMetalForm(name=item.name)

    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Metal).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
            return redirect(url_for('update.edit_metal', item_id=item_id))
        else:
            item.name = name
            db.session.commit()
            return redirect(url_for('update.display_metal'))

    return render_template('product/edit/edit_template.html', form=form, item_id=item_id)


@bp.route('/color/edit/<int:item_id>', methods=['GET', 'POST'])
@admin_only
def edit_color(item_id):
    item = db.get_or_404(Color, item_id)
    form = AddColorForm(name=item.name)

    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Color).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
            return redirect(url_for('update.edit_color', item_id=item_id))
        else:
            item.name = name
            db.session.commit()
            return redirect(url_for('update.display_color'))

    return render_template('product/edit/edit_template.html', form=form, item_id=item_id)


@bp.route('/style/edit/<int:item_id>', methods=['GET', 'POST'])
@admin_only
def edit_style(item_id):
    item = db.get_or_404(Style, item_id)
    form = AddStyleForm(name=item.name)

    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Style).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
            return redirect(url_for('update.edit_style', item_id=item_id))
        else:
            item.name = name
            db.session.commit()
            return redirect(url_for('update.display_style'))

    return render_template('product/edit/edit_template.html', form=form, item_id=item_id)


@bp.route('/product/edit/<int:item_id>', methods=['GET', 'POST'])
@admin_only
def edit_product(item_id):
    item = db.get_or_404(Product, item_id)
    form = AddProductForm(name=item.name, price=item.price, stock=item.stock)
    categories = db.session.execute(db.select(Category).filter_by(active=True)).scalars()
    metals = db.session.execute(db.select(Metal).filter_by(active=True)).scalars()
    colors = db.session.execute(db.select(Color).filter_by(active=True)).scalars()
    styles = db.session.execute(db.select(Style).filter_by(active=True)).scalars()

    if request.method == 'POST':
        file = form.img.data
        print(file)
        img_url = None
        name = form.name.data.title()
        stock = form.stock.data
        price = form.price.data
        category = request.form['category_id']
        metal = request.form['metal_id']
        color = request.form['color_id']
        style = request.form['style_id']

        exist = db.session.execute(db.select(Product).filter_by(name=name, stock=stock,
                                                                category_id=category,
                                                                metal_id=metal,
                                                                color_id=color,
                                                                style_id=style,
                                                                price=price)).scalar()
        if exist:
            flash('Already Exist')
            return redirect(url_for('update.edit_product', item_id=item_id))
        else:
            if file and allowed_file(file.filename):
                num = db.session.execute(db.select(Product).order_by(Product.id.desc())).scalar().id + 1
                file.filename = f"product_{item.id}.{file.filename.rsplit('.', 1)[1].lower()}"
                img_url = secure_filename(file.filename)
                file.save(os.path.join('app/static/img/products', img_url))
                item.img_url = img_url

            item.name = name
            item.stock = stock
            item.price = price
            item.category_id = category
            item.metal_id = metal
            item.color_id = color
            item.style_id = style

            db.session.commit()
            return redirect(url_for('update.display_product', category_id=category,
                                    metal_id=metal, color_id=color, style_id=style))

    return render_template('product/edit/edit_product.html', item_id=item_id,
                           form=form, categories=categories, metals=metals, styles=styles,
                           colors=colors,category_id=item.category_id, metal_id=item.metal_id,
                           style_id=item.style_id, color_id=item.color_id)


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
