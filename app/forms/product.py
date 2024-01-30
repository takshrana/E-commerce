from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


class ShowProduct(FlaskForm):
    options = SelectField("Products", coerce=str)


class AddProductForm(FlaskForm):

    category_id = SelectField("Category", coerce=int, validators=[DataRequired()])
    name = StringField("Product Name", validators=[DataRequired()])
    desc = StringField("Product Description", validators=[])
    stock = IntegerField("Stock", validators=[DataRequired()])
    price = IntegerField("Product Price", validators=[DataRequired()])
    img_url = StringField("Image URL")
    submit = SubmitField("Add Product")


class ShowCategory(FlaskForm):
    options = SelectField("Categories", coerce=str)


class AddCategoryForm(FlaskForm):

    name = StringField("Category Name", validators=[DataRequired()])
    submit = SubmitField("Add Category")


class ShowMetal(FlaskForm):
    options = SelectField("Metals", coerce=str)


class AddMetalForm(FlaskForm):

    name = StringField("Metal Name", validators=[DataRequired()])
    submit = SubmitField("Add Metal")


class ShowStone(FlaskForm):
    options = SelectField("Stones", coerce=str)


class AddStoneForm(FlaskForm):
    name = StringField("Stone Name", validators=[DataRequired()])
    submit = SubmitField("Add Stone")

