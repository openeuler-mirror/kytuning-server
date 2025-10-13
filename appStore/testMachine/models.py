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
    arch_name = models.CharField(max_length=50, verbose_name='架构')
    cpu_module_name = models.CharField(max_length=100, verbose_name='cpu型号')
    ip = models.CharField(max_length=50, verbose_name='IP')
    os_version = models.CharField(max_length=50, verbose_name='操作系统版本')
    test_user = models.CharField(max_length=255, verbose_name='当前操作系统负责人', )
    use_time = models.DateTimeField(verbose_name='接手时间', auto_now=True)


    class Meta:
        db_table = 'testMachine'
