from rest_framework import serializers
from appStore.unixbench.models import Unixbench

class UnixbenchSerializer(serializers.ModelSerializer):
    """
    stream数据序列化
    """

    class Meta:
        model = Unixbench
        fields = '__all__'
