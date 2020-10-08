from django.urls import path
from . import views
from .views import products_list

urlpatterns = [
    path('products/', products_list, name='products_list'),
    
]
