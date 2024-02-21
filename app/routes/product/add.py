import os
from flask import render_template, url_for, redirect, request, flash
from app.product.add import bp
from datetime import datetime
from flask_login import current_user
from app.extensions import db
from app.models.product import Product, Category, Style, Metal, Color
from app.forms.product import AddCategoryForm, AddProductForm, AddMetalForm, AddStyleForm,  AddColorForm
from werkzeug.utils import secure_filename
from functools import wraps

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def admin_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return function(*args, **kwargs)
        else:
            return render_template('404.html')
    return wrapper



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/product', methods=['GET', 'POST'])
@bp.route('product/<int:category_id>/<int:metal_id>/<int:color_id>/<int:style_id>', methods=['GET', 'POST'])
@admin_only
def add_product(category_id=1, metal_id=1, color_id=1, style_id=1):
    # display = ShowSubcategory()
    # display.options.choices = [g.name for g in choices]

    form = AddProductForm()
    categories = db.session.execute(db.select(Category).filter_by(active=True)).scalars()
    metals = db.session.execute(db.select(Metal).filter_by(active=True)).scalars()
    colors = db.session.execute(db.select(Color).filter_by(active=True)).scalars()
    styles = db.session.execute(db.select(Style).filter_by(active=True)).scalars()
    # form.category_id.choices = [(g.id, g.name) for g in category]
    choices = db.session.execute(db.select(Product).filter_by(category_id=category_id,
                                                              metal_id=metal_id,
                                                              color_id=color_id,
                                                              style_id=style_id,)).scalars()
    form.options.choices = [g.name for g in choices]

    if request.method == 'POST':
        file = form.img.data
        name = form.name.data.title()
        stock = form.stock.data
        price = form.price.data
        img_url = None
        # date = datetime.now().strftime('%Y-%m-%d')
        category = category_id
        metal = metal_id
        color = color_id
        style = style_id
        exist = db.session.execute(db.select(Product).filter_by(name=name,
                                                                category_id=category,
                                                                metal_id=metal,
                                                                color_id=color,
                                                                style_id=style,)).scalar()
        if exist:
            flash('Already Exist')
        else:
            if file and allowed_file(file.filename):
                num = db.session.execute(db.select(Product).order_by(Product.id.desc())).scalar().id + 1
                file.filename = f"product_{num}.{file.filename.rsplit('.', 1)[1].lower()}"
                img_url = secure_filename(file.filename)
                file.save(os.path.join('app/static/img/products', img_url))

            new_entry = Product(name=name,
                                stock=stock,
                                price=price,
                                img_url=img_url,
                                category_id=category,
                                metal_id=metal,
                                color_id=color,
                                style_id=style,)
            db.session.add(new_entry)
            db.session.commit()
        return redirect(url_for('product.add_product', category_id=category_id,
                                metal_id=metal_id, color_id=color_id, style_id=style_id))

    return render_template("product/add/add_product.html", form=form,
                           categories=categories, metals=metals, styles=styles, colors=colors,
                           category_id=category_id, metal_id=metal_id, style_id=style_id,
                           color_id=color_id)


@bp.route('/category', methods=['GET', 'POST'])
@admin_only
def add_category():
    category = db.session.execute(db.select(Category).filter_by(active=True)).scalars()
    form = AddCategoryForm()
    form.options.choices = [g.name for g in category]

    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Category).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
        else:
            new_entry = Category(name=name)
            db.session.add(new_entry)
            db.session.commit()
        return redirect(url_for('product.add_category'))

    return render_template("product/add/add_template.html", form=form)


@bp.route('/metal', methods=['GET', 'POST'])
@admin_only
def add_metal():
    choices = db.session.execute(db.select(Metal)).scalars()

    form = AddMetalForm()
    form.options.choices = [g.name for g in choices]
    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Metal).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
        else:
            new_entry = Metal(name=name)
            db.session.add(new_entry)
            db.session.commit()
        return redirect(url_for('product.add_metal'))

    return render_template("product/add/add_template.html", form=form)


@bp.route('/style', methods=['GET', 'POST'])
@admin_only
def add_style():
    choices = db.session.execute(db.select(Style)).scalars()
    form = AddStyleForm()
    form.options.choices = [g.name for g in choices]
    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Style).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
        else:
            new_entry = Style(name=name)
            db.session.add(new_entry)
            db.session.commit()
        return redirect(url_for('product.add_style'))

    return render_template("product/add/add_template.html", form=form)


@bp.route('/color', methods=['GET', 'POST'])
@admin_only
def add_color():
    choices = db.session.execute(db.select(Color)).scalars()
    form = AddColorForm()
    form.options.choices = [g.name for g in choices]
    if request.method == 'POST':
        name = form.name.data.title()
        exist = db.session.execute(db.select(Color).filter_by(name=name)).scalar()
        if exist:
            flash('Already Exist')
        else:
            new_entry = Color(name=name)
            db.session.add(new_entry)
            db.session.commit()
        return redirect(url_for('product.add_color'))

    return render_template("product/add/add_template.html", form=form)


# @bp.route('/subcategory', methods=['GET', 'POST'])
# @bp.route('/subcategory/<int:id>', methods=['GET', 'POST'])
# def add_subcategory(id=1):
#     # display = ShowSubcategory()
#     # display.options.choices = [g.name for g in choices]
#
#     form = AddSubcategoryForm()
#     category = db.session.execute(db.select(Category)).scalars()
#     # form.category_id.choices = [(g.id, g.name) for g in category]
#     choices = db.session.execute(db.select(Subcategory).filter_by(category_id=id)).scalars()
#     form.options.choices = [g.name for g in choices]
#
#     if request.method == 'POST':
#         name = form.name.data.capitalize()
#         category = id
#         new_entry = Subcategory(name=name, category_id=category)
#         db.session.add(new_entry)
#         db.session.commit()
#         return redirect(url_for('product.add_subcategory'))
#
#     return render_template("product/add_subcategory.html", form=form, categories=category, id=id)

# @bp.route('/', methods=['GET', 'POST'])
# def add_product():
#
#     form = AddProductForm()
#     category = db.session.execute(db.select(Category).filter_by(active=True)).scalars()
#     metals = db.session.execute(db.select(Metal).filter_by(active=True)).scalars()
#     colors = db.session.execute(db.select(Color).filter_by(active=True)).scalars()
#     styles = db.session.execute(db.select(Style).filter_by(active=True)).scalars()
#
#     form.category_id.choices = [(g.id, g.name) for g in category]
#     form.metal_id.choices = [(g.id, g.name) for g in metals]
#     form.color_id.choices = [(g.id, g.name) for g in colors]
#     form.style_id.choices = [(g.id, g.name) for g in styles]
#
#     if form.validate_on_submit():
#         name = form.name.data.title()
#         desc = form.desc.data
#         stock = form.stock.data
#         price = form.price.data
#         # date = datetime.now().strftime('%Y-%m-%d')
#         img = form.img.data
#         category = form.category_id.data
#         metal = form.metal_id.data
#         color = form.color_id.data
#         style = form.style_id.data
#
#         new_entry = Product(name=name,
#                             desc=desc,
#                             stock=stock,
#                             price=price,
#                             img=img,
#                             metal_id=metal,
#                             category_id=category,
#                             color_id=color,
#                             style_id=style,)
#         db.session.add(new_entry)
#         db.session.commit()
#
#         return redirect(url_for('product.add_product'))
#     return render_template("product/add_template.html", form=form)

def get_all_product():
    result = db.session.execute(db.select(Product).order_by(Product.active.desc())).scalars()
    return result
