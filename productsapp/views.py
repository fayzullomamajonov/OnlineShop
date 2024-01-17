from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreationForm, LoginForm


# Create your views here.

def categorymodel(request):
    categorys = CategoryModel.objects.all()
    context = {
        'categorys': categorys
    }

    return render(request,'home.html',context=context)

# sing up view

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

# login page view

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

# logout page 

def user_logout(request):
    logout(request)
    return redirect('login')


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