from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300,default='username')
    contact = models.IntegerField(null = True)
    address = models.CharField(max_length=300,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','contact','address']

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    contact_person = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.name} {"-->"} {self.category.name}'

class Customer(models.Model):
    name = models.CharField(max_length = 300)
    address = models.CharField(max_length=300)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=300,null=True)
    customer = models.ManyToManyField(Customer)
    product = models.ManyToManyField(Product)
    order_date = models.DateField()
    delivery_date = models.DateField()
    

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.location} {"-->"} {self.category.name}'

class Shipment(models.Model):
    ORDER_STATUSES = (
    (1, 'Processing'),
    (2, 'Delivered'),
    (3, 'Cancelled')
)

    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.SET_NULL,null=True)
    shipment_data = models.TextField()
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUSES, default=1)

    def __str__(self):
        if self.status == 1:
            state = " --> Processing"
            return f'{self.order.name} {state}'
    
        elif self.status == 2:
            state = " --> Delivered"
            return f'{self.order.name} {state}'
        
        elif self.status == 3:
            state = " --> Cancelled"
            return f'{self.order.name} {state}'
        



