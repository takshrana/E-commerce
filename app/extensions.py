from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()


# def db_init(app):
#     db.init_app(app)
#
#
# def login_init(app):
#     login_manager.init_app(app)
#
#
# def bs_init(app):
#     bootstrap.init_app(app)