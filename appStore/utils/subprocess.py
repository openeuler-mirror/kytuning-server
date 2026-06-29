"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:15:41 2024 +0800
"""
#!/usr/bin/env python
# encoding: utf-8
"""
网络相关的公共函数
@author: Wqz
@time: 15/4/24 03:04 PM
"""
import glob
import re
import os
import shutil
import tarfile
import subprocess
from appStore.utils.constants import RESULT_LOG_FILE, TOOLS_URL


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

    # 检查 wget、unzip 和 make 是否已安装
    check_yum_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "rpm -q wget unzip make"'
    check_yum_result = subprocess.run(check_yum_command, shell=True, capture_output=True, text=True)
    if '未安装软件包' in check_yum_result.stdout:
        # 如果是最小化安装的话没有wget和unzip所以需要下载这两个软件包。
        yum_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "yum install wget unzip make -y"'
        yum_result = subprocess.run(yum_command, shell=True)
        if yum_result.returncode:
            yum_result.stderr = "执行" + yum_command + "失败"
            return yum_result

    # 下载run_kytuning代码
    wget_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "rm -rf /root/run_kytuning-ffdev/;wget -O /root/run_kytuning-ffdev.zip %srun_kytuning-ffdev.zip"' % (
        TOOLS_URL)
    wget_result = subprocess.run(wget_command, shell=True)
    if wget_result.returncode:
        wget_result.stderr = "测试端下载run_kytuning代码出错,请检查账号、密码是否正确，网络是否可用\n请在其它机器中测试：\"" + wget_command
        return wget_result

    # 解压
    unzip_command = f'sshpass -p {test_password} ssh {test_username}@{test_ip} "unzip /root/run_kytuning-ffdev.zip -d /root/;rm -rf /root/run_kytuning-ffdev/conf/kytuning.cfg;"'
    unzip_result = subprocess.run(unzip_command, shell=True)
    if unzip_result.returncode:
        unzip_result.stderr = "unzip解压失败，请查看是否有unzip命令，以及run_kytuning-ffdev.zip是否下载成功"
        return unzip_result

    # 复制配置文件conf文件和yaml文件
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

    # 放在后面是为了获取日志
    if return_result.returncode and return_result.returncode != 255:
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
        # 脚本中需要替换到的位置
        pattern = fr'({variable}=).*'
        if variable in ['root_size', 'swap_size', 'clear_part', 'kernel510']:
            # 这三个不是str类型
            replacement = fr'\g<1>{new_value}'
        else:
            # \g < 1 > 表示对之前定义的第一个捕获组进行引用
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
    # todo 后期有时间做优化和排查根本原因
    if machine_name == 'intel' and ISO_name.startswith('openEuler'):
        # 先删除可能存在的旧的ifcfg-enP1p3s0f0文件
        rm_networkcfg_command = f'sshpass -p {server_password} ssh -o StrictHostKeyChecking=no {server_user_name}@{server_IP} "rm -rf /root/ifcfg-enP1p3s0f0"'
        subprocess.run(rm_networkcfg_command, shell=True)
        scp_command = f'sshpass -p {server_password} scp -r ./appStore/utils/autoInstall/%s.sh ./appStore/utils/autoInstall/%s ./appStore/utils/autoInstall/clear_kytuning_efibootmgr.sh ./appStore/utils/autoInstall/ifcfg-enP1p3s0f0 {server_user_name}@{server_IP}:/root/' % (
            str(user_name), ks_name)
    else:
        scp_command = f'sshpass -p {server_password} scp -r ./appStore/utils/autoInstall/%s.sh ./appStore/utils/autoInstall/%s ./appStore/utils/autoInstall/clear_kytuning_efibootmgr.sh {server_user_name}@{server_IP}:/root/' % (
            str(user_name), ks_name)
    result = subprocess.run(scp_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode:
        return '文件复制出错'
    ssh_command = f'sshpass -p {server_password} ssh -o ServerAliveInterval=10 {server_user_name}@{server_IP} "bash /root/%s.sh"' % (str(user_name))
    subprocess.Popen(ssh_command, shell=True)
    # 下方的方式是接受参数，但是接受的参数重定向到空文件中了。因为这个地方不需要等待返回结果，所以直接使用上面的方法。
    # ssh_process = subprocess.Popen(ssh_command, shell=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
    #                                stderr=subprocess.DEVNULL, text=True)
    return


def check_disk_size(test_ip, test_username, test_password):
    """
    检查磁盘剩余空间大小
    :param test_ip:机器IP
    :param test_username:机器用户名
    :param test_password:机器密码
    :return: 磁盘剩余空间，单位为G。
    """
    check_yum_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "bash -s" < ./appStore/utils/autoInstall/check_disk_size.sh'
    check_yum_result = subprocess.run(check_yum_command, shell=True, capture_output=True, text=True)
    remaining_disk_space = check_yum_result.stdout.strip()
    return remaining_disk_space


def stop_test_task(test_ip, test_username, test_password):
    """
    终止测似任务
    :param test_ip:机器IP
    :param test_username:机器用户名
    :param test_password:机器密码
    :return: 停止测试结果。
    """
    stop_test_command = f'sshpass -p {test_password} ssh -o StrictHostKeyChecking=no {test_username}@{test_ip} "pkill -f kytuning -9"'
    stop_test_result = subprocess.run(stop_test_command, shell=True, capture_output=True, text=True)
    return stop_test_result


def check_system_success(ip, server_name, password):
    """
    检查操作系统是否安装完成
    :param ip: 设备ip
    :param server_name: 设备用户名
    :param password: 设备密码
    :return: 安装操作系统是否成功
    """
    print(f"--------------------检查系统是否安装成功 (IP: {ip})-----------------")
    # 去除旧的连接记录
    mv_ssh_keygen = "ssh-keygen -R " + ip
    subprocess.run(mv_ssh_keygen, shell=True)
    print(f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} 'echo success'")
    try:
        result = subprocess.run(f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} 'echo success'", shell=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "success" in result.stdout:
            print('系统安装成功========')
            return True
    except Exception as e:
        print(f"系统安装失败============: {e}")
    return False


def update_rpm(ip, server_name, password, koji_addr, user_config_path):
    """
    更新rpm包
    :param ip: 设备ip
    :param server_name: 设备用户名
    :param password: 设备密码
    :param koji_addr: koji仓库地址
    :return: 是否更新rpm包完成
    """
    mv_ssh_keygen = "ssh-keygen -R " + ip
    subprocess.run(mv_ssh_keygen, shell=True)

    # 配置yum源
    # 重命名 /etc/yum.repos.d/ 目录下所有 .repo 文件为 .repo-bak
    command_list_files = (
        f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} "
        "'sudo ls /etc/yum.repos.d/*.repo'"
    )
    result_list_files = subprocess.run(command_list_files, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result_list_files.returncode != 0:
        print("Error listing .repo files:", result_list_files.stderr)
        return

    repo_files = result_list_files.stdout.splitlines()
    for repo_file in repo_files:
        repo_file = repo_file.strip()
        command_rename_file = (
            f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} "
            f"'sudo mv {repo_file} {repo_file}-bak'"
        )
        result_rename_file = subprocess.run(command_rename_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result_rename_file.returncode != 0:
            print(f"Error renaming {repo_file}:", result_rename_file.stderr)
            return

    # 新增 kojifile.repo 文件并写入指定的内容
    print(koji_addr, 'koji_addr地址是--------------------------')
    kojifiles_repo = f"""[kojifiles]
