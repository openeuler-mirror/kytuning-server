"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
from appStore.testMachine.models import TestMachine
from appStore.testMachine.serializers import TestMachineSerializer
from rest_framework import status, viewsets

# Create your views here.

class TestMachineViewSet(viewsets.ModelViewSet):
    """
    测试机器数据管理
    """

    queryset = TestMachine.objects.all().order_by('-id')
    serializer_class = TestMachineSerializer
