
from fastapi import FastAPI

from app.routes.product_routes import router as product_router
from app.routes.order_routes import router as order_router

from app.core.exception_handler import register_exception_handlers


app = FastAPI(
    title="Sistem Pemesanan Produk",
    description="REST API untuk mengelola produk dan pesanan",
    version="1.0.0"
)


# Error handling
register_exception_handlers(app)


# Router
app.include_router(product_router)
app.include_router(order_router)


@app.get("/")
def home():

    return {
        "message": "Sistem Pemesanan Produk",
        "docs": "/docs"
    }
