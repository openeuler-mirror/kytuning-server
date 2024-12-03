"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 10:00:37 2024 +0800
"""
#!/usr/bin/env python
# encoding: utf-8
"""
公共函数
@author: Wqz
@time: 11/6/19 4:33 PM
"""
from django.core.paginator import Paginator, EmptyPage
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import pagination, status
from rest_framework.permissions import BasePermission
from appStore.utils import constants


def return_time(test_time):
    time = test_time.split('-')[0] + '-' + test_time.split('-')[1] + '-' + test_time.split('-')[2] + ' ' + \
               test_time.split('-')[3] + ':' + test_time.split('-')[4] + ':' + test_time.split('-')[5]
    return time


def json_response(data=None, code=None, message=None):
    """
    返回自定义格式数据
    :param data:
    :param code:
    :param message:
    :return:
    """
    res = {
        'data': data,
        'code': code,
        'message': message
    }
    return JsonResponse(res)


def list_response(result, code, message):
    """
    :param result:
    :param code:
    :param message:
    :return:
    """
    res = {}
    if result.data:
        res['data'] = result.data
    if code:
        res['code'] = code
    if message:
        res['message'] = message
    return JsonResponse(res)


def model_to_dict_myself(queryset, **kwargs):
    """
        返回model_to_dict转换的字段
        """
    if not queryset:
        return {}
    data = []
    if 'exclude' in kwargs.keys():
        for query in queryset:
            dict = model_to_dict(query, exclude=kwargs['exclude'])
            data.append(dict)
    elif 'fields' in kwargs.keys():
        for query in queryset:
            dict = model_to_dict(query, fields=kwargs['fields'])
            data.append(dict)
    else:
        for query in queryset:
            dict = model_to_dict(query)
            data.append(dict)
    return data


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
        'is_superuser': user.is_superuser,
        'is_staff': user.is_staff,
        'code': 200,
    }


def get_error_message(serializer):
    """
    返回错误信息
    :param serializer:
    :return:
    """
    for _, error in serializer.errors.items():
        return error[0]


class LimsPageSet(pagination.PageNumberPagination):
    """
    分页设置
    分页样式  ?page=1&page_size=10
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = 'page'


# class ZbmPermission(BasePermission):
#     """
#     管理员和超级管理员可以对系统进行各种
#     权限操作，普通用户只能对信息进行查看
#     """
#     def has_permission(self, request, view):
#         try:
#             user_type = request.user.user_type_choices
#             if user_type == 2 or request.user.is_superuser or request.method == 'GET':
#                 return True
#             return False
#         except:
#             pass


def get_page(data, objs):
    """
    进行分页
    :param data:
    :param objs:
    :return:
    """
    try:
        page = int(data.get('page', 1))
        page_size = int(data.get('page_size', 5))
    except Exception as e:
        return json_response({}, status.HTTP_400_BAD_REQUEST, '参数类型不对')
    paginator = Paginator(objs, page_size)  # 设置每一页显示几条  创建一个panginator对象
    try:
        current_num = page  # 当在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        list = paginator.page(current_num)
    except EmptyPage:
        list = paginator.page(1)  # 当输入的page是不存在的时候就会报错
    return list
