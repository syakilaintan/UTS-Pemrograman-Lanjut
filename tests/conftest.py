
import pytest

from app.main import app

from app.core.dependencies import (
    product_repository,
    order_repository
)

from fastapi.testclient import TestClient


@pytest.fixture
def client():

    product_repository.products.clear()
    product_repository.next_id = 1

    order_repository.orders.clear()
    order_repository.next_id = 1

    return TestClient(app)


@pytest.fixture
def admin_headers():

    return {
        "X-API-Key": "admin123"
    }


@pytest.fixture
def sample_product(client, admin_headers):

    response = client.post(
        "/products",
        headers=admin_headers,
        json={
            "name": "Buku Tulis",
            "price": 5000,
            "stock": 20
        }
    )

    return response.json()
