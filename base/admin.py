from django.contrib import admin
from .models import User,Product,Category,Order,Supplier,Shipment,Warehouse,Customer

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Supplier)
admin.site.register(Shipment)
admin.site.register(Warehouse)
