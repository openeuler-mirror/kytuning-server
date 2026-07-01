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
from appStore.testCase.models import TestCase
from appStore.testMachine.models import TestMachine
from appStore.testMachine.serializers import TestMachineSerializer
from appStore.utils.autoTest.send_url_message import send_lanxin_message
from appStore.utils.common import json_response, make_ks_password
from appStore.utils.constants import DNS, RUN_KYTUNING_CONFIG_TEMP
from appStore.utils.subprocess import check_disk_size, get_link_status, update_system, update_auto_install
from appStore.utils.timed_tasks import auto_install_system

log = logging.getLogger('kytuninglog')


class TestMachineViewSet(viewsets.ModelViewSet):
    """
    测试机器数据管理
    """
    queryset = TestMachine.objects.all().order_by('-id')
    serializer_class = TestMachineSerializer

    def list(self, request, *args, **kwargs):
        if (request.GET.get('search_by_name', None)):
            queryset = TestMachine.objects.filter(owner=request.user.chinese_name).order_by('-id')
        else:
            queryset = TestMachine.objects.all().order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

    def create(self, request, *args, **kwargs):
        if TestMachine.objects.filter(BMC_IP=request.data.get('BMC_IP')):
            return json_response({}, status.HTTP_400_BAD_REQUEST, 'BMC_IP重复，请修改BMC_IP')
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
        log.info('Machine数据存储错误 ：%s，' % config_serializer.errors)
        log.info('Machine存储数据为 ：%s，' % data_machine)
        return json_response(config_serializer.errors, status.HTTP_400_BAD_REQUEST, config_serializer.errors)

    def put(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_204_NO_CONTENT, '未获取到数据')
        if not machine_data.BMC_IP == request.data.get('BMC_IP'):
            if TestMachine.objects.filter(BMC_IP=request.data.get('BMC_IP')):
                return json_response({}, status.HTTP_400_BAD_REQUEST, 'BMC_IP重复，请修改BMC_IP')
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
            return json_response({}, status.HTTP_205_RESET_CONTENT, '未获取到数据')
        if machine_data.queue_user:
            # 允许多人排队
            if not request.user.chinese_name in machine_data.queue_user.split(','):
                if len(machine_data.queue_user.split(',')) < 5:
                    machine_data.queue_user = machine_data.queue_user + ',' + request.user.chinese_name
                    machine_data.save()
                    return json_response({}, status.HTTP_200_OK, '申请成功')
                else:
                    return json_response({}, status.HTTP_205_RESET_CONTENT, '当前已有5人排队，等待时间过长请更换机器')
            return json_response({}, status.HTTP_205_RESET_CONTENT, '您已经申请成功，无需重复申请')
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
        if request.user.chinese_name in machine_data.queue_user.split(','):
            # 删除当前人员
            queue_names = [queue_name for queue_name in machine_data.queue_user.split(',') if queue_name != request.user.chinese_name]
            machine_data.queue_user = ','.join(queue_names)
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
            if TestMachine.objects.filter(server_IP=request.data.get('server_IP')):
                return json_response({}, status.HTTP_205_RESET_CONTENT, '有server_IP重复，请修改server_IP')
        machine_data.server_IP = request.data.get('server_IP')
        machine_data.server_user_name = request.data.get('server_user_name')
        machine_data.server_password = request.data.get('server_password')
        new_server_password = request.data.get('new_server_password')
        new_iso_name = request.data.get('new_iso_name')
        machine_data.link_status = get_link_status(machine_data.BMC_IP, machine_data.BMC_user_name, machine_data.BMC_password, machine_data.server_IP,
                                                   machine_data.server_user_name, machine_data.server_password)
        replacements = {}
        # 补充需要替换脚本文件的内容
        if new_iso_name == 'other(手动创建)' or not new_iso_name:
            ISO = None
        else:
            # 检查磁盘空间是否充足
            remaining_disk_space = check_disk_size(machine_data.server_IP, machine_data.server_user_name, machine_data.server_password)
            if not remaining_disk_space:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '请更新服务器状态，查看账号密码是否正确')
            if not request.data.get('clear_part'):
                if int(remaining_disk_space) <= int(request.data.get('root_size')) + int(request.data.get('swap_size')) + 1 + 1:
                    return json_response({}, status.HTTP_205_RESET_CONTENT,
                                         '磁盘空间不足请重新设置;当前磁盘空间为：%sG;' % (int(remaining_disk_space) - 2))
            if not request.data.get('root_size') or not isinstance(request.data.get('root_size'), (int, float)):
                return json_response({}, status.HTTP_205_RESET_CONTENT, '请输入根文件路径大小')
            else:
                replacements['root_size'] = request.data.get('root_size')
            if not request.data.get('swap_size') or not isinstance(request.data.get('swap_size'), (int, float)):
                return json_response({}, status.HTTP_205_RESET_CONTENT, '请输入交换空间大小')
            else:
                replacements['swap_size'] = request.data.get('swap_size')
            # ks文件中用户密码加密
            if new_server_password:
                replacements['PASSWORD'] = make_ks_password(new_server_password)
            else:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '重构系统请输入密码')
            ISO = AdaptISO.objects.filter(ISO_name=new_iso_name).first()
            replacements['HTTP_ISO_PATH'] = ISO.http_address
            if ISO.arch_name == 'x86':
                replacements['BOOT_EFI'] = '/EFI/BOOT/BOOTX64.EFI'
            elif ISO.arch_name == 'aarch':
                replacements['BOOT_EFI'] = '/EFI/BOOT/BOOTAA64.EFI'
            replacements['KS_FILE_NAME'] = ISO.ks_file_name
            replacements['NETWORK_IP'] = machine_data.server_IP
            replacements['DNS'] = DNS
            replacements['clear_part'] = request.data.get('clear_part')
            replacements['kernel510'] = request.data.get('kernel_type')
        if machine_data.owner == request.user.chinese_name:
            if new_iso_name:
                machine_data.iso_name = new_iso_name
            if ISO:
                update_auto_install(request.user, replacements)
                update_system(request.user, machine_data.server_IP, machine_data.server_user_name, machine_data.server_password,
                              machine_data.machine_name, ISO.ISO_name, ISO.ks_file_name)
                machine_data.server_password = new_server_password
            machine_data.save()
            return json_response({}, status.HTTP_200_OK, '修改成功')
        elif not machine_data.owner:
            # 判断是不是第一个申请人
            if machine_data.queue_user and (machine_data.queue_user.split(',')[0] != request.user.chinese_name and machine_data.queue_user.split(',')[0] != 'root'):
                return json_response({}, status.HTTP_205_RESET_CONTENT, '当前申请人是 %s，请协商后在使用' % machine_data.queue_user)
            machine_data.owner = request.user.chinese_name
            # 删除当前人员
            if machine_data.queue_user:
                queue_names = [queue_name for queue_name in machine_data.queue_user.split(',') if queue_name != request.user.chinese_name]
                machine_data.queue_user = ','.join(queue_names)
            if new_iso_name:
                machine_data.iso_name = new_iso_name
            if ISO:
                update_auto_install(request.user, replacements)
                update_system(request.user, machine_data.server_IP, machine_data.server_user_name, machine_data.server_password,
                              machine_data.machine_name, ISO.ISO_name, ISO.ks_file_name)
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
            if machine_data.queue_user:
                if machine_data.queue_user.split(',')[0] == 'root':
                    # 执行自动化安装操作系统，自动化测试等。
                    user_config_path = RUN_KYTUNING_CONFIG_TEMP + 'root'
                    test_case = TestCase.objects.filter(ip=machine_data.server_IP).filter(test_type='监控测试').filter(test_result='排队中').last()
                    auto_install_system(machine_data, request, machine_data.server_IP, test_case.iso_name, test_case.kojifile_addr, user_config_path)
                content = "BMC设备IP为：{} 的机器已完成使用，请您确认".format(machine_data.BMC_IP)
                # send_lanxin_message(machine_data.queue_user.split(',')[0], content)
            return json_response({}, status.HTTP_200_OK, '使用完成状态修改成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '不可更改别人的使用状态')

    def update_status(self, request, *args, **kwargs):
        machine_id = request.data.get('id')
        machine_data = TestMachine.objects.get(id=machine_id)
        if not machine_id or not machine_data:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
        machine_data.link_status = get_link_status(machine_data.BMC_IP, machine_data.BMC_user_name, machine_data.BMC_password,
                                                   machine_data.server_IP, machine_data.server_user_name, machine_data.server_password)
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
