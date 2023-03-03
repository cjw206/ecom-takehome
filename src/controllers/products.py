from typing import Any

from fastapi import APIRouter

from models.product import PriceUpdate, ProductPrice
from services.product_service import receive
router = APIRouter()


@router.post("/receive")
async def receive_price_update(price_update: PriceUpdate) -> Any:
    receive(price_update)
    return price_update

@router.get("/search")
async def find_product_price(sku: str) -> ProductPrice:
    return None