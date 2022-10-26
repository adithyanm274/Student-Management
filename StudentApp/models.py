from django.db import models

# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True)