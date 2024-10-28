from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

class Subscriber(models.Model):
    email = models.CharField(max_length=100, null=False)

class Notification(models.Model):
    subscriber = models.ForeignKey(Subscriber, models.CASCADE, null=False)
    post = models.ForeignKey(Blog, models.CASCADE, null=False)
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)