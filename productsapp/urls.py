from django.urls import path
from .views import HomePageView,ProductsView


urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('products/',ProductsView.as_view(),name='products'),
]