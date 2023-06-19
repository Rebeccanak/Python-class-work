from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display =("firstname","lastname","email","phonenumber","password","address")

admin.site.register(Customer,CustomerAdmin) 
