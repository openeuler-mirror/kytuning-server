"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 10:58:36 2024 +0800
"""
import os
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
        ks_data['message'] = request.data.get('message')
        ks_data['ks_content'] = request.data.get('ks_content')
        config_serializer = KsFileListSerializer(data=ks_data)
        if config_serializer.is_valid():
            self.perform_create(config_serializer)
            # 创建ks文件
            with open('./appStore/utils/autoInstall/' + ks_data['ks_name'], 'w') as file:
                file.write(ks_data['ks_content'])
            log.info('创建%s文件完成，' % ks_data['ks_name'])
            return json_response(config_serializer.data, status.HTTP_200_OK, '创建成功！')
        log.info('Machine数据存储错误 ：%s，' % config_serializer.errors)
        log.info('Machine存储数据为 ：%s，' % ks_data)
        return json_response(config_serializer.errors, status.HTTP_400_BAD_REQUEST, config_serializer.errors)

    def put(self, request, *args, **kwargs):
        ks_id = request.data.get('id')
        ks_data = KsFile.objects.get(id=ks_id)
        if not ks_id or not ks_data:
            return json_response({}, status.HTTP_204_NO_CONTENT, '未获取到数据')
        if request.user.is_superuser or request.user.chinese_name == ks_data.user_name:
            ks_data.ks_name = request.data.get('ks_name')
            ks_data.message = request.data.get('message')
            ks_data.ks_content = request.data.get('ks_content')
            ks_data.save()
            # 更新ks文件
            with open('./appStore/utils/autoInstall/' + ks_data.ks_name, 'w') as file:
                file.write(ks_data.ks_content)
            log.info('更新%s文件完成，' % ks_data.ks_name)
            return json_response('', status.HTTP_200_OK, '更新成功！')
        else:
            return json_response({}, status.HTTP_401_UNAUTHORIZED, '只有管理员或者管理人员才能修改数据')

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if not id or not KsFile.objects.filter(id=id):
            return json_response({}, status.HTTP_400_BAD_REQUEST, '请传递正确的测试id')
        ks_file_data = KsFile.objects.filter(id=id).first()
        if not ks_file_data:
            return json_response({}, status.HTTP_204_NO_CONTENT, '未获取到数据')
        # 判断只有能删除自己的数据或者是管理员。
        if request.user.is_superuser or request.user.chinese_name == ks_file_data.user_name:
            # todo 增加一个公共函数获取增加 装饰器 功能（因为有很多地方使用到了）
            KsFile.objects.filter(id=id).delete()
            try:
                # 删除ks文件
                os.remove('./appStore/utils/autoInstall/' + ks_file_data.ks_name)
                log.info('删除%s文件完成，' % ks_file_data.ks_name)
            except Exception as e:
                log.info('删除%s文件时发生错误：%s，' % (ks_file_data.ks_name, e))
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_401_UNAUTHORIZED, '只有管理员或者管理人员才能删除该数据')
