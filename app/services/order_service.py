
from app.models.order import Order, OrderItem
from app.schemas.order_schema import OrderCreate
from app.interfaces.product_repository_interface import (
    ProductRepositoryInterface
)
from app.interfaces.order_repository_interface import (
    OrderRepositoryInterface
)
from app.interfaces.notification_interface import NotificationInterface


class OrderService:

    def __init__(
        self,
        product_repository: ProductRepositoryInterface,
        order_repository: OrderRepositoryInterface,
        notification: NotificationInterface
    ):
        self.product_repository = product_repository
        self.order_repository = order_repository
        self.notification = notification

    def create_order(self, data: OrderCreate):

        order_items = []
        total_price = 0
        requested_stock = {}

        # Menggabungkan jumlah jika produk yang sama
        # muncul lebih dari sekali dalam pesanan.
        for item in data.items:
            requested_stock[item.product_id] = (
                requested_stock.get(item.product_id, 0)
                + item.quantity
            )

        # Validasi seluruh produk dan stok terlebih dahulu.
        for product_id, quantity in requested_stock.items():

            product = self.product_repository.get_by_id(product_id)

            if product is None:
                raise ValueError(
                    f"Produk dengan ID {product_id} tidak ditemukan"
                )

            if product.stock < quantity:
                raise ValueError(
                    f"Stok produk {product.name} tidak mencukupi"
                )

        # Membuat detail pesanan.
        for product_id, quantity in requested_stock.items():

            product = self.product_repository.get_by_id(product_id)

            subtotal = product.price * quantity

            order_item = OrderItem(
                product_id=product.id,
                product_name=product.name,
                quantity=quantity,
                price=product.price,
                subtotal=subtotal
            )

            order_items.append(order_item)
            total_price += subtotal

        order = Order(
            id=0,
            customer_id=data.customer_id,
            items=order_items,
            total_price=total_price,
            status="pending"
        )

        # Simpan pesanan terlebih dahulu.
        saved_order = self.order_repository.save(order)

        # Kurangi stok produk.
        for product_id, quantity in requested_stock.items():

            product = self.product_repository.get_by_id(product_id)

            product.stock -= quantity

            self.product_repository.update(product)

        self.notification.send(
            f"Pesanan {saved_order.id} berhasil dibuat"
        )

        return saved_order

    def get_all_orders(self):
        return self.order_repository.get_all()

    def get_order(self, order_id: int):
        order = self.order_repository.get_by_id(order_id)

        if order is None:
            raise ValueError("Pesanan tidak ditemukan")

        return order

    def update_status(self, order_id: int, status: str):

        order = self.order_repository.get_by_id(order_id)

        if order is None:
            raise ValueError("Pesanan tidak ditemukan")

        allowed_status = [
            "pending",
            "processing",
            "completed",
            "cancelled"
        ]

        if status not in allowed_status:
            raise ValueError("Status pesanan tidak valid")

        if order.status == "completed":
            raise ValueError(
                "Pesanan yang sudah selesai tidak dapat diubah"
            )

        if order.status == "cancelled":
            raise ValueError(
                "Pesanan yang sudah dibatalkan tidak dapat diubah"
            )

        # Stok dikembalikan hanya jika pembatalan pertama.
        if status == "cancelled":

            for item in order.items:

                product = self.product_repository.get_by_id(
                    item.product_id
                )

                if product is not None:
                    product.stock += item.quantity
                    self.product_repository.update(product)

        order.status = status

        updated_order = self.order_repository.update(order)

        self.notification.send(
            f"Status pesanan {order.id} menjadi {status}"
        )

        return updated_order
