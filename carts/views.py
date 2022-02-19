from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from carts.models import Cart, CartItems, Order, OrderedItems
from inventory.models import Product
from carts.serializer import CartSerializer, OrderSerializer, OrderedItemsSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # serializer_class = CartSerializer
    # swagger_schema = CartSerializer

    def get(self, request):
        user = request.user
        print(user)
        cart = Cart.objects.get(user=user, ordered=False)
        queryset = CartItems.objects.filter(cart=cart.id)
        serializer = CartSerializer(queryset, many=True)

        return Response({"success": "permission is working", "data": serializer.data})

    @swagger_auto_schema(request_body=CartSerializer)
    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        product = Product.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItems(user=user, product=product, cart=cart, quantity=quantity, price=price)
        cart_items.save()

        return Response({'Success': 'Items Added to your cart '})

    def put(self, request):
        data = request.data
        cart_item = CartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()

        return Response({"message": "Updated"})

    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = CartItems.objects.get(id=data.get('id'))
        cart_item.delete()
        cart = Cart.objects.get(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart.id)
        serializer = CartSerializer(queryset, many=True)

        return Response({"success": "permission is working", "data": serializer.data})


class OrderAPI(APIView):
    def get(self, request):
        user = request.user
        queryset = Order.objects.get(user=user)
        serializer = OrderSerializer(queryset, many=True)
        return Response({"Orders": serializer.data})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
