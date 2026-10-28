
from app.models.product import Product
from app.interfaces.product_repository_interface import (
    ProductRepositoryInterface
)


class ProductRepository(ProductRepositoryInterface):

    def __init__(self):
        self.products = {}
        self.next_id = 1

    def get_all(self) -> list[Product]:
        return list(self.products.values())

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)

    def save(self, product: Product) -> Product:
        product.id = self.next_id
        self.products[self.next_id] = product
        self.next_id += 1
        return product

    def update(self, product: Product) -> Product:
        self.products[product.id] = product
        return product

    def delete(self, product_id: int) -> bool:
        if product_id not in self.products:
            return False

        del self.products[product_id]
        return True
