from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


# Create your views here.
