
from app.interfaces.notification_interface import NotificationInterface


class ConsoleNotification(NotificationInterface):

    def send(self, message: str) -> None:
        print(f"[NOTIFICATION] {message}")
