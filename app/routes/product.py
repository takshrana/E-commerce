from flask import render_template, url_for, redirect
from app.product import bp
from datetime import datetime
from app.extensions import db
from app.models.product import Product, Category, Stone, Metal, Price
from app.forms.product import AddCategoryForm, AddProductForm, ShowProduct, ShowCategory, ShowMetal, AddMetalForm, ShowStone, AddStoneForm


@bp.route('/', methods=['GET', 'POST'])
def add_product():
    products = db.session.execute(db.select(Product)).scalars()
    display = ShowProduct()
    display.options.choices = [g.name for g in products]

    form = AddProductForm()
    category = db.session.execute(db.select(Category)).scalars()
    form.category_id.choices = [(g.id, g.name) for g in category]

    if form.validate_on_submit():
        name = form.name.data.capitalize()
        desc = form.desc.data
        stock = form.stock.data
        price = form.stock.data
        date = datetime.now().strftime('%Y-%m-%d')
        img_url = form.img_url.data
        category = form.category_id.data

        new_entry = Product(name=name, desc=desc, stock=stock, price=price, img_url=img_url, category_id=category)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('product.add_product'))
    return render_template("product/add_template.html", form=form, display=display)


@bp.route('/category', methods=['GET', 'POST'])
def add_category():
    category = db.session.execute(db.select(Category)).scalars()
    display = ShowCategory()
    display.options.choices = [g.name for g in category]

    form = AddCategoryForm()
    if form.validate_on_submit():
        name = form.name.data.capitalize()
        new_entry = Category(name=name)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('product.add_product'))

    return render_template("product/add_template.html", form=form, display=display)@bp.route('/category', methods=['GET', 'POST'])


@bp.route('/metal', methods=['GET', 'POST'])
def add_metal():
    choices = db.session.execute(db.select(Metal)).scalars()
    display = ShowMetal()
    display.options.choices = [g.name for g in choices]

    form = AddMetalForm()
    if form.validate_on_submit():
        name = form.name.data.capitalize()
        new_entry = Metal(name=name)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('product.add_product'))

    return render_template("product/add_template.html", form=form, display=display)


@bp.route('/stone', methods=['GET', 'POST'])
def add_stone():
    choices = db.session.execute(db.select(Stone)).scalars()
    display = ShowStone()
    display.options.choices = [g.name for g in choices]

    form = AddStoneForm()
    if form.validate_on_submit():
        name = form.name.data.capitalize()
        new_entry = Stone(name=name)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('product.add_product'))

    return render_template("product/add_template.html", form=form, display=display)