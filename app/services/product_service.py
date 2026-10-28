
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.interfaces.product_repository_interface import (
    ProductRepositoryInterface
)


class ProductService:

    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def get_all_products(self):
        return self.repository.get_all()

    def get_product(self, product_id: int):
        product = self.repository.get_by_id(product_id)

        if product is None:
            raise ValueError("Produk tidak ditemukan")

        return product

    def create_product(self, data: ProductCreate):
        product = Product(
            id=0,
            name=data.name,
            price=data.price,
            stock=data.stock
        )

        return self.repository.save(product)

    def update_product(self, product_id: int, data: ProductUpdate):
        product = self.repository.get_by_id(product_id)

        if product is None:
            raise ValueError("Produk tidak ditemukan")

        product.name = data.name
        product.price = data.price
        product.stock = data.stock

        return self.repository.update(product)

    def delete_product(self, product_id: int):
        deleted = self.repository.delete(product_id)

        if not deleted:
            raise ValueError("Produk tidak ditemukan")

        return True
