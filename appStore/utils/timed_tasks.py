"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""

import time
import schedule
import threading
from django.http import HttpRequest

from appStore.utils.constants import NEW_SERVER_PASSWORD, ROOT_SIZE, SWAP_SIZE, INTERVAL, START_TIME, CHECK_TIMEOUT
from appStore.utils.subprocess import check_system_success, update_rpm


def auto_install_system(test_machine_data, request, ip, iso_name, koji_addr, user_config_path):
    """
    自动化安装操作系统
    :param test_machine_data: 安装操作系统的设备对象
    :param request: request对象
    :param ip: 设备ip
    :param iso_name: iso的名称
    :param koji_addr: kojifile地址
    :param user_config_path：用户配置地址
    :return: 安装操作系统是否成功
    """
    test_machine_data.owner = request.user.chinese_name

    # 自动化安装
    from appStore.testMachine.views import TestMachineViewSet
    request_test_machine = HttpRequest()
    request_test_machine.method = 'POST'
    # 获取设备信息
    machine_data = {'id': test_machine_data.id,
                    'server_IP': ip,
                    'server_user_name': test_machine_data.server_user_name,
                    'server_password': test_machine_data.server_password,
                    'new_server_password': NEW_SERVER_PASSWORD,
                    'new_iso_name': iso_name,
                    'root_size': ROOT_SIZE,
                    'swap_size': SWAP_SIZE,
                    'clear_part': True,
                    'kernel_type': None
                    }

    request_test_machine.data = machine_data
    request_test_machine.user = request.user
    TestMachineViewSet = TestMachineViewSet()
    # todo 放开
    TestMachineViewSet.modify_server(request=request_test_machine)

    # 设置任务起始时间
    START_TIME[ip] = time.time()
    # 设置定时任务，检查系统是否安装成功
    schedule.every(INTERVAL).seconds.do(test_tasks, ip, test_machine_data.server_user_name, test_machine_data.server_password, koji_addr,
                                        user_config_path)
    # 启动定时任务调度器
    start_scheduler()
    return None


def test_tasks(ip, username, password, koji_addr, user_config_path):
    """
    执行测试任务
    :param ip: 设备ip
    :param server_name: 设备用户名
    :param password: 设备密码
    :param koji_addr: kojifile地址
    :param user_config_path：用户配置地址
    :return:
    """
    print(f"-----------自动化安装操作系统-----------")
    if check_system_success(ip, username, password):
        print(f"任务 {ip} 的系统安装成功")
        update_rpm(ip, username, password, koji_addr, user_config_path)
        return schedule.CancelJob
    if time.time() - START_TIME[ip] > CHECK_TIMEOUT:
        print(f"任务 {ip} 安装失败：超时未检测到系统安装成功")
        # todo 页面提示报错
        return schedule.CancelJob
    print(f"{INTERVAL} 秒后重试任务 {ip}...")
    return False


def start_scheduler():
    """
    启动定时任务调度器
    """
    print('---------启动定时任务调度器------------')
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
