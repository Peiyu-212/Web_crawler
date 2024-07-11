import os

import pytz

from django.conf import settings

from rest_framework import serializers

from ..models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        local_tz = pytz.timezone('Asia/Taipei')
        local_time = instance.news_time.astimezone(local_tz)
        representation['news_time'] = local_time.strftime('%Y-%m-%d %H:%M:%S')

        if os.path.exists(settings.MEDIA_ROOT + '/' +
                          instance.photo.filepath.name):
            filepath = instance.photo.filepath.url
        else:
            filepath = instance.photo.url
        representation['photo'] = {"filepath": filepath,
                                   "title": instance.photo.title}
        return representation
