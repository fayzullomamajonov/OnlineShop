from django.urls import path
from .views import categorymodel,productlist,get_product_info


urlpatterns = [
    path('',categorymodel,name='home'),
    path('product/<str:category>/',productlist,name='product'),
    path('product-info/<int:pk>/',get_product_info,name='product_info')
]