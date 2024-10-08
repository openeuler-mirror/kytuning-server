from rest_framework import serializers
from appStore.users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    用户信息
    """

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserProfile(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = UserProfile
        fields = (
            'id', 'username', 'password', 'chinese_name', 'is_active', 'is_superuser', 'is_staff', 'user_phone',
        )
