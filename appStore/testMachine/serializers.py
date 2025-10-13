"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
from rest_framework import serializers

from appStore.testMachine.models import TestMachine


class TestMachineSerializer(serializers.ModelSerializer):
    """
    testMachine数据序列化
    """
    use_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = TestMachine
        fields = '__all__'
