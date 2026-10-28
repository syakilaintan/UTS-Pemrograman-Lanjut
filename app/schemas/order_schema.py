
from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    customer_id: str = Field(min_length=1)
    items: list[OrderItemCreate] = Field(min_length=1)


class OrderStatusUpdate(BaseModel):
    status: str


class OrderItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: int
    subtotal: int


class OrderResponse(BaseModel):
    id: int
    customer_id: str
    items: list[OrderItemResponse]
    total_price: int
    status: str
