from rest_framework import serializers
from appStore.project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Project数据序列化
    """

    class Meta:
        model = Project
        fields = '__all__'
