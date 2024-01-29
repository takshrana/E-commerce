from flask import Flask

from config import Config
from app.extensions import login_manager, db, bootstrap


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.product import bp as prod_bp
    app.register_blueprint(prod_bp)

    @app.route('/test')
    def test_page():
        return '<h1>Test</h1>'

    return app
