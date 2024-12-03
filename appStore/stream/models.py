"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:02:58 2024 +0800
"""
from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Stream(models.Model):
    """stream表"""
    ThreadType = (
        ("单线程", "单线程"),
        ("多线程", "多线程"),
    )
    env_id = models.IntegerField(verbose_name='环境id')
    execute_cmd = models.CharField(max_length=255, verbose_name='执行命令',null=True,blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True,blank=True)
    # modify_parameters = models.TextField(null=True, blank=True, verbose_name='修改参数') #如果是很多的化可以使用text文本类型
    single_thread = models.CharField(choices=ThreadType, max_length=10, verbose_name='单线程',null=True,blank=True)
    single_array_size = models.IntegerField(verbose_name='single_array_size',null=True,blank=True)
    single_copy = models.FloatField(verbose_name='single_copy',null=True,blank=True)
    single_scale = models.FloatField(verbose_name='single_scale',null=True,blank=True)
    single_add = models.FloatField(verbose_name='single_add',null=True,blank=True)
    single_triad = models.FloatField(verbose_name='single_triad',null=True,blank=True)
    multi_threading = models.CharField(choices=ThreadType, max_length=10, verbose_name='多线程',null=True,blank=True)
    multi_array_size = models.IntegerField(verbose_name='multi_array_size',null=True,blank=True)
    multi_copy = models.FloatField(verbose_name='multi_copy',null=True,blank=True)
    multi_scale = models.FloatField(verbose_name='multi_scale',null=True,blank=True)
    multi_add = models.FloatField(verbose_name='multi_add',null=True,blank=True)
    multi_triad = models.FloatField(verbose_name='multi_triad',null=True,blank=True)

    class Meta:
        db_table = 'stream'
