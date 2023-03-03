from models.retailer import Retailer

def get_retailer(sku: str) -> Retailer:
    retailer = Retailer()
    retailer.sku = "123abc"
    retailer.retailer_name = "mom and pop shop"
