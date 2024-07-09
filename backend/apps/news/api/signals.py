from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import News


@receiver(post_save, sender=News)
def send_new_data_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "AddNews",
            {
                "type": "send_new_data",
                "text": "New data available"
            },
        )
