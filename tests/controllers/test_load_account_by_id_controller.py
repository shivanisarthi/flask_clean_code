from tests.test_main import client
from tests.test_main import adapt_request as adapt
from src.application.controllers import LoadAccountByIdController, Account
from mock import Mock, AsyncMock
from faker import Faker

faker = Faker()


def repo_mock(account=None):
    load_by_id = AsyncMock(return_value=account)
    repo = Mock()
    repo.load_by_id = load_by_id
    return repo


async def test_load_account_on_success(client):
    account = Account(id=10, username="John Doe")
    current_controller = LoadAccountByIdController(repo_mock(account))
    request = adapt(dict(id=10))
    response = await current_controller.handle(request)
    expected_response = Account(id=10, username="John Doe")
    assert response.status == 200
    assert response.body == expected_response


async def test_return_none(client):
    current_controller = LoadAccountByIdController(repo_mock(None))
    request = adapt(dict(id=10))
    response = await current_controller.handle(request)
    expected_response = ""
    assert response.status == 204
    assert response.body == expected_response
