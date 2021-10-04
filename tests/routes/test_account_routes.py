from tests.test_main import client


# def test_200(client):
#     request_body = dict(username="John Doe")
#     response = client.post("/", json=request_body)
#     print(response.json)
#     assert response.status_code == 200


def test_400_on_invalid_name(client):
    request_body = dict()
    response = client.post("/accounts", json=request_body)
    assert response.status_code == 400
