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
import glob
import os
import tarfile
import subprocess
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from rest_framework import pagination, status

from appStore.utils.constants import RESULT_LOG_FILE


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


def test_case(test_ip, test_username, test_password, test_case_names, user_config_path, result_log_name):
    """

    :param test_ip: 测试机器的ip
    :param test_username: 测试机器的用户名
    :param test_password: 测试机器的密码
    :param result_log_name: 存放日志文件路径
    :param test_case_names: 需要哪几项
    :param run_kytuning_temp: run_kytuning存放的临时文件
    :return:
    """
    # 下载run_kytuning代码
    wget_command = f'sshpass -p {test_password} ssh {test_username}@{test_ip} "rm -rf /root/run_kytuning-ffdev/;wget -O /root/run_kytuning-ffdev.zip http://localhost:9000/tools/run_kytuning-ffdev.zip;unzip /root/run_kytuning-ffdev.zip -d /root/;rm -rf /root/run_kytuning-ffdev/conf/user.cfg;rm -rf /root/run_kytuning-ffdev/yaml-base/"'
    wget_result = subprocess.run(wget_command, shell=True)
    if wget_result.returncode:
        wget_result.stderr = "测试端下载run_kytuning代码出错,请检查账号、密码是否正确，网络是否可用"
        return wget_result

    # # 复制配置文件conf文件和yaml文件
    scp_command = f'sshpass -p {test_password} scp -o StrictHostKeyChecking=no -r {user_config_path}/conf {user_config_path}/yaml-base {test_username}@{test_ip}:/root/run_kytuning-ffdev/'
    scp_result = subprocess.run(scp_command, shell=True)

    if scp_result.returncode:
        scp_result.stderr = "复制配置文件出错"
        return scp_result

    # 保存性能测试的打印日志
    with open(result_log_name + '_outp.log', 'w') as f:
        # 在远程服务器上运行run.sh脚本
        ssh_command = f'sshpass -p {test_password} ssh {test_username}@{test_ip} "cd /root/run_kytuning-ffdev/;sh /root/run_kytuning-ffdev/run.sh"'
        return_result = subprocess.run(ssh_command, stdout=f, stderr=f, encoding='utf-8', shell=True)


    # 保存kytuning的日志，先获取此次测试测试了哪几项，在获取对应的kytuning.log文件
    for test_case_name in test_case_names:
        klog_command = f'sshpass -p {test_password} scp -o StrictHostKeyChecking=no -r {test_username}@{test_ip}:/root/kytuning/run/{test_case_name}/kytuning.log {result_log_name}_{test_case_name}_kytuning.log'
        klog_result = subprocess.run(klog_command, shell=True)

    # 打包日志文件，方便户下载
    tar_file_path = result_log_name + '.tar'
    # 获取以指定前缀的所有文件路径
    file_paths = glob.glob(result_log_name + '*')

    # 打包文件
    with tarfile.open(tar_file_path, "w") as tar:
        for file_path in file_paths:
            tar.add(file_path, arcname=file_path.replace(RESULT_LOG_FILE, ''))

    # 删除旧文件
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
    if return_result.returncode:
        return_result.stderr = "sh run.sh 命令出错，请查看详细日志"
        return return_result

    return klog_result
