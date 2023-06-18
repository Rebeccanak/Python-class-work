from django.db import models

# Create your models here.
class Products(models.Model):

    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    description=models.TextField()
    image=models.ImageField()
    date_created=models.DateTimeField(AUTO_NEW_ADD=True)
    date_updated=models.DateTimeField(auto_new=True)
    stock=models.PositiveIntegerField
    
