"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:02:58 2024 +0800
"""
from django.db import models

# Create your models here.
class TestCase(models.Model):
    """测试案例表"""
    ThreadType = (
        ("单线程", "单线程"),
        ("多线程", "多线程"),
    )
    project_name = models.CharField(max_length=50, verbose_name='项目名称')
    ip = models.CharField(max_length=50, verbose_name='IP地址')
    stream = models.IntegerField(default=0, verbose_name='几组stream数据')
    lmbench = models.IntegerField(default=0, verbose_name='几组lmbench数据')
    unixbench = models.IntegerField(default=0, verbose_name='几组unxibench数据')
    fio = models.IntegerField(default=0, verbose_name='几组fio数据')
    iozone = models.IntegerField(default=0, verbose_name='几组iozone数据')
    jvm2008 = models.IntegerField(default=0, verbose_name='几组jvm2008数据')
    cpu2006 = models.IntegerField(default=0, verbose_name='几组cpu2006数据')
    cpu2017 = models.IntegerField(default=0, verbose_name='几组cpu2017数据')
    user_name = models.CharField(max_length=255, verbose_name='测试人员')
    test_result = models.TextField(verbose_name='测试结果反馈', null=True, blank=True)  # 如果有多项也是拼接
    result_log_name = models.CharField(max_length=255, verbose_name='日志文件路径的base部分')
    is_error = models.BooleanField(default=False,verbose_name="是否是错误列表所需要的")
    test_time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)


    class Meta:
        db_table = 'testCase'
