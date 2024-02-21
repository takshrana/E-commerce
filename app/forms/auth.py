from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(Email)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(Email)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")