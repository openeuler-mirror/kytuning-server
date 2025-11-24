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
公共函数
@author: Wqz
@time: 15/4/24 03:04 PM
"""
import subprocess

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