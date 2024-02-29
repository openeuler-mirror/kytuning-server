from rest_framework import serializers
from appStore.lmbench.models import Lmbench

class LmbenchSerializer(serializers.ModelSerializer):
    """
    Lmbench数据序列化
    """

    class Meta:
        model = Lmbench
        fields = '__all__'
