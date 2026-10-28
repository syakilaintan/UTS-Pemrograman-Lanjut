
from abc import ABC, abstractmethod


class NotificationInterface(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass
