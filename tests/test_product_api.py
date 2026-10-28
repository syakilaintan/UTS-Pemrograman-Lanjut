
def test_get_products(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == []


def test_create_product(client, admin_headers):
    response = client.post(
        "/products",
        headers=admin_headers,
        json={
            "name": "Buku Tulis",
            "price": 5000,
            "stock": 20
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Buku Tulis"


def test_create_product_without_api_key(client):
    response = client.post(
        "/products",
        json={
            "name": "Buku",
            "price": 5000,
            "stock": 10
        }
    )

    assert response.status_code == 401


def test_create_product_invalid_price(client, admin_headers):
    response = client.post(
        "/products",
        headers=admin_headers,
        json={
            "name": "Buku",
            "price": -5000,
            "stock": 10
        }
    )

    assert response.status_code == 422


def test_create_product_invalid_stock(client, admin_headers):
    response = client.post(
        "/products",
        headers=admin_headers,
        json={
            "name": "Buku",
            "price": 5000,
            "stock": -1
        }
    )

    assert response.status_code == 422


def test_create_product_empty_name(client, admin_headers):
    response = client.post(
        "/products",
        headers=admin_headers,
        json={
            "name": "",
            "price": 5000,
            "stock": 10
        }
    )

    assert response.status_code == 422


def test_get_product_detail(
    client,
    admin_headers,
    sample_product
):
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Buku Tulis"


def test_get_product_not_found(client):
    response = client.get("/products/999")

    assert response.status_code == 404


def test_update_product(
    client,
    admin_headers,
    sample_product
):
    response = client.put(
        "/products/1",
        headers=admin_headers,
        json={
            "name": "Buku Baru",
            "price": 7000,
            "stock": 15
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Buku Baru"


def test_delete_product(
    client,
    admin_headers,
    sample_product
):
    response = client.delete(
        "/products/1",
        headers=admin_headers
    )

    assert response.status_code == 204


def test_delete_product_not_found(client, admin_headers):
    response = client.delete(
        "/products/999",
        headers=admin_headers
    )

    assert response.status_code == 404
