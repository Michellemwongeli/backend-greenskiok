from django.contrib import admin

# Register your models here.
from .models import Cart, Payment, Order
# Register your models here.

admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Order)
