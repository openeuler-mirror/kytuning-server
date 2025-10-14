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

from appStore.utils.common import json_response


# Create your views here.

class TestMachineViewSet(viewsets.ModelViewSet):
    """
    测试机器数据管理
    """

    queryset = TestMachine.objects.all().order_by('-id')
    serializer_class = TestMachineSerializer

    def list(self, request, *args, **kwargs):
        queryset = TestMachine.objects.all().order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

    def create(self, request, *args, **kwargs):
        machine_data = {}
        machine_data['owner'] = request.user.chinese_name
        machine_data['machine_name'] = request.data.get('machine_name')
        machine_data['arch_name'] = request.data.get('arch_name')
        machine_data['cpu_module_name'] = request.data.get('cpu_module_name')
        machine_data['BMC_IP'] = request.data.get('BMC_IP')
        machine_data['BMC_user_name'] = request.data.get('BMC_user_name')
        machine_data['BMC_password'] = request.data.get('BMC_password')
        config_serializer = TestMachineSerializer(data=machine_data)
        if config_serializer.is_valid():
            self.perform_create(config_serializer)
            return json_response(config_serializer.data, status.HTTP_200_OK, '创建成功！')
        return json_response(config_serializer.errors, status.HTTP_400_BAD_REQUEST, config_serializer.errors)

    def put(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        machine_data.owner = request.user.chinese_name
        machine_data.machine_name = request.data.get('machine_name')
        machine_data.arch_name = request.data.get('arch_name')
        machine_data.cpu_module_name = request.data.get('cpu_module_name')
        machine_data.BMC_IP = request.data.get('BMC_IP')
        machine_data.BMC_user_name = request.data.get('BMC_user_name')
        machine_data.BMC_password = request.data.get('BMC_password')
        machine_data.save()
        return json_response({}, status.HTTP_200_OK, '修改成功')

    def apply_use_machine(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        machine_data.queue_user = request.user.chinese_name
        machine_data.save()
        return json_response({}, status.HTTP_200_OK, '申请成功')



    def delete(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if not id or not TestMachine.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        if request.user.is_superuser:
            test_case_data = TestMachine.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            TestMachine.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只有管理员才能删除该数据')