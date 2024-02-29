from rest_framework import serializers
from appStore.fio.models import Fio

class FioSerializer(serializers.ModelSerializer):
    """
    fio数据序列化
    """

    class Meta:
        model = Fio
        fields = '__all__'
