from django.shortcuts import get_object_or_404
from ninja import Router
from .models import Product, Offer
from .schemas import ProductInSchema, ProductOutSchema, OfferSchema
from typing import List
from uuid import UUID

router = Router()

@router.post('/', response=ProductOutSchema)
def create_product(request, product : ProductInSchema):
    created_product = Product.objects.create(**product.dict())
    return created_product

@router.get('/', response=List[ProductOutSchema])
def list_products(request):
    products = Product.objects.all()
    return products

@router.get("/{product_id}", response=ProductOutSchema)
def get_product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product

@router.put("/{product_id}", response=ProductOutSchema)
def update_product(request, product_id: str, product: ProductInSchema):
    updated_product = get_object_or_404(Product, id=product_id)
    updated_product.name = product.name
    updated_product.description = product.description
    updated_product.save()
    return updated_product

@router.delete("/{product_id}")
def delete_product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}


@router.get("offers/", response=List[OfferSchema])
def list_offers(request):
    offers = Offer.objects.all()
    return offers

@router.get("offers/{offer_id}", response=OfferSchema)
def get_offer(request, offer_id:UUID ):
    offer = get_object_or_404(Offer, id=offer_id)
    return offer

