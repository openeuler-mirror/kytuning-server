"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:10:52 2024 +0800
"""
from django.db import models

# Create your models here.
class UserConfig(models.Model):
    """用户配置表"""
    user_name = models.CharField(max_length=50, verbose_name='用户名称')
    user_password = models.CharField(max_length=50, verbose_name='用户密码')
    project_name = models.CharField(max_length=50, verbose_name='测试项目名称')
    test_ip = models.CharField(max_length=50, verbose_name='测试机器IP')
    test_password = models.CharField(max_length=50, verbose_name='测试机器密码')
    stream_number = models.CharField(max_length=100, verbose_name='stream测试迭代次数')
    lmbench_number = models.CharField(max_length=100, verbose_name='lmbench测试迭代次数')
    unixbench_number = models.CharField(max_length=100, verbose_name='unixbench测试迭代次数')
    fio_number = models.CharField(max_length=100, verbose_name='fio测试迭代次数')
    iozone_number = models.CharField(max_length=100, verbose_name='iozone测试迭代次数')
    jvm2008_number = models.CharField(max_length=100, verbose_name='jvm2008测试迭代次数')
    cpu2006_number = models.CharField(max_length=100, verbose_name='cpu2006测试迭代次数')
    cpu2017_number = models.CharField(max_length=100, verbose_name='cpu2017测试迭代次数')
    stream_config = models.TextField(verbose_name='stream测试配置文件')
    lmbench_config = models.TextField(verbose_name='lmbench测试配置文件')
    unixbbench_config = models.TextField(verbose_name='unixbbench测试配置文件')
    fio_config = models.TextField(verbose_name='fio测试配置文件')
    iozone_config = models.TextField(verbose_name='iozone测试配置文件')
    jvm2008_config = models.TextField(verbose_name='jvm2008测试配置文件')
    cpu2006_config = models.TextField(verbose_name='cpu2006测试配置文件')
    cpu2006_loongarch64_config = models.TextField(verbose_name='cpu2006_loongarch64测试配置文件')
    cpu2017_config = models.TextField(verbose_name='cpu2017测试配置文件')
    message = models.CharField(max_length=200,verbose_name='描述信息', null=True, blank=True)

    class Meta:
        db_table = 'userConfig'