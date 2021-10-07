from flask import Flask
from src.main.factories import make_add_account, make_load_account_by_id
from src.main.adapters import make_adapter

adapt = make_adapter()


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts", methods=["POST"], view_func=adapt.as_view("create_acc", make_add_account()))
    app.add_url_rule("/accounts/<id>", methods=["GET"], view_func=adapt.as_view("acc_by_id", make_load_account_by_id()))
    return app
