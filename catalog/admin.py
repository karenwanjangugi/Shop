from django.contrib import admin
from .models import Product,Category,Customer,Subscription
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Subscription)
# Register your models here.