# profiles/receivers.py

from django.dispatch import receiver
from .signals import bio_updated


@receiver(bio_updated)
def notify_bio_change(sender, **kwargs):
    user = kwargs["user"]
    old_bio = kwargs["old_bio"]
    new_bio = kwargs["new_bio"]

    print(f"User '{user.username}' updated their bio from '{old_bio}' to '{new_bio}'")
