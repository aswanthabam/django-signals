from django.contrib import admin
from .models import Blog, Subscriber, Notification
# Register your models here.
admin.site.register([Blog, Subscriber, Notification])