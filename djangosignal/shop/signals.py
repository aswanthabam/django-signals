# shop/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderLog


def create_order_log(sender, instance, created, **kwargs):
    if created:
        OrderLog.objects.create(order_number=instance.order_number, action="Created")


# Connect the signal using connect() with dispatch_uid
post_save.connect(create_order_log, sender=Order, dispatch_uid="create_order_log")
