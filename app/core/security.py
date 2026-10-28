
import os

from fastapi import Header, HTTPException, status


ADMIN_API_KEY = os.getenv(
    "ADMIN_API_KEY",
    "admin123"
)


def verify_admin_api_key(
    x_api_key: str | None = Header(default=None)
):

    if x_api_key != ADMIN_API_KEY:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key tidak valid"
        )

    return x_api_key
