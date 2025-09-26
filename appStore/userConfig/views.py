"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:10:52 2024 +0800
"""
from appStore.userConfig.models import UserConfig
from appStore.userConfig.serializers import UserConfigSerializer
from appStore.utils.common import json_response
from appStore.utils.customer_view import CusModelViewSet
# Create your views here.

class UserConfigViewSet(CusModelViewSet):
    """
    测试机器数据管理
    """
    queryset = UserConfig.objects.all().order_by('-id')
    serializer_class = UserConfigSerializer

    def list(self, request, *args, **kwargs):
        queryset = UserConfig.objects.filter(user_name=request.user.username).all().order_by('-id')
        if not queryset:
            return json_response({}, status.HTTP_200_OK, '列表')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '测试完成')

    def create(self, request, *args, **kwargs):
        user_config_data = {}
        user_config_data['user_name'] = request.user.username
        user_config_data['user_password'] = request.data.get('user_password')
        user_config_data['project_name'] = request.data.get('project_name')
        user_config_data['test_ip'] = request.data.get('test_ip')
        user_config_data['test_password'] = request.data.get('test_password')
        user_config_data['stream_number'] = request.data.get('stream')
        user_config_data['lmbench_number'] = request.data.get('lmbench')
        user_config_data['unixbench_number'] = request.data.get('unixbench')
        user_config_data['fio_number'] = request.data.get('fio')
        user_config_data['iozone_number'] = request.data.get('iozone')
        user_config_data['jvm2008_number'] = request.data.get('jvm2008')
        user_config_data['cpu2006_number'] = request.data.get('cpu2006')
        user_config_data['cpu2017_number'] = request.data.get('cpu2017')
        user_config_data['stream_config'] = request.data.get('yaml')['stream']
        user_config_data['lmbench_config'] = request.data.get('yaml')['lmbench']
        user_config_data['unixbbench_config'] = request.data.get('yaml')['unixbench']
        user_config_data['fio_config'] = request.data.get('yaml')['fio']
        user_config_data['iozone_config'] = request.data.get('yaml')['iozone']
        user_config_data['jvm2008_config'] = request.data.get('yaml')['jvm2008']
        user_config_data['cpu2006_config'] = request.data.get('yaml')['cpu2006']
        user_config_data['cpu2006_loongarch64_config'] = request.data.get('yaml')['cpu2006_loongarch64']
        user_config_data['cpu2017_config'] = request.data.get('yaml')['cpu2017']
        config_serializer = UserConfigSerializer(data=user_config_data)
        if config_serializer.is_valid():
            self.perform_create(config_serializer)
            return json_response(config_serializer.data, status.HTTP_200_OK, '创建成功！')
        return json_response({}, status.HTTP_400_BAD_REQUEST,config_serializer.errors)

    def delete(self, request):
        id = request.data.get('id', None)
        if not id or not UserConfig.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = UserConfig.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.username == user_name:
            test_case_data = UserConfig.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            UserConfig.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许删除该数据')


