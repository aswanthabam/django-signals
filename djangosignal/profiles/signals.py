# profiles/signals.py

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.dispatch import Signal
from django.contrib.auth.models import User
from .models import Profile


# Pre-save signal receiver for the Profile model
@receiver(pre_save, sender=Profile)
def lowercase_username(sender, instance, **kwargs):
    # Convert the username to lowercase before saving
    instance.username = instance.username.lower()


# Post-save signal receiver for the Profile model
@receiver(post_save, sender=Profile)
def profile_saved_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Profile created for user: {instance.user.username}")
    else:
        print(f"Profile updated for user: {instance.user.username}")


# The providing_args argument was deprecated in Django 4.0 and removed in Django 4.1. You no longer need to use it when creating a signal. You can simply define the signal without any arguments.
bio_updated = Signal()
