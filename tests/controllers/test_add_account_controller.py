from tests.test_main import client, adapt_request as adapt
from src.application.controllers import AddAccountController, Account
from mock import Mock, AsyncMock


def repoMock():
    add_mock = AsyncMock(return_value=Account(id="1", name='John Doe'))
    repo = Mock()
    repo.add = add_mock
    return repo


async def test_missing_id(client):
    current_controller = AddAccountController(repoMock())
    request = adapt(dict(name='JohnDoe'))
    response = await current_controller.handle(request)
    expected_response = 400
    assert response.status == expected_response


async def test_missing_name(client):
    current_controller = AddAccountController(repoMock())
    request = adapt(dict(id='10'))
    response = await current_controller.handle(request)
    expected_response = 400
    assert response.status == expected_response


async def test_account_on_success(client):
    current_controller = AddAccountController(repoMock())
    request = adapt(dict(id='10', name='JohnDoe'))
    response = await current_controller.handle(request)
    expected_response = Account(id='1', name='John Doe')
    assert response.status == 200
    assert response.body == expected_response
