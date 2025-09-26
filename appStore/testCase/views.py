"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
import configparser
import os
import shutil
import subprocess
import time

import yaml
from django.http import HttpResponse, FileResponse

from appStore.testCase.models import TestCase
from appStore.testCase.serializers import TestCaseSerializer
from appStore.utils.common import test_case, json_response, get_error_message
from appStore.utils.constants import RESULT_LOG_FILE, RUN_KYTUNING_CONFIG_TEMP
from appStore.utils.customer_view import CusModelViewSet
from rest_framework import status


# Create your views here.

class TestCaseViewSet(CusModelViewSet):
    """
    测试用例数据管理
    """

    queryset = TestCase.objects.all().order_by('-id')
    serializer_class = TestCaseSerializer

    def list(self, request, *args, **kwargs):
        queryset = TestCase.objects.filter().all().order_by('-id')
        if not queryset:
            return json_response({}, status.HTTP_200_OK, '列表')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '测试完成')

    def do_test_case(self, request, *args, **kwargs):
        # 创建对应数据库
        data_test_case = {}
        data_test_case['user_name'] = request.user.chinese_name
        data_test_case['ip'] = request.data.get('test_ip')
        test_password = request.data.get('test_password')
        data_test_case['project_name'] = request.data.get('project_name')
        data_test_case['stream'] = request.data.get('stream')
        data_test_case['lmbench'] = request.data.get('lmbench')
        data_test_case['unixbench'] = request.data.get('unixbench')
        data_test_case['fio'] = request.data.get('fio')
        data_test_case['iozone'] = request.data.get('iozone')
        data_test_case['jvm2008'] = request.data.get('jvm2008')
        data_test_case['cpu2006'] = request.data.get('cpu2006')
        data_test_case['cpu2017'] = request.data.get('cpu2017')
        data_test_case['test_result'] = '运行中'
        data_test_case['result_log_name'] = RESULT_LOG_FILE + str(request.user) + '_' + str(time.time())

        test_case_names = []
        if int(data_test_case['stream']):
            test_case_names.append('stream')
        if int(data_test_case['lmbench']):
            test_case_names.append('lmbench')
        if int(data_test_case['unixbench']):
            test_case_names.append('unixbench')
        if int(data_test_case['fio']):
            test_case_names.append('fio')
        if int(data_test_case['iozone']):
            test_case_names.append('iozone')
        if int(data_test_case['jvm2008']):
            test_case_names.append('jvm2008')
        if int(data_test_case['cpu2006']):
            test_case_names.append('cpu2006')
        if int(data_test_case['cpu2017']):
            test_case_names.append('cpu2017')

        if not os.path.exists(RESULT_LOG_FILE):
            os.makedirs(RESULT_LOG_FILE)
        # 为每个用户创建一个临时的配置文件目录
        user_config_path = RUN_KYTUNING_CONFIG_TEMP + str(request.user)
        if not os.path.exists(user_config_path):
            os.makedirs(os.path.join(user_config_path, "conf"))
            os.makedirs(os.path.join(user_config_path, "yaml-base"))
        else:
            shutil.rmtree(user_config_path)
            os.makedirs(os.path.join(user_config_path, "conf"))
            os.makedirs(os.path.join(user_config_path, "yaml-base"))

        # 修改 conf/user.cfg文件
        with open(user_config_path + '/conf/user.cfg', 'w') as configfile:
            configfile.write('rk_benchmark="{}"\n'.format(' '.join(test_case_names)))
            configfile.write('project_name={}\n'.format(data_test_case['project_name']))
            configfile.write('upload=true\n')
            configfile.write('username={}\n'.format(str(request.user)))
            configfile.write('password={}\n'.format(request.data.get('user_password')))

        # 将配置数据写入YAML文件
        # 第一代的版本就先只支持迭代次数
        if int(data_test_case['stream']):
            stream_yaml = request.data.get('yaml')['stream'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['stream'])))
            with open(user_config_path + '/yaml-base/stream-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(stream_yaml)
        if int(data_test_case['lmbench']):
            lmbench_yaml = request.data.get('yaml')['lmbench'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['lmbench'])))
            with open(user_config_path + '/yaml-base/lmbench-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(lmbench_yaml)
        if int(data_test_case['unixbench']):
            unixbench_yaml = request.data.get('yaml')['unixbench'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['unixbench'])))
            with open(user_config_path + '/yaml-base/unixbench-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(unixbench_yaml)
        if int(data_test_case['fio']):
            fio_yaml = request.data.get('yaml')['fio'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['fio'])))
            with open(user_config_path + '/yaml-base/fio-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(fio_yaml)
        if int(data_test_case['iozone']):
            iozone_yaml = request.data.get('yaml')['iozone'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['iozone'])))
            with open(user_config_path + '/yaml-base/iozone-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(iozone_yaml)
        if int(data_test_case['jvm2008']):
            jvm2008_yaml = request.data.get('yaml')['jvm2008'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['jvm2008'])))
            with open(user_config_path + '/yaml-base/jvm2008-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(jvm2008_yaml)
        if int(data_test_case['cpu2006']):
            cpu2006_yaml = request.data.get('yaml')['cpu2006'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['cpu2006'])))
            with open(user_config_path + '/yaml-base/cpu2006-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(cpu2006_yaml)
            cpu2006_loongarch64_yaml = request.data.get('yaml')['cpu2006_loongarch64'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['cpu2006_loongarch64'])))
            with open(user_config_path + '/yaml-base/cpu2006-loongarch64-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(cpu2006_loongarch64_yaml)
        if int(data_test_case['cpu2017']):
            cpu2017_yaml = request.data.get('yaml')['cpu2017'].replace('maxiterations:  1', 'maxiterations: %d' % (
                int(data_test_case['cpu2017'])))
            with open(user_config_path + '/yaml-base/cpu2017-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(cpu2017_yaml)
        # return json_response({}, status.HTTP_400_BAD_REQUEST,{})
        # 创建请求测试数据
        serializer_test_case = TestCaseSerializer(data=data_test_case)
        if serializer_test_case.is_valid():
            self.perform_create(serializer_test_case)
            test_case_id = serializer_test_case.data['id']
        else:
            return json_response(serializer_test_case.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer_test_case))
        # 运行测试
        return_result = test_case(data_test_case['ip'], 'root', test_password, test_case_names,  user_config_path, data_test_case['result_log_name'])
        if return_result.stderr and return_result.stderr != '\nAuthorized users only. All activities may be monitored and reported.\n':
            TestCase.objects.filter(id=test_case_id).update(test_result=return_result.stderr)
            return json_response('', status.HTTP_204_NO_CONTENT, return_result.stderr)
        else:
            TestCase.objects.filter(id=test_case_id).update(test_result='测试完成')
            return json_response('', status.HTTP_200_OK, '测试完成')

    def delete(self, request):
        id = request.data.get('id', None)
        if not id or not TestCase.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = TestCase.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            test_case_data = TestCase.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            # 删除数据
            TestCase.objects.filter(id=id).delete()
            # 删除日志文件
            subprocess.run("rm -rf " + str(TestCase.objects.filter(id=id).first().result_log_name) + '.tar', shell=True)
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许删除该数据')

    def down_message(self, request, *args, **kwargs):
        test_case_id = request.GET.get('id')
        result_log_name = TestCase.objects.filter(id=test_case_id).first().result_log_name
        # 检查文件是否存在
        log_file_path = result_log_name+'.tar'
        if not os.path.exists(log_file_path):
            return HttpResponse('文件不存在', status=404)
        # 使用FileResponse对象将文件作为HTTP响应发送回前端
        return FileResponse(open(log_file_path, 'rb'), as_attachment=True,status=200)