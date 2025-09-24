"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:10:52 2024 +0800
"""
from appStore.userConfig.models import UserConfig
from appStore.userConfig.serializers import UserConfigSerializer
from appStore.utils.customer_view import CusModelViewSet
# Create your views here.

class UserConfigViewSet(CusModelViewSet):
    """
    测试机器数据管理
    """

    queryset = UserConfig.objects.all().order_by('-id')
    serializer_class = UserConfigSerializer