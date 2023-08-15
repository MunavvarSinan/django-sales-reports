from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
import random
import string
from .utils import generate_code

# Create your models here.

# product * quantity = total price
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    # save method is called when a model is created or updated before it is saved to the database
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)
    # this is used to calculate the price of a product based the quantity user have selected  
    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"
    
class Sales(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position) # one sale can have many positions
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Sales for the amount of ${self.total_price}"

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
    
    def get_positions(self):
        return self.positions.all()
    
class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"File name: {self.file_name}"
 