from django.db import models

# Create your models here.
# profiles/models.py

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        from .signals import bio_updated

        # Check if the instance already exists in the database
        if self.pk:
            old_instance = Profile.objects.get(pk=self.pk)
            if old_instance.bio != self.bio:
                # Send the signal if the bio has changed
                bio_updated.send(
                    sender=self.__class__,
                    user=self.user,
                    old_bio=old_instance.bio,
                    new_bio=self.bio,
                )
        super().save(*args, **kwargs)
