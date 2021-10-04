from flask import Flask
from src.main.factories.add_account_factory import make_add_account
from src.main.adapters.flask_route_adapter import adapt_route as adapt


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts", methods=["POST"], view_func=adapt(make_add_account()))
    return app
