import os
import pytest
from src.main.config import config_by_name
from src.main.app import create_app
from collections import namedtuple


@pytest.fixture
def client():
    app = create_app()
    app.config.from_object(config_by_name["test"])
    with app.test_client() as client:
        yield client


def adapt_request(current_dict):
    return namedtuple("request", current_dict.keys())(*current_dict.values())
