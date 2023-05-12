from ninja import Schema, ModelSchema
from .models import Product, Offer


class ProductInSchema(Schema):
    name : str
    description : str

class ProductOutSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ['id', 'name', 'description']

class OfferSchema(ModelSchema):
    class Config:
        model = Offer
        model_fields = ['id', 'price', 'items_in_stock', 'product']
