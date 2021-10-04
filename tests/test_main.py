import pytest
from src.main.app import create_app, db
from collections import namedtuple


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def adapt_request(current_dict):
    return namedtuple("Obj", current_dict.keys())(*current_dict.values())
