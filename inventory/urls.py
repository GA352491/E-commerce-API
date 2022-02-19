from django.contrib import admin
from django.urls import path, include
from inventory import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.ProductView.as_view()),
    path('company/', views.CompanyView.as_view()),
    path('demo/', views.DemoView.as_view()),
    path('addtocart/<pk>/', views.add_to_cart, name='addtocart'),
    path('showcart', views.show_cart, name='cart'),

]
