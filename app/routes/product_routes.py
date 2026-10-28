
from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.core.security import verify_admin_api_key
from app.core.dependencies import product_service


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get(
    "",
    response_model=list[ProductResponse]
)
def get_products():

    return product_service.get_all_products()


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(product_id: int):

    try:
        return product_service.get_product(product_id)

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_admin_api_key)]
)
def create_product(data: ProductCreate):

    return product_service.create_product(data)


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    dependencies=[Depends(verify_admin_api_key)]
)
def update_product(
    product_id: int,
    data: ProductUpdate
):

    try:
        return product_service.update_product(
            product_id,
            data
        )

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(verify_admin_api_key)]
)
def delete_product(product_id: int):

    try:
        product_service.delete_product(product_id)

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
