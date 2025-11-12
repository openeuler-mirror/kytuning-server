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
    发起测试
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
        wget_result.stderr = "执行" + wget_command + "失败"
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
    """
    获取链接状态
    :param BMC_IP:
    :param BMC_user_name:
    :param BMC_password:
    :param server_IP:
    :param server_user_name:
    :param server_password:
    :return:
    """
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
    """
    制作ks文件中的密码加密
    :param new_server_password: 用户输入密码
    :return: 加密后的密码
    """
    PASSWORD = crypt.crypt(new_server_password)
    if '/' in PASSWORD or '$' in PASSWORD:
        PASSWORD = PASSWORD.replace('/', r'\/').replace('$', r'\$')
    return PASSWORD

def update_auto_install(user_name, replacements):
    """
    更新自动化安装脚本
    :param user_name: 用户名称
    :param replacements: 需要替换的内容
    :return:
    """
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

def update_system(user_name, server_IP, server_user_name, server_password, machine_name, ISO_name, ks_name):
    """
    执行自动化安装系统的脚本
    :param user_name:
    :param server_IP:
    :param server_user_name:
    :param server_password:
    :param machine_name:
    :param ISO_name:
    :return:
    """
    # 复制脚本至需要重置的系统
    if machine_name == 'intel' and ISO_name.startswith('openEuler'):
        # 先删除可能存在的旧的ifcfg-enP1p3s0f0文件
        rm_networkcfg_command = f'sshpass -p {server_password} ssh -o StrictHostKeyChecking=no {server_user_name}@{server_IP} "rm -rf /root/ifcfg-enP1p3s0f0"'
        subprocess.run(rm_networkcfg_command, shell=True)
        scp_command = f'sshpass -p {server_password} scp -r ./appStore/utils/autoInstall/%s.sh ./appStore/utils/autoInstall/%s ./appStore/utils/autoInstall/clear_kytuning_efibootmgr.sh ./appStore/utils/autoInstall/ifcfg-enP1p3s0f0 {server_user_name}@{server_IP}:/root/' % (str(user_name), ks_name)
    else:
        scp_command = f'sshpass -p {server_password} scp -r ./appStore/utils/autoInstall/%s.sh ./appStore/utils/autoInstall/%s ./appStore/utils/autoInstall/clear_kytuning_efibootmgr.sh {server_user_name}@{server_IP}:/root/' % (str(user_name), ks_name)
    result = subprocess.run(scp_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode:
        return '文件复制出错'
    ssh_command = f'sshpass -p {server_password} ssh -o ServerAliveInterval=10 {server_user_name}@{server_IP} "sh /root/%s.sh"' % (str(user_name))
    subprocess.Popen(ssh_command, shell=True)
    # 下方的方式是接受参数，但是接受的参数重定向到空文件中了。因为这个地方不需要等待返回结果，所以直接使用上面的方法。
    # ssh_process = subprocess.Popen(ssh_command, shell=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
    #                                stderr=subprocess.DEVNULL, text=True)
    return

def get_range(value_list):
    """

    :param value_list:原始分割列表
    :return: （大于5有几组数据，大于5的最小值，大于5的最大值，小于5有几组数据，小于5的最小值，小于5的最大值）
    """
    # 将数据转换为浮点数类型,列表中不能装%号类型，要么就会变成str类型，所以直接去除%处理。
    data = [float(value.replace('%', '')) if value is not None else 0.0 for value in value_list]


    # 大于5%的元素数量和范围
    greater_than_5 = [value for value in data if value > 5]
    count_greater_than_5 = len(greater_than_5)
    min_greater_than_5 = "{:.2f}%".format(min(greater_than_5)) if greater_than_5 else None
    max_greater_than_5 = "{:.2f}%".format(max(greater_than_5)) if greater_than_5 else None

    # 小于-5%的元素数量和范围
    less_than_minus_5 = [value for value in data if value < -5]
    count_less_than_minus_5 = len(less_than_minus_5)
    min_less_than_minus_5 = "{:.2f}%".format(-min(less_than_minus_5)) if less_than_minus_5 else None
    max_less_than_minus_5 = "{:.2f}%".format(-max(less_than_minus_5)) if less_than_minus_5 else None

    return (count_greater_than_5,min_greater_than_5,max_greater_than_5,count_less_than_minus_5,max_less_than_minus_5,min_less_than_minus_5)

def get_analyze_message(data,analyze):
    if data[0] == 1:
        analyze += '有1个单项性能提升%s，' % (data[1])
    elif data[0] > 1:
        analyze += '有%d个单项性能提升%s~%s，' % (data[0], data[1], data[2])
    if data[3] == 1:
        analyze += '有1个单项性能下降%s;' % (data[4])
    elif data[3] > 1:
        analyze += '有%d个单项性能下降%s~%s;' % (data[3], data[4], data[5])
    return analyze

def get_iozone_analyze_message(key, value, old_mark_name, number, analyze):
    name2 = key.split('-')[1].split('（')[0]
    if key.split('-')[0] == 'double':
        name1='两倍内存时：'
    elif key.split('-')[0] == 'full':
        name1='一倍内存时：'
    elif key.split('-')[0] == 'half':
        name1='内存一半时：'
    if value > 5:
        name3 = '提升'
    elif value <-5:
        name3 = '下降'
    if old_mark_name == name1:
        analyze += name2 + name3 + str(value) + '%，'
    else:
        old_mark_name = name1
        analyze = analyze[:-1]+';'
        analyze += '\n%d.'%(number) + name1 + name2 + name3 + str(value) + '%，'
        number += 1
    return analyze,old_mark_name,number


def get_analyze_data(datas,test_type):
    """
    数据分析内容结果获取
    :param datas: 对比数据
    :param test_type: 测试类型
    :return: 数据分析结果
    """
    if test_type == 'stream':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            compar_name = datas[1]['column'+str(int(matching_key.split('column')[-1])-1)]
            if compar_name:
                analyze = compar_name + '对比'+ base_name + '\n'
                for data in datas[4:]:
                    value = round(float(data[matching_key].strip('%')), 2)
                    if value >= 5:
                        analyze += str(data['column1'])+'的'+str(data['column2'])+'提升了'+str(value)+'%'+'\n'
                    elif value <= -5:
                        analyze += str(data['column1'])+'的'+str(data['column2'])+'提升了'+str(value)+'%'+'\n'
                if analyze == compar_name + '对比' + base_name + '\n':
                    analyze += '数据对比没有明显差距，相对持平状态。' + '\n'
                    all_analyze += analyze + '\n'
                else:
                    all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'lmbench':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values=[]
                number=1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])

                Basic_system_list=compare_values[:5]
                Basic_system_value = get_range(Basic_system_list)
                if Basic_system_value[0] or Basic_system_value[3]:
                    analyze += '%d.大项Basic system parameters中'%(number)
                    number += 1
                    analyze = get_analyze_message(Basic_system_value, analyze)
                    analyze += '\n'

                Processor_list=compare_values[5:16]
                Processor_value = get_range(Processor_list)
                if Processor_value[0] or Processor_value[3]:
                    analyze += '%d.大项Processor中'%(number)
                    number += 1
                    analyze = get_analyze_message(Processor_value, analyze)
                    analyze += '\n'

                Basic_integer_list=compare_values[16:21]
                Basic_integer_value = get_range(Basic_integer_list)
                if Basic_integer_value[0] or Basic_integer_value[3]:
                    analyze += '%d.大项Basic integer operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_integer_value, analyze)
                    analyze += '\n'

                Basic_uint64_list=compare_values[21:26]
                Basic_uint64_value = get_range(Basic_uint64_list)
                if Basic_uint64_value[0] or Basic_uint64_value[3]:
                    analyze += '%d.大项Basic uint64 operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_uint64_value, analyze)
                    analyze += '\n'

                Basic_float_list=compare_values[26:30]
                Basic_uint64_value = get_range(Basic_uint64_list)
                if Basic_uint64_value[0] or Basic_uint64_value[3]:
                    analyze += '%d.大项Basic float operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_uint64_value, analyze)
                    analyze += '\n'

                Basic_double_list=compare_values[30:34]
                Basic_double_value = get_range(Basic_double_list)
                if Basic_double_value[0] or Basic_double_value[3]:
                    analyze += '%d.大项Basic double operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_double_value, analyze)
                    analyze += '\n'

                Context_switching_list=compare_values[34:41]
                Context_switching_value = get_range(Context_switching_list)
                if Context_switching_value[0] or Basic_uint64_value[3]:
                    analyze += '%d.大项Context switching中' % (number)
                    number += 1
                    analyze = get_analyze_message(Context_switching_value, analyze)
                    analyze += '\n'

                Communication_latencies_list=compare_values[41:49]
                Communication_latencies_value = get_range(Communication_latencies_list)
                if Communication_latencies_value[0] or Communication_latencies_value[3]:
                    analyze += '%d.大项*Local* Communication latencies中' % (number)
                    number += 1
                    analyze = get_analyze_message(Communication_latencies_value, analyze)
                    analyze += '\n'

                File_and_VM_list=compare_values[49:57]
                File_and_VM_value = get_range(File_and_VM_list)
                if File_and_VM_value[0] or File_and_VM_value[3]:
                    analyze += '%d.大项File & VM system latencies in microseconds中' % (number)
                    number += 1
                    analyze = get_analyze_message(File_and_VM_value, analyze)
                    analyze += '\n'

                Communication_bandwidths_list=compare_values[57:66]
                Communication_bandwidths_value = get_range(Communication_bandwidths_list)
                if Communication_bandwidths_value[0] or Communication_bandwidths_value[3]:
                    analyze += '%d.大项*Local* Communication bandwidths in MB/s - bigger is better中' % (number)
                    number += 1
                    analyze = get_analyze_message(Communication_bandwidths_value, analyze)
                    analyze += '\n'

                Memory_latencies_list=compare_values[66:71]
                Memory_latencies_value = get_range(Memory_latencies_list)
                if Memory_latencies_value[0] or Memory_latencies_value[3]:
                    analyze += '%d.大项Memory latencies in nanoseconds中' % (number)
                    number += 1
                    analyze = get_analyze_message(Memory_latencies_value, analyze)
                    analyze += '\n'

                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'unixbench':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])

                single_list = compare_values[:12]
                single_value = get_range(single_list)
                if single_value[0] or single_value[3]:
                    analyze += '%d.单线程中' % (number)
                    number += 1
                    analyze = get_analyze_message(single_value, analyze)
                    single_score = float(compare_values[12].replace('%', '')) if compare_values[12] is not None else 0
                    if single_score > 2:
                        analyze += '总分提升%d%%;\n'%(single_score)
                    elif single_score < -2:
                        analyze += '总分下降%d%%;\n'%(single_score)
                    else:
                        analyze += '总分基本持平;\n'

                multi_list = compare_values[13:25]
                multi_value = get_range(multi_list)
                if multi_value[0] or multi_value[3]:
                    analyze += '%d.多线程中' % (number)
                    number += 1
                    analyze = get_analyze_message(multi_value, analyze)
                    single_score = float(compare_values[25].replace('%', '')) if compare_values[25] is not None else 0
                    if single_score > 2:
                        analyze += '总分提升%d%%;\n' % (single_score)
                    elif single_score < -2:
                        analyze += '总分下降%d%%;\n' % (single_score)
                    else:
                        analyze += '总分基本持平;\n'

                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'fio':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'
                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])
                # compare_values[2::4]只要iops的数据
                fio_value = get_range(compare_values[2::4])
                analyze += '%d.总共测试%d项，' % (number,len(compare_values[2::4]))
                analyze = get_analyze_message(fio_value,analyze)
                analyze += '\n'
                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'iozone':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'
                # 全部的对比数据的名称和值
                compare_names = []
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_names.append(data['column1'])
                    compare_values.append(data[matching_key])
                compare_dict = dict(zip(compare_names, compare_values))

                old_mark_name = ''
                for key,value in compare_dict.items():
                    value_ = float(value.replace('%', '')) if value is not None else 0.0
                    analyze, old_mark_name, number = get_iozone_analyze_message(key, value_, old_mark_name, number, analyze)
            all_analyze += analyze + '\n\n'
        return all_analyze
    elif test_type == 'jvm2008':
        pass
    elif test_type == 'cpu2006':
        pass
    elif test_type == 'cpu2017':
        pass