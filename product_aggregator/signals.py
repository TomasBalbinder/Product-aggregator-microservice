from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .authentication import get_access_token
from .models import Product

@receiver(post_save, sender=Product)  
def registration_product(sender, instance, created, **kwargs):
    product = instance 
    if created:
        product = instance
        url = "https://python.exercise.applifting.cz/api/v1/products/register"
        headers = {
            "accept": "application/json",
            "Bearer": get_access_token(),
        }
        body = {
            "id": str(product.id),
            "name": product.name,
            "description": product.description,
        }
        response = requests.post(url, headers=headers, json=body)
        json_data = response.json()       
        if response.status_code == 201:
            return json_data['id']
        else:
            return json_data['detail']
        
        
