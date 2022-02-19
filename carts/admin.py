from django.contrib import admin
from carts.models import Cart, CartItems, OrderedItems, Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
admin.site.register(OrderedItems)
