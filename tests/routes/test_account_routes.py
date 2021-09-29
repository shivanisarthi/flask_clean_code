from tests.test_main import client


def test_200(client):
    request_body = dict(id='1', name='John Doe')
    response = client.get('/', json=request_body)
    data = response.json
    assert response.status_code == 200
    assert data == request_body


def test_404_on_invalid_name(client):
    request_body = dict(id='1')
    response = client.get('/', json=request_body)
    data = response.json
    assert response.status_code == 404
    assert data == dict(message='Missing name')


def test_404_on_invalid_id(client):
    request_body = dict(name='John Doe')
    response = client.get('/', json=request_body)
    data = response.json
    assert response.status_code == 404
    assert data == dict(message='Missing id')
