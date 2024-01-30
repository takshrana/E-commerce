from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


# class ShowProduct(FlaskForm):
#     options = SelectField("Products", coerce=str)


class AddProductForm(FlaskForm):

    # category_id = SelectField("Category", coerce=int, validators=[DataRequired()])
    # metal_id = SelectField("Metal", coerce=int, validators=[DataRequired()])
    # color_id = SelectField("Color", coerce=int, validators=[DataRequired()])
    # style_id = SelectField("Style", coerce=int, validators=[DataRequired()])
    options = SelectField("Products", coerce=str)
    name = StringField("Product Name", validators=[DataRequired()])
    stock = IntegerField("Stock")
    price = IntegerField("Product Price", validators=[DataRequired()])
    img_url = StringField("Image URL")
    submit = SubmitField("Add Product")


# class ShowCategory(FlaskForm):
#     options = SelectField("Categories", coerce=str)


class AddCategoryForm(FlaskForm):
    options = SelectField("Categories", coerce=str)
    name = StringField("Category Name", validators=[DataRequired()])
    submit = SubmitField("Add Category")


# class ShowMetal(FlaskForm):
#     options = SelectField("Metals", coerce=str)


class AddMetalForm(FlaskForm):
    options = SelectField("Metals", coerce=str)
    name = StringField("Metal Name", validators=[DataRequired()])
    submit = SubmitField("Add Metal")


# class ShowStone(FlaskForm):
#     options = SelectField("Stones", coerce=str)


class AddStyleForm(FlaskForm):
    options = SelectField("Styles", coerce=str)
    name = StringField("Style Name", validators=[DataRequired()])
    submit = SubmitField("Add Style")


class AddColorForm(FlaskForm):
    options = SelectField("Colors", coerce=str)
    name = StringField("Color Name", validators=[DataRequired()])
    submit = SubmitField("Add Color")


# class ShowSubcategory(FlaskForm):
#     options = SelectField("Subcategories", coerce=str)
#
#
# class AddSubcategoryForm(FlaskForm):
#
#     options = SelectField("Subcategories", coerce=str)
#     name = StringField("Subcategory Name", validators=[DataRequired()])
#     submit = SubmitField("Add Product")
