from flask.app import Flask
import pytest
from src.main.routes.account_routes import set_account_routes
from src.main.app import create_app, db
from src.main.config.base import config_by_name
from collections import namedtuple


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config.from_object(config_by_name["test"])
    app = set_account_routes(app)
    db.init_app(app)
    with app.test_client() as client:
        yield client


def adapt_request(current_dict):
    return namedtuple("request", current_dict.keys())(*current_dict.values())
