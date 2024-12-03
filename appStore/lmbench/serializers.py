"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Thu Feb 29 16:18:43 2024 +0800
"""
from rest_framework import serializers
from appStore.lmbench.models import Lmbench

class LmbenchSerializer(serializers.ModelSerializer):
    """
    Lmbench数据序列化
    """

    class Meta:
        model = Lmbench
        fields = '__all__'
