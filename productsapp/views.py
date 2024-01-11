from django.shortcuts import render
from django.views.generic import TemplateView,DeleteView
# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'

class ProductsView(TemplateView):
    template_name = 'products.html'