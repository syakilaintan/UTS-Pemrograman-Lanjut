
from abc import ABC, abstractmethod
from app.models.order import Order


class OrderRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> list[Order]:
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Order | None:
        pass

    @abstractmethod
    def save(self, order: Order) -> Order:
        pass

    @abstractmethod
    def update(self, order: Order) -> Order:
        pass
