
def test_admin_access_with_valid_key(
    client,
    admin_headers
):
    response = client.get(
        "/orders",
        headers=admin_headers
    )

    assert response.status_code == 200


def test_admin_access_without_key(client):
    response = client.get("/orders")

    assert response.status_code == 401


def test_admin_access_with_wrong_key(client):
    response = client.get(
        "/orders",
        headers={
            "X-API-Key": "wrong-key"
        }
    )

    assert response.status_code == 401
