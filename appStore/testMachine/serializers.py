from rest_framework import serializers
from appStore.testMachine.models import TestMachine


class TestMachineSerializer(serializers.ModelSerializer):
    """
    testMachine数据序列化
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = TestMachine
        fields = '__all__'
