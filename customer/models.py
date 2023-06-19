from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=32)
    lastname=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    phonenumber=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    address=models.CharField(max_length=32)


    def register(self):
        self.save
        def get_customer_by_email(email):
            try:
                return Customer.objects.get(email=email)
            except:
                return False
        def isExist(self):
                if Customer.objects.filter(email = self.email):
                    return True
                return False
   




    

#     name=models.CharField(max_length=32)
#     price=models.DecimalField(max_digits=8, decimal_places=2)
#     description=models.TextField()
#     image=models.ImageField()
#     date_created=models.DateTimeField(AUTO_NEW_ADD=True)
#     date_updated=models.DateTimeField(auto_new=True)
#     stock=models.PositiveIntegerField
    
