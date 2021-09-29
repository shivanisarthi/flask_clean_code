import pytest
from src.main.app import create_app
from src.main.config.base import config_by_name


@pytest.fixture
def client():
    app = create_app()
    app.config.from_object(config_by_name['dev'])
    with app.test_client() as client:
        yield client
