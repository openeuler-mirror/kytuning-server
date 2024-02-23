from rest_framework import serializers
from appStore.env.models import Env

class EnvSerializer(serializers.ModelSerializer):
    """
    环境数据序列化
    """

    class Meta:
        model = Env
        fields = '__all__'