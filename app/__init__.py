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

    from app.product.add import bp as add_bp
    app.register_blueprint(add_bp)

    from app.product.update import bp as upd_bp
    app.register_blueprint(upd_bp)

    @app.route('/test')
    def test_page():
        return '<h1>Test</h1>'

    with app.app_context():
        db.create_all()
        
    return app
