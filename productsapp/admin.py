from django.contrib import admin
from .models import ProductModel,CategoryModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(ProductModel)


