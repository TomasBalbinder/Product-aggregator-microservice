from ninja import Schema, ModelSchema
from .models import Product



class AccessTokenSchema(Schema):
    access_token: str
    token_type: str

class ProductInSchema(Schema):
    name : str
    description : str

class ProductOutSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ['id', 'name', 'description']