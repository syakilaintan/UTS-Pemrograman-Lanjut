
from dataclasses import dataclass


@dataclass
class OrderItem:
    product_id: int
    product_name: str
    quantity: int
    price: int
    subtotal: int


@dataclass
class Order:
    id: int
    customer_id: str
    items: list[OrderItem]
    total_price: int
    status: str
