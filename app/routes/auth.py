from flask import render_template, flash, redirect, url_for
from app.auth import bp
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db, login_manager
from app.models.auth import User
from app.forms.auth import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if db.session.execute(db.select(User).filter_by(email=form.email.data)).scalar():
            flash("Email already registered.")
        else:
            salt_pass = generate_password_hash(password=form.password.data, method='pbkdf2:sha256', salt_length=8)

            new_user = form.email.data
            user = User(email=new_user,password=salt_pass)

            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home.index'))

    return render_template("auth/register.html", form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(email=form.email.data)).scalar()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home.index'))
            else:
                flash("Wrong password. Try Again.")
        else:
            flash("Email does not exist, pls register.")
    return render_template("auth/login.html", form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))