name = kojifiles
baseurl = {koji_addr}
gpgcheck = 0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-kylin
enabled = 1
"""
    print(kojifiles_repo)
    command_add_repo = (
        f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} "
        f"\"echo '{kojifiles_repo}' | sudo tee /etc/yum.repos.d/kojifile.repo\""
    )
    result_add_repo = subprocess.run(command_add_repo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result_add_repo.returncode != 0:
        print("Error adding kojifiles repo:", result_add_repo.stderr)
        return
    print("---------------------kojifiles的repo源配置成功.")

    # 检查 wget、unzip 和 make 是否已安装
    check_yum_command = f'sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} "rpm -q wget unzip make"'
    check_yum_result = subprocess.run(check_yum_command, shell=True, capture_output=True, text=True)
    if '未安装软件包' in check_yum_result.stdout:
        # 如果是最小化安装的话没有wget和unzip所以需要下载这两个软件包。
        yum_command = f'sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} "yum install wget unzip make -y"'
        yum_result = subprocess.run(yum_command, shell=True)
        if yum_result.returncode:
            yum_result.stderr = "执行" + yum_command + "失败"
            return yum_result

    # 下载run_kytuning代码
    wget_command = f'sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} "rm -rf /root/run_kytuning-ffdev/;wget -O /root/run_kytuning-ffdev.zip %srun_kytuning-ffdev.zip"' % (
        TOOLS_URL)
    wget_result = subprocess.run(wget_command, shell=True)
    if wget_result.returncode:
        wget_result.stderr = "测试端下载run_kytuning代码出错,请检查账号、密码是否正确，网络是否可用\n请在其它机器中测试：\"" + wget_command
        return wget_result

    # 解压
    unzip_command = f'sshpass -p {password} ssh {server_name}@{ip} "unzip /root/run_kytuning-ffdev.zip -d /root/;rm -rf /root/run_kytuning-ffdev/conf/kytuning.cfg;"'
    unzip_result = subprocess.run(unzip_command, shell=True)
    if unzip_result.returncode:
        unzip_result.stderr = "unzip解压失败，请查看是否有unzip命令，以及run_kytuning-ffdev.zip是否下载成功"
        return unzip_result

    print("---------------------软件包下载并解压完成.")

    # 复制配置文件conf文件和yaml文件
    scp_command = f'sshpass -p {password} scp -r {user_config_path}/conf {user_config_path}/yaml-base {server_name}@{ip}:/root/run_kytuning-ffdev/'
    scp_result = subprocess.run(scp_command, shell=True)

    if scp_result.returncode:
        scp_result.stderr = "复制配置文件出错"
        return scp_result

    # 执行rpm更新脚本，更新完成后执行自动测试
    try:
        result = subprocess.run(
            f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {server_name}@{ip} 'bash /root/run_kytuning-ffdev/monitor_test/update_system.sh'",
            shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "success" in result.stdout:
            print('系统安装成功========')
            return True
    except Exception as e:
        print(f"系统安装失败============: {e}")
    return False
