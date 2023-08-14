from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='customers', default='no_picture.png') # this will create a folder called customers in the media folder and over there we will store the logo of the customer
    # and the default means the default picture if the user does not upload any picture
    
    def __str__(self):  
        return str(self.name) # str is used to convert the hexadecimal value to string value