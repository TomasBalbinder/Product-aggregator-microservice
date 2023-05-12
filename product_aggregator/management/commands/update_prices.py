import time
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from product_aggregator.authentication import get_access_token
from product_aggregator.models import Product, Offer

class Command(BaseCommand):
    def handle(self, *args, **options):       
        access_token = get_access_token()
        while True:       
            self.update_product_prices(access_token)       
            time.sleep(60)
    def update_product_prices(self, access_token):    
        products = Product.objects.all()
        for product in products:          
            url = f"https://python.exercise.applifting.cz/api/v1/products/{product.id}/offers"
            headers = {
                "accept": "application/json",
                "Bearer": access_token,
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:            
                offer_data = response.json()
                for data in offer_data:
                    defaults = {
                    'price': data['price'],
                    'items_in_stock': data['items_in_stock'],
                    'product_id': product.id,
                    }
                    offer, created = Offer.objects.update_or_create(id=data['id'], defaults=defaults)
                    if created:
                        print('A new offer has been created.')
                    else:
                        print('The offer with ID {} has been updated.'.format(data['id']))

           

