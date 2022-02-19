from rest_framework import serializers
from carts.models import Cart, CartItems, Order, OrderedItems
from inventory.serializer import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()

    class Meta:
        model = CartItems
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItems
        fields = '__all__'
