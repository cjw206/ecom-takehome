from pydantic import BaseModel

class Retailer(BaseModel):
    sku: str
    retailer_name: str