"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 11:15:07 2024 +0800
"""
import logging
from rest_framework import status, viewsets
# Create your views here.
from appStore.userConfig.models import UserConfig
from appStore.userConfig.serializers import UserConfigSerializer
from appStore.utils.common import json_response

log = logging.getLogger('kytuninglog')

class UserConfigViewSet(viewsets.ModelViewSet):
    """
    用户配置数据管理
    """
    queryset = UserConfig.objects.all().order_by('-id')
    serializer_class = UserConfigSerializer

    def list(self, request, *args, **kwargs):
        queryset = UserConfig.objects.filter(user_name=request.user.chinese_name).all().order_by('-id')
        id = request.GET.get('configID')
        if not queryset:
            return json_response({}, status.HTTP_200_OK, '没有查到对应数据')
        if id:
            if id == '0':  # 获取最后一条数据
                queryset = [queryset.first()]
            else:
                queryset = queryset.filter(id=id)
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '用户列表获取完成')

    def create(self, request, *args, **kwargs):
        data_user_config = {}
        data_user_config['user_name'] = request.user.chinese_name
        data_user_config['config_name'] = request.data.get('config_name')
        data_user_config['project_name'] = request.data.get('project_name')
        data_user_config['stream_number'] = request.data.get('stream')
        data_user_config['lmbench_number'] = request.data.get('lmbench')
        data_user_config['unixbench_number'] = request.data.get('unixbench')
        data_user_config['fio_number'] = request.data.get('fio')
        data_user_config['iozone_number'] = request.data.get('iozone')
        data_user_config['jvm2008_number'] = request.data.get('jvm2008')
        data_user_config['cpu2006_number'] = request.data.get('cpu2006')
        data_user_config['cpu2017_number'] = request.data.get('cpu2017')
        data_user_config['stream_config'] = request.data.get('yaml')['stream']
        data_user_config['lmbench_config'] = request.data.get('yaml')['lmbench']
        data_user_config['unixbench_config'] = request.data.get('yaml')['unixbench']
        data_user_config['fio_config'] = request.data.get('yaml')['fio']
        data_user_config['iozone_config'] = request.data.get('yaml')['iozone']
        data_user_config['jvm2008_config'] = request.data.get('yaml')['jvm2008']
        data_user_config['cpu2006_config'] = request.data.get('yaml')['cpu2006']
        data_user_config['cpu2006_loongarch64_config'] = request.data.get('yaml')['cpu2006_loongarch64']
        data_user_config['cpu2017_config'] = request.data.get('yaml')['cpu2017']
        data_user_config['project_message'] = request.data.get('project_message')
        if request.data.get('is_send_config'):
            data_user_config['is_send_config'] = request.data.get('is_send_config')
            # 删除旧数据
            UserConfig.objects.filter(user_name=data_user_config['user_name']).filter(is_send_config=True).delete()
        serializer_config = UserConfigSerializer(data=data_user_config)
        if serializer_config.is_valid():
            self.perform_create(serializer_config)
            return json_response(serializer_config.data, status.HTTP_200_OK, '创建成功！')
        log.info('userConfig数据存储错误 ：%s，'%serializer_config.errors)
        log.info('userConfig存储数据为 ：%s，'%data_user_config)
        return json_response({}, status.HTTP_400_BAD_REQUEST, serializer_config.errors)

    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        if not id or not UserConfig.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = UserConfig.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            config_data = UserConfig.objects.get(id=id)  # get=filter.first()
            if not config_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            config_data.config_name = request.data.get('config_name')
            # config_data.user_password = request.data.get('user_password')
            config_data.project_name = request.data.get('project_name')
            config_data.stream_number = request.data.get('stream')
            config_data.lmbench_number = request.data.get('lmbench')
            config_data.unixbench_number = request.data.get('unixbench')
            config_data.fio_number = request.data.get('fio')
            config_data.iozone_number = request.data.get('iozone')
            config_data.jvm2008_number = request.data.get('jvm2008')
            config_data.cpu2006_number = request.data.get('cpu2006')
            config_data.cpu2017_number = request.data.get('cpu2017')
            config_data.stream_config = request.data.get('yaml').get('stream')
            config_data.lmbench_config = request.data.get('yaml').get('lmbench')
            config_data.unixbench_config = request.data.get('yaml').get('unixbench')
            config_data.fio_config = request.data.get('yaml').get('fio')
            config_data.iozone_config = request.data.get('yaml').get('iozone')
            config_data.jvm2008_config = request.data.get('yaml').get('jvm2008')
            config_data.cpu2006_config = request.data.get('yaml').get('cpu2006')
            config_data.cpu2006_loongarch64_config = request.data.get('yaml').get('cpu2006_loongarch64')
            config_data.cpu2017_config = request.data.get('yaml').get('cpu2017')
            config_data.project_message = request.data.get('project_message')
            config_data.save()
            return json_response({}, status.HTTP_200_OK, '修改成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许修改该数据')

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if not id or not UserConfig.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = UserConfig.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            test_case_data = UserConfig.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            UserConfig.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许删除该数据')
