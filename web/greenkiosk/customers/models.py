from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.user()

class ShippingAddress(models.Model):
    
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=6)
    notes = models.TextField()
    

    def __str__(self):
        return self.customer()
