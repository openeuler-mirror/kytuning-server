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
import logging
import threading
from django.http import HttpRequest

from appStore.testCase.models import TestCase
from appStore.testMachine.models import TestMachine
from appStore.userConfig.models import UserConfig
from appStore.users.models import UserProfile
from appStore.utils.constants import NEW_SERVER_PASSWORD, ROOT_SIZE, SWAP_SIZE, INTERVAL, START_TIME, CHECK_TIMEOUT, MONITOR_KOJIFILES_TIME, \
    RUN_KYTUNING_CONFIG_TEMP
from appStore.utils.subprocess import check_system_success, update_rpm, get_kojifiles_md5

log = logging.getLogger('kytuninglog')


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
    log.info("-----------自动化安装操作系统-----------")
    print("-----------自动化安装操作系统-----------")
    if check_system_success(ip, username, password):
        log.info(f"任务 {ip} 的系统安装成功")
        print(f"任务 {ip} 的系统安装成功")
        update_rpm(ip, username, password, koji_addr, user_config_path)
        return schedule.CancelJob
    if time.time() - START_TIME[ip] > CHECK_TIMEOUT:
        log.info(f"任务 {ip} 安装失败：超时未检测到系统安装成功")
        print(f"任务 {ip} 安装失败：超时未检测到系统安装成功")
        test_case = TestCase.objects.filter(ip=ip).last()
        test_case.test_result = '系统安装失败'
        test_case.save()
        return schedule.CancelJob
    jobs = schedule.jobs
    for job in jobs:
        print(f'当前环境中还存在的任务有：{job}')
    return False


def start_scheduler():
    """
    启动定时任务调度器
    """

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()


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
    # request_test_machine.user = request.user
    request_test_machine.user = request.user
    TestMachineViewSet = TestMachineViewSet()
    log.info('-----------执行自动化安装--------------')
    print('-----------执行自动化安装--------------')
    TestMachineViewSet.modify_server(request=request_test_machine)

    # 设置任务起始时间
    START_TIME[ip] = time.time()
    # 设置定时任务，检查系统是否安装成功
    schedule.every(INTERVAL).minutes.do(test_tasks, ip, test_machine_data.server_user_name, test_machine_data.server_password, koji_addr,
                                        user_config_path)
    # 启动定时任务调度器
    start_scheduler()
    return None


def install_system(monitor_test, request, user_config_path):
    new_koji_md5 = get_kojifiles_md5(monitor_test.kojifile_addr)
    print('新的kojifilemd5为：', new_koji_md5)
    if new_koji_md5 == monitor_test.kojifile_md5:
        log.info("kojifiles未发生改变，无需处理")
        print("kojifiles未发生改变，无需处理")
    else:
        monitor_test.kojifile_md5 = new_koji_md5
        log.info("kojifiles地址发生改变,执行自动化性能测试")
        print("kojifiles地址发生改变,执行自动化性能测试")
        # 获取迭代测试的ip信息

        machine_data = TestMachine.objects.get(server_IP=monitor_test.ip)
        # 判断机器是否有人使用或者是否有排队人员
        if machine_data.owner or machine_data.queue_user:
            # 判断排队列表中是否存在root用户
            print(f'当前排队用户是{machine_data.queue_user}')
            print(f'当前使用用户是{machine_data.owner}')
            if 'root' not in machine_data.queue_user.split(',') and machine_data.owner != 'root':
                monitor_test.test_result = '等待中'
                monitor_test.save()
                print(f'增加排队用户后的排队用户是{machine_data.queue_user}')
                machine_data.queue_user = machine_data.queue_user + ',' + request.user.chinese_name if machine_data.queue_user else request.user.chinese_name
                machine_data.save()
            else:
                print(f'排队人员中有root用户，或者使用人员是root用户，IP机器为:', monitor_test.ip)
        else:
            monitor_test.test_result = '运行中'
            monitor_test.save()
            auto_install_system(machine_data, request, monitor_test.ip, monitor_test.iso_name, monitor_test.kojifile_addr, user_config_path)


def new_monitor_kojifiles():
    """
    重启服务拉起所有监控kojifile地址的定时任务
    :return:
    """
    # 获取所有监控任务
    monitor_test_list = TestCase.objects.filter(is_it_monitored=True).filter(test_result='等待中').order_by('-id')
    print('运行监控测试的数据是', monitor_test_list)

    # 创建一个root的request对象
    from django.test import RequestFactory
    # 创建一个 RequestFactory 实例
    request_factory = RequestFactory()
    # 查找root用户对象
    root_user = UserProfile.objects.get(username='root')
    # 使用 RequestFactory 创建一个 GET 请求对象，并设置用户信息
    request = request_factory.get('/')
    request.user = root_user

    for monitor_test in monitor_test_list:
        print('运行监控测试的数据是', monitor_test)
        user_config_path = RUN_KYTUNING_CONFIG_TEMP + monitor_test.user_name
        # 创建对应的定时任务
        install_system(monitor_test, request, user_config_path)
        # schedule.every(MONITOR_KOJIFILES_TIME).minutes.do(install_system, monitor_test, request, user_config_path)
        # 启动定时任务调度器
        start_scheduler()
    return None
