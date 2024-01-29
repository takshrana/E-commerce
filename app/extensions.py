from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()
