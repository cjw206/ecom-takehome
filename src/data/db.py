from models.product import PriceUpdate

# At this stage I would persist the price update to a
# relational db with a timestamp for history purposes.
def save_updated_price(price_update: PriceUpdate) -> None:
    return None

def get_price_from_db(sku: str) -> PriceUpdate:
    update = PriceUpdate()
    return update
