from django.shortcuts import render, get_object_or_404
from .models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalog/product_details.html', {'product': product})
