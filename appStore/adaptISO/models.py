"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:02:58 2024 +0800
"""
from django.db import models

# Create your models here.
class AdaptISO(models.Model):
    """适配ISO列表"""
    ARCH_NAME_TYPE = (
        ("aarch", "aarch"),
        ("x86", "x86"),
    )
    ISO_name = models.CharField(unique=True, max_length=500, verbose_name='ISO名称')
    http_address = models.CharField(max_length=500, verbose_name='ISO下载地址')
    arch_name = models.CharField(choices=ARCH_NAME_TYPE,max_length=50, verbose_name='架构')
    user_name = models.CharField(max_length=50, verbose_name='适配人员')
    ks_file_name = models.CharField(max_length=1000, verbose_name='ks文件地址及名称')

    class Meta:
        db_table = 'adapt_iso'