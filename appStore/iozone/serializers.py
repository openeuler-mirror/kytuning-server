from rest_framework import serializers
from appStore.iozone.models import Iozone

class IozoneSerializer(serializers.ModelSerializer):
    """
    iozone数据序列化
    """

    class Meta:
        model = Iozone
        fields = '__all__'
