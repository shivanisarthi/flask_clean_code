from flask import Flask
from src.main.factories.add_account_factory import makeAddAccount
from src.main.adapters.flask_route_adapter import adaptRoute


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule('/', view_func=adaptRoute(makeAddAccount()))
    return app
