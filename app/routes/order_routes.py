
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.order_schema import (
    OrderCreate,
    OrderResponse,
    OrderStatusUpdate
)

from app.core.security import verify_admin_api_key
from app.core.dependencies import order_service


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=201
)
def create_order(data: OrderCreate):

    try:
        return order_service.create_order(data)

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get(
    "",
    response_model=list[OrderResponse],
    dependencies=[Depends(verify_admin_api_key)]
)
def get_orders():

    return order_service.get_all_orders()


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(order_id: int):

    try:
        return order_service.get_order(order_id)

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.patch(
    "/{order_id}/status",
    response_model=OrderResponse,
    dependencies=[Depends(verify_admin_api_key)]
)
def update_order_status(
    order_id: int,
    data: OrderStatusUpdate
):

    try:
        return order_service.update_status(
            order_id,
            data.status
        )

    except ValueError as error:

        message = str(error)

        if message == "Pesanan tidak ditemukan":
            status_code = 404
        else:
            status_code = 400

        raise HTTPException(
            status_code=status_code,
            detail=message
        )
