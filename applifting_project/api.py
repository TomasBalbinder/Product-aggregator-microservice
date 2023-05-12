from ninja import NinjaAPI
from product_aggregator.api import router as product_router

api = NinjaAPI()
api.add_router('/products/', product_router)
