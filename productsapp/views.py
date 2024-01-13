from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from django.views.generic import DeleteView
# Create your views here.

def categorymodel(request):
    categorys = CategoryModel.objects.all()
    context = {
        'categorys': categorys
    }

    return render(request,'home.html',context=context)

def productlist(request,category):
    products = ProductModel.objects.filter(category=category)
    category = category
    context = {
        'products':products,
        'category':category
    }
    return render(request,'product.html',context=context)


def get_product_info(request, pk):
    product = ProductModel.objects.filter(id=pk)
    context = {
        'product':product
    }

    return render(request,'product_info.html',context=context)