from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

class Catergory(models.Model):
    catergory = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.catergory}"

class Top(models.Model):
    topping = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.topping} - {self.price}"

class Size(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.size}"

# Create your models here.
class Fooditem(models.Model):
    item = models.CharField(max_length=64)
    cat = models.ForeignKey(Catergory, on_delete=models.CASCADE, related_name="catergories")
    minnumberoftoppings = models.PositiveSmallIntegerField(default=0)
    maxnumberoftoppings = models.PositiveSmallIntegerField(default=0)
    onesize = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pricelarge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    toppings = models.ManyToManyField(Top, blank=True, null=True)

    def __str__(self):
        return f"{self.item}"

class Extras(models.Model):
    topping = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    canbeon = models.ManyToManyField(Fooditem, related_name="goeson")

    def __str__(self):
        return f"{self.topping}  ${self.price}"

class Order(models.Model):
    order = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    item = models.ForeignKey(Fooditem,on_delete=models.SET_NULL,null=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True)
    toppings = models.ManyToManyField(Extras)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    order_placed = models.DateTimeField(default=timezone.now)
    asap = models.BooleanField(default=True)
    requested = models.CharField(max_length=5,null=True, blank=True)
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
    size = models.ForeignKey(Size,on_delete=models.CASCADE, null=True)
    itemid = models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Extras, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
# need to work out if need forgeinn key for cart and then do the do

    def __str__(self):
        return f"{self.item} - {self.toppings}"
