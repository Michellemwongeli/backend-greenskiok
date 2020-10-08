from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Product
from customers.models import Customer


class Cart(models.Model):
    products=models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created=models.DateTimeField()
    total_price=models.DecimalField(max_digits=6, decimal_places=5)
    status=models.CharField(max_length=60)
    

    def __str__(self):
        return self.products()

class Payment(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=60)
    #order=models.OneToOneField(Order, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=30,decimal_places=2)
    date_Of_Payment =models.DateTimeField()
    

    def __str__(self):
        return self.customer()

class Order(models.Model):
    order_number=models.IntegerField()
    date_placed=models.DateTimeField()
    status=models.CharField(max_length=100)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE)
    #payment=models.OneToOneField(Payment, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    # shipping_provider = models.ForeignKey('shipping.Shipping_Provider', on_delete=models.CASCADE)
    order_price = models.DecimalField( blank=True, null=True, max_digits=30,decimal_places=3)
    shipping_cost = models.DecimalField(blank=True, null=True, max_digits=40,decimal_places=4)
    total_price = models.DecimalField( blank=True, null=True, max_digits=20,decimal_places=5)

    def __str__(self):
        return self.order_number()