"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
from appStore.testCase.models import TestCase
from appStore.testCase.serializers import TestCaseSerializer
from appStore.utils.common import test_case, json_response, get_error_message
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
        # remote_host = '172.29.220.91'
        # remote_username = 'root'
        # remote_password = 'Kylin@123321wqz'

        data_test_case['project_name'] = request.POST.get('project_name')
        data_test_case['user_name'] = request.POST.get('remote_username')
        remote_password = request.POST.get('remote_password')
        data_test_case['ip'] = request.POST.get('remote_host')
        data_test_case['stream'] = request.POST.get('stream')
        data_test_case['lmbench'] = request.POST.get('lmbench')
        data_test_case['unixbench'] = request.POST.get('unixbench')
        data_test_case['fio'] = request.POST.get('fio')
        data_test_case['iozone'] = request.POST.get('iozone')
        data_test_case['jvm2008'] = request.POST.get('jvm2008')
        data_test_case['cpu2006'] = request.POST.get('cpu2006')
        data_test_case['cpu2017'] = request.POST.get('cpu2017')
        data_test_case['test_result'] = ''

        serializer_test_case = TestCaseSerializer(data=data_test_case)
        if serializer_test_case.is_valid():
            self.perform_create(serializer_test_case)
        else:
            return json_response(serializer_test_case.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer_test_case))
        #运行测试
        # return_result = test_case(remote_host,remote_username,remote_password)
        # print(return_result, 111)
        # print(type(return_result), 222)
        # print(return_result.stdout, 222)
        # print(return_result.stderr, 333)
        # print(return_result.returncode, 444)
        # if return_result.returncode:
        #     return json_response('', status.HTTP_400_BAD_REQUEST, return_result.stderr)
        return json_response('', status.HTTP_200_OK, '测试完成')