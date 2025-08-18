from django.db import models
# # Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=28)
    def __str__(self):
        return self.name
class Subscription(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.name} price {self.price}"
class Customer(models.Model):
    subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE)
    def __str__(self):
        return f"Customer with subscription {self.subscription}"
