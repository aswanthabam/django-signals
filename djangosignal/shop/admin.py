from django.contrib import admin

# Register your models here.

from .models import Order, OrderLog

admin.site.register(Order)
admin.site.register(OrderLog)
