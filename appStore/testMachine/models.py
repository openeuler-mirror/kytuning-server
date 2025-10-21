"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
from django.db import models


# Create your models here.
class TestMachine(models.Model):
    """测试机器表"""
    Link_Status_Type = (
        ("在线", "在线"),
        ("离线", "离线"),
        ("网络未连接", "网络未连接"),
        ("用户名或密码错误", "用户名或密码错误"),
    )
    Task_Status_Type = (
        ("空闲", "空闲"),
        ("繁忙", "繁忙"),
    )
    ARCH_NAME_TYPE = (
        ("aarch", "aarch"),
        ("x86", "x86"),
    )
    machine_name = models.CharField(max_length=50, verbose_name='设备名称')
    cpu_module_name = models.CharField(max_length=50, verbose_name='cpu型号')
    arch_name = models.CharField(choices=ARCH_NAME_TYPE,max_length=50, verbose_name='架构')
    BMC_IP = models.CharField(max_length=50, verbose_name='BMC_IP')
    BMC_user_name = models.CharField(max_length=50, verbose_name='BMC用户名')
    BMC_password = models.CharField(max_length=50, verbose_name='BMC密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    owner = models.CharField(max_length=50, verbose_name='当前操作系统负责人', null=True, blank=True)
    server_IP = models.CharField(max_length=50, verbose_name='server_IP', null=True, blank=True)
    server_user_name = models.CharField(max_length=50, verbose_name='服务器用户名', null=True, blank=True)
    server_password = models.CharField(max_length=50, verbose_name='服务器密码', null=True, blank=True)
    os_version = models.CharField(max_length=500, verbose_name='操作系统版本', null=True, blank=True)
    link_status = models.CharField(choices=Link_Status_Type, max_length=50, verbose_name='链接状态', null=True, blank=True)
    task_status = models.CharField(choices=Task_Status_Type, max_length=50, verbose_name='任务状态', null=True, blank=True)
    queue_user = models.CharField(max_length=50, verbose_name='排队人员', null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'testMachine'
