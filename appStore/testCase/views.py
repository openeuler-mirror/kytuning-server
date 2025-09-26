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

    def do_test_case1(self, request, *args, **kwargs):
        # 创建对应数据库
        data_test_case = {}
        data_test_case['user_name'] = request.user.chinese_name
        data_test_case['ip'] = request.POST.get('test_ip')
        test_password = request.POST.get('test_password')
        data_test_case['project_name'] = request.POST.get('project_name')
        data_test_case['stream'] = request.POST.get('stream')
        data_test_case['lmbench'] = request.POST.get('lmbench')
        data_test_case['unixbench'] = request.POST.get('unixbench')
        data_test_case['fio'] = request.POST.get('fio')
        data_test_case['iozone'] = request.POST.get('iozone')
        data_test_case['jvm2008'] = request.POST.get('jvm2008')
        data_test_case['cpu2006'] = request.POST.get('cpu2006')
        data_test_case['cpu2017'] = request.POST.get('cpu2017')
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
        # todo 密码怎么解决，从数据库中获取在解密？

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
            configfile.write('password={}\n'.format(request.POST.get('password')))

        # 将配置数据写入YAML文件
        # 第一代的版本就先只支持迭代次数
        if int(data_test_case['stream']):
            # 这个是获取用户的全部配置直接写入的方式
            # with open(user_config + '/yaml-base/stream-base.yaml', 'w') as f:
            #     yaml.dump(stream_base_yaml, f)
            # 读取YAML文件中的数据
            with open('./yaml-base/stream-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            # 根据需要修改配置数据
            config['maxiterations'] = int(data_test_case['stream'])
            # 将修改后的数据写回YAML文件
            with open(user_config_path + '/yaml-base/stream-base.yaml', 'w') as f:
                yaml.dump(config, f, default_flow_style=False)
        if int(data_test_case['lmbench']):
            with open('./yaml-base/lmbench-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            config['maxiterations'] = int(data_test_case['lmbench'])
            with open(user_config_path + '/yaml-base/lmbench-base.yaml', 'w') as f:
                yaml.dump(config, f, default_flow_style=False)
        if int(data_test_case['unixbench']):
            with open('./yaml-base/unixbench-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            config['maxiterations'] = int(data_test_case['unixbench'])
            with open(user_config_path + '/yaml-base/unixbench-base.yaml', 'w') as f:
                yaml.dump(config, f)
        if int(data_test_case['fio']):
            with open('./yaml-base/fio-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            config['maxiterations'] = int(data_test_case['fio'])
            with open(user_config_path + '/yaml-base/fio-base.yaml', 'w') as f:
                yaml.dump(config, f)
        if int(data_test_case['iozone']):
            with open('./yaml-base/iozone-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            config['maxiterations'] = int(data_test_case['iozone'])
            with open(user_config_path + '/yaml-base/iozone-base.yaml', 'w') as f:
                yaml.dump(config, f)
        if int(data_test_case['jvm2008']):
            # 读取YAML文件中的数据
            with open('./yaml-base/jvm2008-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            # 根据需要修改配置数据
            config['maxiterations'] = int(data_test_case['jvm2008'])
            # 将修改后的数据写回YAML文件
            with open(user_config_path + '/yaml-base/jvm2008-base.yaml', 'w') as f:
                yaml.dump(config, f)
        if int(data_test_case['cpu2006']):
            # todo cpu2006-loongarch64-base.yaml这个怎么处理
            # 读取YAML文件中的数据
            with open('./yaml-base/cpu2006-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            # 根据需要修改配置数据
            config['maxiterations'] = int(data_test_case['cpu2006'])
            # 将修改后的数据写回YAML文件
            with open(user_config_path + '/yaml-base/cpu2006-base.yaml', 'w') as f:
                yaml.dump(config, f)
        if int(data_test_case['cpu2017']):
            # 读取YAML文件中的数据
            with open('./yaml-base/cpu2017-base.yaml', 'r') as f:
                config = yaml.full_load(f)
            # 根据需要修改配置数据
            config['maxiterations'] = int(data_test_case['cpu2017'])
            # 将修改后的数据写回YAML文件
            with open(user_config_path + '/yaml-base/cpu2017-base.yaml', 'w') as f:
                yaml.dump(config, f)
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