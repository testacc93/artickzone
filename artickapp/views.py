from django.shortcuts import render
from .models import Product

def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', context={'products':product})

def products(request):
    product = Product.objects.all()
    return render(request, 'product.html', context={'products':product})

def about(request):
    product = Product.objects.all()
    return render(request, 'about.html', context={'products':product})

def contact(request):
    product = Product.objects.all()
    return render(request, 'contact.html', context={'products':product})