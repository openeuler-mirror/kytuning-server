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
    machine_name = models.CharField(max_length=50, verbose_name='设备名称')
    cpu_module_name = models.CharField(max_length=100, verbose_name='cpu型号')
    arch_name = models.CharField(max_length=50, verbose_name='架构')
    BMC_IP = models.CharField(max_length=50, verbose_name='BMC_IP')
    BMC_user_name = models.CharField(max_length=50, verbose_name='BMC用户名')
    BMC_password = models.CharField(max_length=50, verbose_name='BMC密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    os_version = models.CharField(max_length=50, verbose_name='操作系统版本', null=True, blank=True)
    test_user = models.CharField(max_length=255, verbose_name='当前操作系统负责人', null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'testMachine'
