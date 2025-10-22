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
import crypt
import glob
import re
import os
import shutil
import tarfile
import subprocess
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from rest_framework import pagination, status
from appStore.utils.constants import RESULT_LOG_FILE, TOOLS_URL


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
        'chinesename': user.chinese_name,
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

    mv_ssh_keygen = "ssh-keygen -R " + test_ip
    subprocess.run(mv_ssh_keygen, shell=True)

    # 如果是最小化安装的话没有wget和unzip所以需要下载这两个软件包。
    wget_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "yum install wget unzip make -y"'
    wget_result = subprocess.run(wget_command, shell=True)
    if wget_result.returncode:
        wget_result.stderr = "测试端下载run_kytuning代码出错,请检查账号、密码是否正确，网络是否可用\n请在其它机器中测试：\"" + wget_command
        return wget_result

    # 下载run_kytuning代码
    wget_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "rm -rf /root/run_kytuning-ffdev/;wget -O /root/run_kytuning-ffdev.zip %srun_kytuning-ffdev.zip"' % (
        TOOLS_URL)
    wget_result = subprocess.run(wget_command, shell=True)
    if wget_result.returncode:
        wget_result.stderr = "测试端下载run_kytuning代码出错,请检查账号、密码是否正确，网络是否可用\n请在其它机器中测试：\"" + wget_command
        return wget_result

    # 解压
    unzip_command = f'sshpass -p {test_password} ssh {test_username}@{test_ip} "unzip /root/run_kytuning-ffdev.zip -d /root/;rm -rf /root/run_kytuning-ffdev/conf/kytuning.cfg;rm -rf /root/run_kytuning-ffdev/yaml-base/"'
    unzip_result = subprocess.run(unzip_command, shell=True)
    if unzip_result.returncode:
        unzip_result.stderr = "unzip解压失败，请查看是否有unzip命令，以及run_kytuning-ffdev.zip是否下载成功"
        return unzip_result

    # # 复制配置文件conf文件和yaml文件
    scp_command = f'sshpass -p {test_password} scp -r {user_config_path}/conf {user_config_path}/yaml-base {test_username}@{test_ip}:/root/run_kytuning-ffdev/'
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


def get_link_status(BMC_IP, BMC_user_name, BMC_password, server_IP, server_user_name, server_password):
    # 判断离线状态 f是可以使用变量
    ipmi_cmd = f"ipmitool -H {BMC_IP} -I lanplus -U {BMC_user_name} -P \'{BMC_password}\' chassis power status"
    result = subprocess.run(ipmi_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stdout.strip() == 'Chassis Power is off':
        return '离线'

    # 判断网络无法链接状态
    result = subprocess.run(["ping", "-c", "1", "-w", "1", server_IP], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)
    output = result.stdout
    if not "1 packets transmitted, 1 received" in output:
        return '网络未连接'

    mv_ssh_keygen = "ssh-keygen -R " + server_IP
    subprocess.run(mv_ssh_keygen, shell=True)

    ssh_cmd = f'sshpass -p {server_password} ssh -o StrictHostKeyChecking=no {server_user_name}@{server_IP}'
    result = subprocess.run(ssh_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    # 获取返回状态 0 代表成功
    if result.returncode:
        return '用户名或密码错误'
    return '在线'

def make_ks_password(new_server_password):
    PASSWORD = crypt.crypt(new_server_password)
    if '/' in PASSWORD or '$' in PASSWORD:
        PASSWORD = PASSWORD.replace('/', r'\/').replace('$', r'\$')
    return PASSWORD

def update_auto_install(user_name, replacements):
    # 原始脚本文件路径
    auto_install_file = './appStore/utils/autoInstall/auto_install.sh'
    # 副本文件路径
    user_install_file = './appStore/utils/autoInstall/' + str(user_name) + '.sh'
    # 复制原始脚本文件到副本文件
    shutil.copy2(auto_install_file, user_install_file)
    # 读取副本脚本内容
    with open(user_install_file, 'r') as f:
        script_content = f.read()
    # 遍历替换字典中的每个键值对，将对应的变量行替换为新值
    for variable, new_value in replacements.items():
        pattern = fr'({variable}=).*'
        replacement = fr'\g<1>"{new_value}"'
        script_content = re.sub(pattern, replacement, script_content)

    # 将更新后的内容写回副本脚本文件
    with open(user_install_file, 'w') as f:
        f.write(script_content)

def update_system(user_name, server_IP, server_user_name, server_password, KS_FILE_NAME):
    # 复制脚本至需要重置的系统
    # todo 后期ifcfg-enP1p3s0f0可以做服务器类型和ISO版本判断来确定ifcfg-enP1p3s0f0是否拷贝
    scp_command = f'sshpass -p {server_password} scp -r ./appStore/utils/autoInstall/%s.sh ./appStore/utils/autoInstall/%s ./appStore/utils/autoInstall/clear_kytuning_efibootmgr.sh ./appStore/utils/autoInstall/ifcfg-enP1p3s0f0 {server_user_name}@{server_IP}:/root/' % (
    str(user_name), KS_FILE_NAME)
    result = subprocess.run(scp_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True)
    if result.returncode:
        return '文件复制出错'

    ssh_command = f'sshpass -p {server_password} ssh -o ServerAliveInterval=10 {server_user_name}@{server_IP} "sh /root/%s.sh"' % (
        str(user_name))

    subprocess.Popen(ssh_command, shell=True)
    # 下方的方式是接受参数，但是接受的参数重定向到空文件中了。因为这个地方不需要等待返回结果，所以直接使用上面的方法。
    # ssh_process = subprocess.Popen(ssh_command, shell=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
    #                                stderr=subprocess.DEVNULL, text=True)
    return
