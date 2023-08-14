from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products', default='no_picture.png') # this will create a folder called products in the media folder and over there we will store the image of the product
    price = models.FloatField(help_text='Price of the product in USD')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.created.strftime('%d-%m-%Y')}" # this will return the name of the product and the date on which it was created and displayed in the admin panel product section