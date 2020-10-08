from django.db import models
from django.contrib.auth.models import User
from kiosks.models import Kiosk

class ProductSupplier(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField()
    street_address=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    id_number=models.IntegerField()
    date_added=models.DateTimeField()
    profile_picture=models.ImageField()

    def __str__(self):
        return self.user.get_full_name()

    
class ProductCategory(models.Model):
   name = models.CharField(max_length=28)
   description = models.TextField()
   icon = models.ImageField()

    
   def __str__(self):
        return self.name

        
class Product(models.Model):
    title=models.CharField(max_length=29)
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description=models.TextField()
    supplier_price=models.DecimalField(max_digits=30,decimal_places=2)
    selling_price=models.DecimalField(max_digits=20,decimal_places=3)
    supplier=models.ForeignKey(ProductSupplier, on_delete=models.CASCADE)
    kiosk=models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    number_in_stock=models.IntegerField() 
    product_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class productImage(models.Model):
    #product=models.ForeignKey(max_length=29)
    image=models.ImageField()

    def __str__(self):
        return self.product()
    
class productReview(models.Model):
   # product=models.ForeignKey(max_length=29)
    customer=models.ImageField()
    review = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return self.product()