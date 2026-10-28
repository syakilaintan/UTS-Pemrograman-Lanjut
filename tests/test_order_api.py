
def test_create_order(
    client,
    admin_headers,
    sample_product
):
    response = client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 2
                }
            ]
        }
    )

    assert response.status_code == 201
    assert response.json()["total_price"] == 10000


def test_order_reduces_stock(
    client,
    admin_headers,
    sample_product
):
    client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 3
                }
            ]
        }
    )

    response = client.get("/products/1")

    assert response.json()["stock"] == 17


def test_order_product_not_found(client):
    response = client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 999,
                    "quantity": 2
                }
            ]
        }
    )

    assert response.status_code == 400


def test_order_stock_not_enough(
    client,
    admin_headers,
    sample_product
):
    response = client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 100
                }
            ]
        }
    )

    assert response.status_code == 400


def test_order_quantity_invalid(client):
    response = client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 0
                }
            ]
        }
    )

    assert response.status_code == 422


def test_get_orders(
    client,
    admin_headers,
    sample_product
):
    client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 1
                }
            ]
        }
    )

    response = client.get(
        "/orders",
        headers=admin_headers
    )

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_order_detail(
    client,
    admin_headers,
    sample_product
):
    client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 1
                }
            ]
        }
    )

    response = client.get("/orders/1")

    assert response.status_code == 200
    assert response.json()["customer_id"] == "C001"


def test_update_order_status(
    client,
    admin_headers,
    sample_product
):
    client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 1
                }
            ]
        }
    )

    response = client.patch(
        "/orders/1/status",
        headers=admin_headers,
        json={
            "status": "processing"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "processing"


def test_invalid_order_status(
    client,
    admin_headers,
    sample_product
):
    client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 1
                }
            ]
        }
    )

    response = client.patch(
        "/orders/1/status",
        headers=admin_headers,
        json={
            "status": "random"
        }
    )

    assert response.status_code == 400


def test_cancel_order_returns_stock(
    client,
    admin_headers,
    sample_product
):
    client.post(
        "/orders",
        json={
            "customer_id": "C001",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 2
                }
            ]
        }
    )

    client.patch(
        "/orders/1/status",
        headers=admin_headers,
        json={
            "status": "cancelled"
        }
    )

    response = client.get("/products/1")

    assert response.json()["stock"] == 20
