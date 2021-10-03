import pytest
from src.main.app import create_app
from src.main.config.base import config_by_name
from collections import namedtuple


@pytest.fixture
def client():
    app = create_app()
    app.config.from_object(config_by_name['dev'])
    with app.test_client() as client:
        yield client


def adapt_request(current_dict):
    return namedtuple('Obj', current_dict.keys())(*current_dict.values())
