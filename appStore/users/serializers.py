"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Thu Aug 15 17:18:23 2024 +0800
"""
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
