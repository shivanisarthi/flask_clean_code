from tests.test_main import client


def test_200(client):
    request_body = dict(username='John Doe')
    response = client.get('/', json=request_body)
    expected_response = response.json
    print(expected_response)
    assert response.status_code == 200
    assert expected_response == dict(id=10, username='John Doe')


def test_400_on_invalid_name(client):
    request_body = dict()
    response = client.get('/', json=request_body)
    assert response.status_code == 400
