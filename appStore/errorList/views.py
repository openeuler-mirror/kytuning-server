"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:19:26 2024 +0800
"""
from appStore.errorList.models import KytuningError
from appStore.errorList.serializers import ErroirListSerializer
from appStore.utils.common import LimsPageSet, json_response
from rest_framework import status, viewsets

import logging
log = logging.getLogger('mydjango') #这里的mydjango是settings中loggers里面对应的名字



class ErrorListViewSet(viewsets.ModelViewSet):
    """
    错误收集数据管理
    """
    queryset = KytuningError.objects.all()
    serializer_class = ErroirListSerializer
    pagination_class = LimsPageSet

    def list(self, request, *args, **kwargs):
        queryset = KytuningError.objects.all().order_by('-id')
        error_type = request.GET.get('error_type')
        test_type = request.GET.get('test_type')
        error_description = request.GET.get('error_description')
        error_log_excerpt = request.GET.get('error_log_excerpt')
        if not queryset:
            return json_response({}, status.HTTP_200_OK, '列表')
        if error_type:
            queryset = queryset.filter(error_type=error_type)
        if test_type:
            queryset = queryset.filter(test_type=test_type)
        if error_description:
            queryset = queryset.filter(error_description__contains=error_description)
        if error_log_excerpt:
            queryset = queryset.filter(error_log_excerpt__contains=error_log_excerpt)
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

    def create(self, request, *args, **kwargs):
        error_data = {}
        error_data['error_type'] = request.data.get('error_type')
        error_data['user_name'] = request.user.chinese_name
        error_data['test_type'] = request.data.get('test_type')
        error_data['error_description'] = request.data.get('error_description')
        error_data['error_log_excerpt'] = request.data.get('error_log_excerpt')
        error_data['error_log_path'] = request.data.get('error_log_path')
        error_data['solution'] = request.data.get('solution')
        serializer_error = ErroirListSerializer(data=error_data)
        if serializer_error.is_valid():
            self.perform_create(serializer_error)
            return json_response(serializer_error.data, status.HTTP_200_OK, '创建成功！')
        log.info('errorList数据存储错误 ：%s，', serializer_error.errors)
        log.info('errorList存储数据为 ：%s，', error_data)
        return json_response(serializer_error.errors, status.HTTP_400_BAD_REQUEST, serializer_error.errors)

    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        if not id or not KytuningError.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = KytuningError.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            error_data = KytuningError.objects.get(id=id)
            if not error_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            error_data.error_type = request.data.get('error_type')
            error_data.test_type = request.data.get('test_type')
            error_data.error_description = request.data.get('error_description')
            error_data.error_log_excerpt = request.data.get('error_log_excerpt')
            # error_data.error_log_path = request.data.get('error_log_path')
            error_data.solution = request.data.get('solution')
            error_data.save()
            return json_response({}, status.HTTP_200_OK, '修改成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许修改该数据')

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if not id or not KytuningError.objects.filter(id=id):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
        user_name = KytuningError.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            test_case_data = KytuningError.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            KytuningError.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许删除该数据')
