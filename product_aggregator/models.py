from django.db import models
from uuid import uuid4

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    price = models.IntegerField()
    items_in_stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')





