"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
# Create your views here.
from appStore.adaptISO.models import AdaptISO
from appStore.adaptISO.serializers import AdaptISOListSerializer
from appStore.utils.common import LimsPageSet, json_response
from rest_framework import status, viewsets

import logging
log = logging.getLogger('mydjango') #这里的mydjango是settings中loggers里面对应的名字


class AdaptISOListViewSet(viewsets.ModelViewSet):
    """
    错误收集数据管理
    """
    queryset = AdaptISO.objects.all()
    serializer_class = AdaptISOListSerializer
    pagination_class = LimsPageSet

    def list(self, request, *args, **kwargs):
        queryset = AdaptISO.objects.all().order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

