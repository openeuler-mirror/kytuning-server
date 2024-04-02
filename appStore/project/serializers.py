from rest_framework import serializers
from appStore.project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Project数据序列化
    """
    test_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
