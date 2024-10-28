from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from blog.models import Blog, Notification, Subscriber

@receiver(post_save, sender=Blog)
def onblogsave(sender, instance, **kwargs):
    if instance.published:
        Notification.objects.bulk_create([
            Notification(
                subscriber_id=sub_id,
                post=instance,
                message=f"A new post titled '{instance.title}' has been published!"
            ) for sub_id in Subscriber.objects.all().values_list("id",flat=True)
        ])