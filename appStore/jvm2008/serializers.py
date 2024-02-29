from rest_framework import serializers
from appStore.jvm2008.models import Jvm2008

class Jvm2008Serializer(serializers.ModelSerializer):
    """
    Jvm2008数据序列化
    """

    class Meta:
        model = Jvm2008
        fields = '__all__'
