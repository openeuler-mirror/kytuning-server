"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 10:58:36 2024 +0800
"""
import logging
from rest_framework import status, viewsets
# Create your views here.
from appStore.ksFile.models import KsFile
from appStore.ksFile.serializers import KsFileListSerializer
from appStore.utils.common import LimsPageSet, json_response

log = logging.getLogger('kytuninglog')

class KsFileListViewSet(viewsets.ModelViewSet):
    """
     ks列表数据管理
    """
    queryset = KsFile.objects.all()
    serializer_class = KsFileListSerializer
    pagination_class = LimsPageSet

    def list(self, request, *args, **kwargs):
        queryset = KsFile.objects.all().order_by('ks_name')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

    def create(self, request, *args, **kwargs):
        ks_data = {}
        ks_data['user_name'] = request.user.chinese_name
        ks_data['ks_name'] = request.data.get('ks_name')
        ks_data['ks_content'] = request.data.get('ks_content')
        config_serializer = KsFileListSerializer(data=ks_data)
        if config_serializer.is_valid():
            self.perform_create(config_serializer)
            return json_response(config_serializer.data, status.HTTP_200_OK, '创建成功！')
        log.info('Machine数据存储错误 ：%s，', config_serializer.errors)
        log.info('Machine存储数据为 ：%s，', ks_data)
        return json_response(config_serializer.errors, status.HTTP_400_BAD_REQUEST, config_serializer.errors)



