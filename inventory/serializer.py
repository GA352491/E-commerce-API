from rest_framework import serializers
from inventory.models import Category, Product, ProductImages, ColorVariant, QuantityVariant, SizeVariant, Company


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuantityVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'


class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'


class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # company = CompanySerializer()
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        # exclude=[]
