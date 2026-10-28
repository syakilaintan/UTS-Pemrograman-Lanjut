
from app.models.order import Order
from app.interfaces.order_repository_interface import (
    OrderRepositoryInterface
)


class OrderRepository(OrderRepositoryInterface):

    def __init__(self):
        self.orders = {}
        self.next_id = 1

    def get_all(self) -> list[Order]:
        return list(self.orders.values())

    def get_by_id(self, order_id: int) -> Order | None:
        return self.orders.get(order_id)

    def save(self, order: Order) -> Order:
        order.id = self.next_id
        self.orders[self.next_id] = order
        self.next_id += 1
        return order

    def update(self, order: Order) -> Order:
        self.orders[order.id] = order
        return order
