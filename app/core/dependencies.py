
from app.repositories.product_repository import ProductRepository
from app.repositories.order_repository import OrderRepository
from app.notifications.console_notification import ConsoleNotification

from app.services.product_service import ProductService
from app.services.order_service import OrderService


# Repository
product_repository = ProductRepository()
order_repository = OrderRepository()

# Notification
notification = ConsoleNotification()


# Service
product_service = ProductService(
    repository=product_repository
)

order_service = OrderService(
    product_repository=product_repository,
    order_repository=order_repository,
    notification=notification
)
