from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'mainapp/index.html')


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'mainapp/shop.html', context)
