from rest_framework import serializers
from appStore.stream.models import Stream

class StreamSerializer(serializers.ModelSerializer):
    """
    stream数据序列化
    """

    class Meta:
        model = Stream
        fields = '__all__'
