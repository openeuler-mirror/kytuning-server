from rest_framework import serializers
from appStore.cpu2006.models import Cpu2006

class Cpu2006Serializer(serializers.ModelSerializer):
    """
    Cpu2006数据序列化
    """

    class Meta:
        model = Cpu2006
        fields = '__all__'
