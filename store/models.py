from django.db import models
import datetime

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'



class Product(models.Model):
    name=models.CharField( max_length=50)
    price=models.DecimalField(default=0, max_digits=6, decimal_places=2)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=100,default='',blank=True,null=True)
    image=models.ImageField(upload_to='upload/product/')

def __str__(self):
    return str( self.name)




class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=250,default='',blank=True)
    quantity = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name}"