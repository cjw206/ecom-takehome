from pydantic import BaseModel
from decimal import Decimal


class PriceUpdate(BaseModel):
    retailer: str
    sku: str
    price: Decimal
    url: str | None

class ProductPrice(BaseModel):
    sku: str
    price: Decimal
    retailer: str
    url: str | None
