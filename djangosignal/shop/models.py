from django.db import models

# Create your models here.
# shop/models.py
from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


class OrderLog(models.Model):
    order_number = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_number} - {self.action}"
