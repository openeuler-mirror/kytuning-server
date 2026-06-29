"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""

import ast
import time
import schedule
import threading
from django.http import HttpRequest

from appStore.testCase.models import TestCase
from appStore.testMachine.models import TestMachine
from appStore.userConfig.models import UserConfig
from appStore.utils.constants import NEW_SERVER_PASSWORD, ROOT_SIZE, SWAP_SIZE, INTERVAL, START_TIME, CHECK_TIMEOUT, MONITOR_KOJIFILES_TIME, \
    KOJIFILES_MD5
from appStore.utils.subprocess import check_system_success, update_rpm, get_kojifiles_md5


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
    print('-----------执行自动化安装--------------')
    TestMachineViewSet.modify_server(request=request_test_machine)

    # 设置任务起始时间
    START_TIME[ip] = time.time()
    # 设置定时任务，检查系统是否安装成功
    schedule.every(INTERVAL).minutes.do(test_tasks, ip, test_machine_data.server_user_name, test_machine_data.server_password, koji_addr, user_config_path)
    # 启动定时任务调度器
    start_scheduler()
    return None


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


def install_system(kojifile_addr, koji_md5_hash, request, user_config_path):
    new_koji_md5_hash = get_kojifiles_md5(kojifile_addr)
    koji_md5_hash = None
    print("old的MD5哈希值:", koji_md5_hash)
    print("新的MD5哈希值:", new_koji_md5_hash)
    if new_koji_md5_hash == koji_md5_hash:
        print("kojifiles未发生改变，无需处理")
    else:
        KOJIFILES_MD5[kojifile_addr] = new_koji_md5_hash
        print("kojifiles地址发生改变,执行自动化性能测试")
        # 获取监控测试的ip信息
        ip_list = ast.literal_eval('[' + UserConfig.objects.filter(kojifile_addr=kojifile_addr).last().ip + ']')
        for ip in ip_list:
            machine_data = TestMachine.objects.get(server_IP=ip)
            # 判断机器是否有人使用或者是否有排队人员
            if machine_data.owner or machine_data.queue_user:
                machine_data.queue_user = machine_data.queue_user + ',' + request.user.chinese_name if machine_data.queue_user else request.user.chinese_name
                machine_data.save()
            else:
                test_case = TestCase.objects.filter(test_type='监控测试', kojifile_addr=kojifile_addr).order_by('-id').last()
                test_case.test_result = '排队中'
                test_case.save()
                print('----测试任务修改测试状态------')
                auto_install_system(machine_data, request, ip, test_case.iso_name, kojifile_addr, user_config_path)
                # pass

def monitor_kojifiles(kojifile_addr, koji_md5_hash, request, user_config_path):
    """
    监控kojifile地址的定时任务
    :param kojifile_addr: kojifiles地址
    :param koji_md5_hash: kojifiles地址生成的md5值
    :return:
    """
    # 设置定时任务，监控kojifiles地址
    print('---------启动监控测试-----------------')
    schedule.every(MONITOR_KOJIFILES_TIME).days.do(install_system, kojifile_addr, koji_md5_hash, request, user_config_path)
    # schedule.every(MONITOR_KOJIFILES_TIME).minutes.do(install_system, kojifile_addr, koji_md5_hash, request, user_config_path)
    # install_system(kojifile_addr, koji_md5_hash, request, user_config_path)
    # 启动定时任务调度器
    start_scheduler()
    return None
