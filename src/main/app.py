from flask import Flask

from src.main.routes.account_routes import set_account_routes


def create_app() -> Flask:
    app = Flask(__name__)
    app = set_account_routes(app)
    return app
