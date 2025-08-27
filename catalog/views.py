from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import ProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'catalog/product_details.html', {'product': product})  

@csrf_exempt
def update_stock(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = json.loads(request.body)
        action = data.get('action')

        if action == 'add':
            product.stock += 1
        elif action == 'subtract':
            if product.stock > 0:
                product.stock -= 1
        
        product.save()
        return JsonResponse({'stock': product.stock})
    return JsonResponse({'error': 'Invalid request'}, status=400) 

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(list_products)
    else:
        form = ProductForm()
        
    return render(request, "catalog/create_product.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_products')
    else:
        form = AuthenticationForm()
    return render(request, 'catalog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

    