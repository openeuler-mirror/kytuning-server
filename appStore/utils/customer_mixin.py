"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 10:58:08 2024 +0800
"""
#!/usr/bin/env python
# encoding: utf-8
"""
@author: morgan
@time: 8/7/19 4:26 PM
"""
from rest_framework import status

from appStore.utils.common import json_response, get_error_message, list_response


class CusCreateModelMixin(object):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return json_response(serializer.data, status.HTTP_200_OK, '创建成功！')
        return json_response(serializer.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer))

    def perform_create(self, serializer):
        serializer.save()


class CusListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            page = self.paginate_queryset(queryset)
        except:
            return json_response({}, status.HTTP_200_OK, '计划列表获取为空，可能是page/page_size参数不对')
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = serializer.data
            result = self.get_paginated_response(result)
            return list_response(result, status.HTTP_200_OK, '列表')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '列表')


class CusRetrieveModelMixin(object):
    """
    Retrieve a model instance.单个
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return json_response(serializer.data, status.HTTP_200_OK, '获取成功！')


class CusUpdateModelMixin(object):
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            return json_response(serializer.data, status.HTTP_200_OK, '更新成功！')
        return json_response(serializer.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer))

    def perform_update(self, serializer):
        serializer.save()


class CusDestroyModelMixin(object):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return json_response(True, status.HTTP_200_OK, '删除成功！')

    def perform_destroy(self, instance):
        instance.delete()
