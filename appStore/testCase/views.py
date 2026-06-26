"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""

import os
import time
import shutil
import logging
import subprocess
from rest_framework import status, viewsets
from django.http import HttpResponse, FileResponse, HttpRequest
# Create your views here.
from appStore.testCase.models import TestCase
from appStore.testCase.serializers import TestCaseSerializer
from appStore.testMachine.models import TestMachine
from appStore.utils.timed_tasks import auto_install_system
from appStore.utils.common import json_response
from appStore.utils.constants import RESULT_LOG_FILE, RUN_KYTUNING_CONFIG_TEMP, TOOLS_URL, KYTUNING_WEB_URL, SECRET, LANXIN_URL
from appStore.utils.subprocess import test_case, stop_test_task

log = logging.getLogger('kytuninglog')


class TestCaseViewSet(viewsets.ModelViewSet):
    """
    测试用例数据管理
    """
    queryset = TestCase.objects.all().order_by('-id')
    serializer_class = TestCaseSerializer

    def list(self, request, *args, **kwargs):
        """
        测试列表展示功能
        """
        queryset = TestCase.objects.filter().all().order_by('-id')
        if not queryset:
            return json_response({}, status.HTTP_204_NO_CONTENT, '未获取到数据')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '获取列表完成')

    def do_test_case(self, request, *args, **kwargs):
        """
        执行性能测试
        """
        data_test_case = {}
        data_test_case['user_name'] = request.user.chinese_name
        data_test_case['ip'] = request.data.get('test_ip')
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
        data_test_case['test_type'] = request.data.get('test_type')
        data_test_case['result_log_name'] = RESULT_LOG_FILE + str(request.user) + '_' + str(time.time())
        if not data_test_case['ip']:
            return json_response({}, status.HTTP_204_NO_CONTENT, '未填写IP信息')

        if not request.data.get('yaml'):
            return json_response({}, status.HTTP_204_NO_CONTENT, '请刷新页面重试')

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
        # 将配置数据写入YAML文件
        if int(data_test_case['stream']):
            stream_yaml = request.data.get('yaml')['stream'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['stream'])))
            with open(user_config_path + '/yaml-base/stream-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(stream_yaml)
        if int(data_test_case['lmbench']):
            lmbench_yaml = request.data.get('yaml')['lmbench'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['lmbench'])))
            with open(user_config_path + '/yaml-base/lmbench-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(lmbench_yaml)
        if int(data_test_case['unixbench']):
            unixbench_yaml = request.data.get('yaml')['unixbench'].replace('maxiterations:  1',
                                                                           'maxiterations: %d' % (int(data_test_case['unixbench'])))
            with open(user_config_path + '/yaml-base/unixbench-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(unixbench_yaml)
        if int(data_test_case['fio']):
            fio_yaml = request.data.get('yaml')['fio'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['fio'])))
            with open(user_config_path + '/yaml-base/fio-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(fio_yaml)
        if int(data_test_case['iozone']):
            iozone_yaml = request.data.get('yaml')['iozone'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['iozone'])))
            with open(user_config_path + '/yaml-base/iozone-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(iozone_yaml)
        if int(data_test_case['jvm2008']):
            jvm2008_yaml = request.data.get('yaml')['jvm2008'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['jvm2008'])))
            with open(user_config_path + '/yaml-base/jvm2008-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(jvm2008_yaml)
        if int(data_test_case['cpu2006']):
            cpu2006_yaml = request.data.get('yaml')['cpu2006'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['cpu2006'])))
            with open(user_config_path + '/yaml-base/cpu2006-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(cpu2006_yaml)
            cpu2006_loongarch64_yaml = (request.data.get('yaml')['cpu2006_loongarch64'].replace(
                'maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['cpu2006']))))
            with open(user_config_path + '/yaml-base/cpu2006-loongarch64-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(cpu2006_loongarch64_yaml)
        if int(data_test_case['cpu2017']):
            cpu2017_yaml = request.data.get('yaml')['cpu2017'].replace('maxiterations:  1', 'maxiterations: %d' % (int(data_test_case['cpu2017'])))
            with open(user_config_path + '/yaml-base/cpu2017-base.yaml', 'w', encoding='UTF-8') as fp:
                fp.write(cpu2017_yaml)

        if data_test_case['test_type'] == '监控测试':
            # 监控测试
            # todo 一条监控测试对应多条测试数据
            if request.user.is_staff:
                data_test_case['kojifile_addr'] = request.data.get('kojifile_addr')
                data_test_case['iso_name'] = request.data.get('iso_name')
                ip_list = data_test_case['ip']
                for ip in ip_list:
                    data_test_case['ip'] = ip
                    data_test_case['project_name'] = '定时任务-{}-{}'.format(ip, request.data.get('iso_name'))
                    # 判断是否存在owner，如果存在则增加queue_user
                    TestMachine_ = TestMachine.objects.filter(server_IP=ip).first()
                    if TestMachine_.owner == request.user.chinese_name:
                        return json_response('', status.HTTP_401_UNAUTHORIZED, '您正在使用请排查')
                    if TestMachine_.owner or TestMachine_.queue_user:
                        TestMachine_.queue_user = TestMachine_.queue_user + ',' + request.user.chinese_name
                        # TestMachine_.save()
                    else:
                        # 创建测试数据
                        serializer_test_case = TestCaseSerializer(data=data_test_case)
                        if serializer_test_case.is_valid():
                            self.perform_create(serializer_test_case)
                            test_case_id = serializer_test_case.data['id']
                            # 增加测试ID数据
                            # 修改 conf/kytuning.cfg文件
                            with open(user_config_path + '/conf/kytuning.cfg', 'w') as configfile:
                                configfile.write('tools_server_url="{}"\n'.format(TOOLS_URL))
                                configfile.write('rk_benchmark="{}"\n'.format(' '.join(test_case_names)))
                                configfile.write('project_name={}\n'.format(data_test_case['project_name']))
                                configfile.write('project_message={}\n'.format(request.data.get('project_message')))
                                configfile.write('kytuning_web_url={}\n'.format(KYTUNING_WEB_URL))
                                configfile.write('upload=true\n')
                                configfile.write('token={}\n'.format(request.META.get('HTTP_AUTHORIZATION')))
                                configfile.write('SECRET={}\n'.format(SECRET))
                                configfile.write('LANXIN_URL={}\n'.format(LANXIN_URL))
                                configfile.write('test_case_id={}\n'.format(test_case_id))
                            # 自动化安装所需操作系统，监控系统是否安装完成，及自动化测试
                            auto_install_system(TestMachine_, request, ip, data_test_case['iso_name'], data_test_case['kojifile_addr'],
                                                user_config_path)
                        else:
                            log.info('testCase数据存储错误 ：%s，' % (serializer_test_case.errors))
                            log.info('testCase存储数据为 ：%s，' % data_test_case)
                            return json_response(serializer_test_case.errors, status.HTTP_400_BAD_REQUEST, serializer_test_case.errors)
                return json_response('', status.HTTP_200_OK, '自动化安装任务发派成功')
            else:
                return json_response('', status.HTTP_401_UNAUTHORIZED, '只有管理员才能创建作监控')
        else:
            # 其它测试
            # 创建请求测试数据
            serializer_test_case = TestCaseSerializer(data=data_test_case)
            if serializer_test_case.is_valid():
                self.perform_create(serializer_test_case)
                test_case_id = serializer_test_case.data['id']
                # 修改 conf/kytuning.cfg文件
                with open(user_config_path + '/conf/kytuning.cfg', 'w') as configfile:
                    configfile.write('tools_server_url="{}"\n'.format(TOOLS_URL))
                    configfile.write('rk_benchmark="{}"\n'.format(' '.join(test_case_names)))
                    configfile.write('project_name={}\n'.format(data_test_case['project_name']))
                    configfile.write('project_message={}\n'.format(request.data.get('project_message')))
                    configfile.write('kytuning_web_url={}\n'.format(KYTUNING_WEB_URL))
                    configfile.write('upload=true\n')
                    configfile.write('token={}\n'.format(request.META.get('HTTP_AUTHORIZATION')))
                    configfile.write('test_case_id={}\n'.format(test_case_id))
            else:
                log.info('testCase数据存储错误 ：%s，' % (serializer_test_case.errors))
                log.info('testCase存储数据为 ：%s，' % data_test_case)
                return json_response(serializer_test_case.errors, status.HTTP_400_BAD_REQUEST, serializer_test_case.errors)

            """保存至配置管理数据库"""
            from appStore.userConfig.views import UserConfigViewSet
            request_user_config = HttpRequest()
            request_user_config.method = 'POST'
            request.data['is_send_config'] = True
            request_user_config = request
            UserConfigViewSet = UserConfigViewSet()
            UserConfigViewSet.create(request=request_user_config, *args, **kwargs)

            # 运行测试
            TestMachine_ = TestMachine.objects.filter(server_IP=data_test_case['ip']).first()
            if TestMachine_.owner != request.user.chinese_name:
                return json_response('', status.HTTP_401_UNAUTHORIZED, '用户只能使用自己的机器测试')
            try:
                return_result = test_case(data_test_case['ip'], TestMachine_.server_user_name, TestMachine_.server_password,
                                          test_case_names, user_config_path, data_test_case['result_log_name'])
                if return_result.stderr and return_result.stderr != '\nAuthorized users only. All activities may be monitored and reported.\n':
                    log.info('测试的测试数据ID是：%s，测试的返回结果return_result是：%s' % (test_case_id, str(return_result)))
                    log.info('测试的测试数据ID是：%s，测试的返回结果return_result.stderr是：%s' % (test_case_id, str(return_result.stderr)))
                    TestCase.objects.filter(id=test_case_id).update(test_result=return_result.stderr)
                    return json_response('', status.HTTP_204_NO_CONTENT, return_result.stderr)
                else:
                    # 因为上传数据是测试脚本的一部分，如果成功就已经修改过状态了。
                    if TestCase.objects.filter(id=test_case_id).first().test_result != '测试完成':
                        TestCase.objects.filter(id=test_case_id).update(test_result='测试异常')
                    return json_response('', status.HTTP_200_OK, '测试完成')
            except Exception as e:
                log.error('测试的测试数据ID是：%s，发生的异常是：%s', test_case_id, str(e))
                TestCase.objects.filter(id=test_case_id).update(test_result='测试异常')
                return json_response('', status.HTTP_500_INTERNAL_SERVER_ERROR, '发生异常，详细信息请查看日志')

    def delete(self, request, *args, **kwargs):
        """
        删除测试数据信息
        """
        id = request.data.get('id', None)
        if not id or not TestCase.objects.filter(id=id):
            return json_response({}, status.HTTP_400_BAD_REQUEST, '请传递正确的测试id')
        user_name = TestCase.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            test_case_data = TestCase.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_204_NO_CONTENT, '未获取到数据')
            if not TestCase.objects.get(id=id).is_error:
                # 删除日志文件
                subprocess.run("rm -rf " + str(TestCase.objects.filter(id=id).first().result_log_name) + '.tar', shell=True)
            # 删除数据
            TestCase.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_401_UNAUTHORIZED, '此用户不允许删除该数据')

    def down_message(self, request, *args, **kwargs):
        """
        下载日志信息
        """
        result_log_name = request.GET.get('result_log_name')
        # 检查文件是否存在
        log_file_path = result_log_name + '.tar'
        if not os.path.exists(log_file_path):
            return HttpResponse('文件不存在', status=404)
        # 使用FileResponse对象将文件作为HTTP响应发送回前端
        return FileResponse(open(log_file_path, 'rb'), as_attachment=True, status=200)

    def stop_test(self, request, *args, **kwargs):
        """
        终止测试
        """
        id = request.data.get('test_id', None)
        if not id or not TestCase.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = TestCase.objects.filter(id=id).first().user_name
        if request.user.chinese_name == user_name:
            test_case_data = TestCase.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '未查到对应的测试任务')
            server_ip = TestCase.objects.get(id=id).ip
            machine_data = TestMachine.objects.get(server_IP=server_ip)
            stop_test_task(server_ip, machine_data.server_user_name, machine_data.server_password)
            TestCase.objects.filter(id=id).update(test_result='终止测试')
            return json_response({}, status.HTTP_200_OK, '终止测试成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只能终止自己的测试任务')
