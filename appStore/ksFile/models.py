"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 10:58:36 2024 +0800
"""

from django.db import models

# Create your models here.
class KsFile(models.Model):
    """ks文件列表"""
    ks_name = models.CharField(unique=True, max_length=500, verbose_name='ks文件名称')
    ks_content = models.TextField(verbose_name='ks文件内容')
    user_name = models.CharField(max_length=50, verbose_name='创建人员')

    class Meta:
        db_table = 'ks_file'