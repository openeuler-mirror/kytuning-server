"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 14:07:53 2024 +0800
"""
from rest_framework import serializers
from appStore.env.models import Env

class EnvSerializer(serializers.ModelSerializer):
    """
    环境数据序列化
    """

    class Meta:
        model = Env
        fields = '__all__'