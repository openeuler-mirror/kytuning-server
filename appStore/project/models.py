"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 09:53:11 2024 +0800
"""
from datetime import datetime

from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Project(models.Model):
    """Project表"""
    env_id = models.IntegerField(verbose_name='环境id')
    project_name = models.CharField(max_length=255, verbose_name='项目名称',null=True,blank=True)
    user_name = models.CharField(max_length=255, verbose_name='测试人员名称')
    os_version = models.CharField(max_length=255, verbose_name='操作系统版本',null=True,blank=True)
    cpu_module_name = models.CharField( max_length=255, verbose_name='cpu型号',null=True,blank=True)
    times = models.IntegerField(verbose_name='第几次测试')
    ip = models.CharField(max_length=50,verbose_name='测试机器ip',null=True,blank=True)
    stream = models.IntegerField(default=0, verbose_name='几组stream数据')
    cpu2006 = models.IntegerField(default=0, verbose_name='几组cpu2006数据')
    cpu2017 = models.IntegerField(default=0, verbose_name='几组cpu2017数据')
    fio = models.IntegerField(default=0, verbose_name='几组fio数据')
    iozone = models.IntegerField(default=0, verbose_name='几组iozone数据')
    jvm2008 = models.IntegerField(default=0, verbose_name='几组jvm2008数据')
    lmbench = models.IntegerField(default=0, verbose_name='几组lmbench数据')
    unixbench = models.IntegerField(default=0, verbose_name='几组unxibench数据')
    test_time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)
    message = models.CharField(max_length=255, verbose_name='项目描述',null=True,blank=True)

    class Meta:
        db_table = 'project'
