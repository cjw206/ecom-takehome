from models.product import PriceUpdate

cache = dict

# My strategy would be to keep the best price in a cache
# There would likely be a cache per retailer
def get_cache_by_retailer(retailer_name: str) -> dict:
    return cache[retailer_name] 

# A stubbed method for updating values in a cache
def update_cache(price_update: PriceUpdate) -> None:
    return None