"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 11:24:20 2024 +0800
"""
from rest_framework import serializers
from appStore.cpu2017.models import Cpu2017

class Cpu2017Serializer(serializers.ModelSerializer):
    """
    cpu2017数据序列化
    """

    class Meta:
        model = Cpu2017
        fields = '__all__'
