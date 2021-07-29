from django.contrib import admin
from . models import Cart

# Register your models here.

class CartModel(admin.ModelAdmin):
    list_display = ('id', 'user','item')


admin.site.register(Cart, CartModel)
