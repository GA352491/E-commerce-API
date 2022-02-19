from django.shortcuts import render, redirect
from drf_yasg import openapi

from inventory.models import Category, Product, ProductImages, ColorVariant, QuantityVariant, SizeVariant, Company
from inventory.serializer import CategorySerializer, ProductSerializer, CompanySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from carts.models import Cart, CartItems
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
category_param = openapi.Parameter('category', in_=openapi.IN_QUERY, description='description', type=openapi.TYPE_STRING, )


class DemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "success"})


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[category_param])
    def get(self, request, **kwargs):
        category = self.request.query_params.get('category')
        print(category)
        if category:
            queryset = Product.objects.filter(category__name=category).all()
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})

    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        #     return Response(serializer_data.data, status=201)
        return Response({'data': 'request.data'})

    def put(self):
        pass

    def delete(self):
        pass


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def add_to_cart(request, pk):
    print(pk)
    product = Product.objects.get(id=pk)
    print(product)
    cart, _ = Cart.objects.get_or_create(user=request.user, ordered=False)
    cart_item = CartItems.objects.create(product=product, cart=cart, user=request.user, price=product.price, quantity=1)
    return redirect('home')


def show_cart(request):
    user = request.user
    cart = Cart.objects.get(user=user, ordered=False)
    cartitems = CartItems.objects.filter(cart=cart)
    context = {'cartitems': cartitems, 'total_price': cart.total_price}
    return render(request, 'cart.html', context)


class CompanyView(APIView):
    # @swagger_auto_schema(request_body=CompanySerializer)
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CompanySerializer)
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
