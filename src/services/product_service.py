from models.product import PriceUpdate
from data.cache import get_cache_by_retailer, update_cache
import data.db as db

def receive(price_update: PriceUpdate) -> None:
    # persist to db
    save_updated_price(price_update)
    # compare with price in cache
    is_better_price = compare_cached_price(price_update)
    # if price is better update record in cache
    if is_better_price:
        updated_price = db.get_price_from_db(price_update.sku)
        update_cache(updated_price)

def compare_cached_price(price_update: PriceUpdate) -> bool:
    # get cache by retailer
    cache = get_cache_by_retailer(price_update.retailer)
    if cache is None:
        return False
    # get price from cache using the sku as key
    product_price = cache[price_update.sku]
    if product_price is None:
        return True
    
    if price_update.price < product_price.price: 
        return True
    else:
        return False
    
def save_updated_price(price_update: PriceUpdate) -> None:
    db.save_updated_price(price_update)