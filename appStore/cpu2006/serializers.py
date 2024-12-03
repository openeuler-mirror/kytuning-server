"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 11:07:17 2024 +0800
"""
from rest_framework import serializers
from appStore.cpu2006.models import Cpu2006

class Cpu2006Serializer(serializers.ModelSerializer):
    """
    Cpu2006数据序列化
    """

    class Meta:
        model = Cpu2006
        fields = '__all__'
