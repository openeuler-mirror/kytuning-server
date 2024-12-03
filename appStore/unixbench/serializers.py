"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Mar 4 10:03:36 2024 +0800
"""
from rest_framework import serializers
from appStore.unixbench.models import Unixbench

class UnixbenchSerializer(serializers.ModelSerializer):
    """
    stream数据序列化
    """

    class Meta:
        model = Unixbench
        fields = '__all__'
