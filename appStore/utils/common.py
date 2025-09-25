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
import subprocess
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from rest_framework import pagination, status


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

# 定义远程服务器的IP地址、用户名和密码
remote_host = 'IP地址'
remote_username = '用户名'
remote_password = '密码'
def test_case(remote_host,remote_username,remote_password):
    # 使用scp命令将安装包发送到远程服务器
    scp_command = f'sshpass -p {remote_password} scp -o StrictHostKeyChecking=no -r /root/run_kytuning-ffdev/ {remote_username}@{remote_host}:/root/run_kytuning-ffdev'
    return_result = subprocess.run(scp_command, shell=True)
    if return_result.returncode == 5:
        return_result.stderr = "请确认测试机器的账号密码是否正确"
        return return_result
    elif return_result.returncode:
        return_result.stderr = "scp 命令出错"
        return return_result

    # 在远程服务器上运行脚本
    ssh_command = f'sshpass -p {remote_password} ssh {remote_username}@{remote_host} "cd /root/run_kytuning-ffdev/;sh /root/run_kytuning-ffdev/run.sh"'
    return_result = subprocess.run(ssh_command, stderr=subprocess.PIPE, encoding='utf-8', shell=True)
    return return_result