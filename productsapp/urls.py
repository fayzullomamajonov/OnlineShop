from django.urls import path
from .views import categorymodel,productlist,get_product_info,user_login,user_signup, user_logout


urlpatterns = [
    path('',categorymodel,name='home'),
    path('login/',user_login,name='login'),
    path('signup/',user_signup,name='signup'),
    path('logout/',user_logout,name='logout'),
    path('product/<str:category>/',productlist,name='product'),
    path('product-info/<int:pk>/',get_product_info,name='product_info')
]