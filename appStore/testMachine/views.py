"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
import logging
from rest_framework import status, viewsets
# Create your views here.
from appStore.adaptISO.models import AdaptISO
from appStore.testMachine.models import TestMachine
from appStore.testMachine.serializers import TestMachineSerializer
from appStore.utils.common import json_response, get_link_status, update_system, update_auto_install, make_ks_password

log = logging.getLogger('kytuninglog')

class TestMachineViewSet(viewsets.ModelViewSet):
    """
    测试机器数据管理
    """
    queryset = TestMachine.objects.all().order_by('-id')
    serializer_class = TestMachineSerializer

    def list(self, request, *args, **kwargs):
        if (request.GET.get('search_by_name',None)):
            queryset = TestMachine.objects.filter(owner=request.user.chinese_name).order_by('-id')
        else:
            queryset = TestMachine.objects.all().order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

    def create(self, request, *args, **kwargs):
        if TestMachine.objects.get(BMC_IP=request.data.get('BMC_IP')):
            return json_response({}, status.HTTP_205_RESET_CONTENT, 'BMC_IP重复，请修改BMC_IP')
        data_machine = {}
        data_machine['owner'] = request.user.chinese_name
        data_machine['creator'] = request.user.chinese_name
        data_machine['machine_name'] = request.data.get('machine_name')
        data_machine['arch_name'] = request.data.get('arch_name')
        data_machine['cpu_module_name'] = request.data.get('cpu_module_name')
        data_machine['BMC_IP'] = request.data.get('BMC_IP')
        data_machine['BMC_user_name'] = request.data.get('BMC_user_name')
        data_machine['BMC_password'] = request.data.get('BMC_password')
        config_serializer = TestMachineSerializer(data=data_machine)
        if config_serializer.is_valid():
            self.perform_create(config_serializer)
            return json_response(config_serializer.data, status.HTTP_200_OK, '创建成功！')
        log.info('Machine数据存储错误 ：%s，'%config_serializer.errors)
        log.info('Machine存储数据为 ：%s，'%data_machine)
        return json_response(config_serializer.errors, status.HTTP_400_BAD_REQUEST, config_serializer.errors)

    def put(self, request, *args, **kwargs):
        if TestMachine.objects.get(BMC_IP=request.data.get('BMC_IP')):
            return json_response({}, status.HTTP_205_RESET_CONTENT, 'BMC_IP重复，请修改BMC_IP')
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
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
        if machine_data.queue_user:
            return json_response({}, status.HTTP_200_OK, '当前已存在申请人，请稍后')
        elif machine_data.owner == request.user.chinese_name:
            return json_response({}, status.HTTP_200_OK, '您正在使用无需申请')
        else:
            machine_data.queue_user = request.user.chinese_name
            machine_data.save()
            return json_response({}, status.HTTP_200_OK, '申请成功')

    def cancel_apply_use_machine(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        if machine_data.queue_user == request.user.chinese_name:
            machine_data.queue_user = None
            machine_data.save()
            return json_response({}, status.HTTP_200_OK, '取消申请成功')
        else:
            return json_response({}, status.HTTP_200_OK, '不可取消别人的申请')

    def modify_server(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        if not machine_data.server_IP == request.data.get('server_IP'):
            if TestMachine.objects.get(BMC_IP=request.data.get('server_IP')):
                return json_response({}, status.HTTP_205_RESET_CONTENT, '有server_IP重复，请修改server_IP')
        machine_data.server_IP = request.data.get('server_IP')
        machine_data.server_user_name = request.data.get('server_user_name')
        machine_data.server_password = request.data.get('server_password')
        new_server_password = request.data.get('new_server_password')
        new_iso_name = request.data.get('new_iso_name')
        machine_data.link_status = get_link_status(machine_data.BMC_IP, machine_data.BMC_user_name,
                                                   machine_data.BMC_password, machine_data.server_IP,
                                                   machine_data.server_user_name, machine_data.server_password)
        replacements = {}
        if new_iso_name == 'other(手动创建)' or not new_iso_name:
            ISO = None
        else:
            ISO = AdaptISO.objects.filter(ISO_name=new_iso_name).first()
            replacements['HTTP_ISO_PATH'] = ISO.http_address
            if ISO.arch_name == 'x86':
                replacements['BOOT_EFI'] = '/EFI/BOOT/BOOTX64.EFI'
            elif ISO.arch_name == 'aarch':
                replacements['BOOT_EFI'] = '/EFI/BOOT/BOOTAA64.EFI'
            replacements['KS_FILE_NAME'] = ISO.ks_file_name
            replacements['NETWORK_IP'] = machine_data.server_IP
            # ks文件中用户密码加密
            if new_server_password:
                replacements['PASSWORD'] = make_ks_password(new_server_password)
            else:
                return json_response({}, status.HTTP_200_OK,'重构系统请输入密码')

        if machine_data.owner == request.user.chinese_name:
            if new_iso_name:
                machine_data.iso_name = new_iso_name
            if ISO:
                update_auto_install(request.user, replacements)
                update_system(request.user, machine_data.server_IP, machine_data.server_user_name, machine_data.server_password, machine_data.machine_name, ISO.ISO_name, ISO.ks_file_name)
                machine_data.server_password = new_server_password
            machine_data.save()
            return json_response({}, status.HTTP_200_OK, '修改成功')
        elif not machine_data.owner:
            if machine_data.queue_user and machine_data.queue_user != request.user.chinese_name:
                return json_response({}, status.HTTP_200_OK, '当前申请人是 %s，请协商后在使用' % machine_data.queue_user)
            machine_data.owner = request.user.chinese_name
            machine_data.queue_user = None
            if new_iso_name:
                machine_data.iso_name = new_iso_name
            if ISO:
                update_auto_install(request.user, replacements)
                update_system(request.user, machine_data.server_IP, machine_data.server_user_name, machine_data.server_password, machine_data.machine_name, ISO.ISO_name, ISO.ks_file_name)
                machine_data.server_password = new_server_password
            machine_data.save()
            return json_response({}, status.HTTP_200_OK, '修改成功')
        else:
            return json_response({}, status.HTTP_200_OK, '不可修改他人的机器')

    def finished_using(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        if machine_data.owner == request.user.chinese_name:
            machine_data.owner = None
            machine_data.iso_name = None
            machine_data.link_status = None
            machine_data.task_status = None
            machine_data.save()
            return json_response({}, status.HTTP_200_OK, '使用完成状态修改成功')
        else:
            return json_response({}, status.HTTP_200_OK, '不可更改别人的使用状态')

    def update_status(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        machine_data.link_status = get_link_status(machine_data.BMC_IP, machine_data.BMC_user_name,
                                                   machine_data.BMC_password, machine_data.server_IP,
                                                   machine_data.server_user_name, machine_data.server_password)
        machine_data.save()
        return json_response({}, status.HTTP_200_OK, '更新状态完成')

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if not id or not TestMachine.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        test_case_data = TestMachine.objects.filter(id=id).first()
        if request.user.is_superuser or request.user.chinese_name == test_case_data.creator:
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            TestMachine.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只有创建人员才能删除该数据')
