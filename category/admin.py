from django.contrib import admin

# Register your models here.
from .models import Customer

class CategoryAdmin(admin.ModelAdmin):
    list_display =("productName","productSize")

admin.site.register(Customer,CategoryAdmin) 
