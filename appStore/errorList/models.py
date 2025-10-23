"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:19:26 2024 +0800
"""
from django.db import models

# Create your models here.
class KytuningError(models.Model):
    """错误收集列表"""
    ErrorType = (
        ("编译类型错误", "编译类型错误"),
        ("运行类型错误", "运行类型错误"),
    )
    TestType = (
        ("stream", "stream"),
        ("lmbench", "lmbench"),
        ("unixbench", "unixbench"),
        ("fio", "fio"),
        ("iozone", "iozone"),
        ("jvm2008", "jvm2008"),
        ("cpu2006", "cpu2006"),
        ("cpu2017", "cpu2017"),
        ("other", "other"),
    )
    error_type = models.CharField(choices=ErrorType,max_length=50, verbose_name='错误类型')
    user_name = models.CharField(max_length=250, verbose_name='操作人员')
    test_type = models.CharField(choices=TestType,max_length=50, verbose_name='测试类型')
    error_description = models.CharField(max_length=250, verbose_name='错误描述')
    error_log_excerpt = models.CharField(max_length=250, verbose_name='错误日志节选')
    error_log_path = models.CharField(max_length=250, verbose_name='错误日志路径')
    solution = models.CharField(max_length=50, verbose_name='解决方案')

    class Meta:
        db_table = 'Kytuning_error'