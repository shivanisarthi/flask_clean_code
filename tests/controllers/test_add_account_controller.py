from tests.test_main import client
from tests.test_main import adapt_request as adapt
from src.application.controllers import AddAccountController, Account
from mock import Mock, AsyncMock
from faker import Faker

faker = Faker()


def repo_mock():
    add_mock = AsyncMock(return_value=Account(id=10, username='John Doe'))
    repo = Mock()
    repo.add = add_mock
    return repo


def validator_mock(return_value):
    validator_mock = Mock()
    validator_mock.validate = Mock(return_value=return_value)
    return validator_mock


async def test_missing_name(client):
    current_controller = AddAccountController(repo_mock(), validator_mock(Exception))
    request = adapt(dict())
    response = await current_controller.handle(request)
    expected_response = 400
    assert response.status == expected_response


async def test_account_on_success(client):
    current_controller = AddAccountController(repo_mock(), validator_mock(None))
    request = adapt(dict(username='John Doe'))
    response = await current_controller.handle(request)
    print(request.username)
    expected_response = Account(id=10, username=request.username)
    assert response.status == 200
    assert response.body == expected_response
