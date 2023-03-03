**Third Party Libraries**

fastapi for endpoints
uvicorn as the web server

**Tooling**

python version 3.11
pipenv for mananging packages and virtualenv

**Assumptions**

Based on the interfaces provided I assumed the unique idetifier for a retailer
would be the retailer name, as it appears sku would be the identifier for specific product.

Based on the wording in the prompt I assumed implementing the search endpoint was out of
scope for now.

**Strategy**
Knowing that the search endpoint needs to return a response in < 20ms I decided that
the best strategy would be to persist the data to a database to use as a source of truth and for historic purposes,
all the while keeping the best prices in cached. This way when the search endpoint is implemented the prices can be
fetched without querying a db.

**Run Locally**

Doesn't do much but assuming pipenv and virtualenv are in your PATH variable
then in the src directory run `pipenv run uvicorn app:api_router --reload`