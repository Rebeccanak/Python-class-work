from django.db import models

# Create your models here.

class Category(models.Model):
    productName=models.CharField(max_length=32)
    productSize=models.CharField(max_length=900)
    # productDescription=models.EmailField(max_length=32)
   