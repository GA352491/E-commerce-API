from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.user.username + 'cart'


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username + 'cartItem'


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = product.price * int(cart_items.quantity)
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart_items.price + cart.total_price
    cart.save()
    print("Request finished!")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_signature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username + self.order_id


class OrderedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + self.order.order_id + 'paid'
