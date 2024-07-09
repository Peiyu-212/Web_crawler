import pytz

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
        representation['photo'] = {"filepath": instance.photo.filepath.url,
                                   "url": instance.photo.url,
                                   "title": instance.photo.title}
        return representation
