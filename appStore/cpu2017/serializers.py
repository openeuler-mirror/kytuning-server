from rest_framework import serializers
from appStore.cpu2017.models import Cpu2017

class Cpu2017Serializer(serializers.ModelSerializer):
    """
    cpu2017数据序列化
    """

    class Meta:
        model = Cpu2017
        fields = '__all__'
