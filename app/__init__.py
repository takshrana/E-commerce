from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    app.add_url_rule('/', endpoint='index')

    @app.route('/test')
    def test_page():
        return '<h1>Test</h1>'

    return app
