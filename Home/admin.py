from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','type_of_product','price','location','grade','seasonality','image']


# @admin.register(Graph)
# class GraphAdmin(admin.ModelAdmin):
#     list_display = ['id','date','price']