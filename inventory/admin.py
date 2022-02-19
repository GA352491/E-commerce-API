from django.contrib import admin
from inventory.models import Category, Product, QuantityVariant, ColorVariant, SizeVariant, ProductImages, Company

# ProductInventory,ProductType, ProductAttribute, ProductAttributeValues, #ProductAttributeValue, Stock, Media, Brand

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
admin.site.register(ProductImages)
admin.site.register(Company)
# admin.site.register(ProductAttribute)
# admin.site.register(ProductInventory)
# admin.site.register(ProductType)
# admin.site.register(ProductAttributeValues)
# admin.site.register(ProductAttributeValue)
# admin.site.register(Stock)
# admin.site.register(Media)
# admin.site.register(Brand)
