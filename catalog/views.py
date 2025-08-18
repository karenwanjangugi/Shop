from django.shortcuts import render
from .models import Product

# Create your views here.

def list_products(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'catalog/product_details.html', {'product': product})  






