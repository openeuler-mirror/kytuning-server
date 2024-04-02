from datetime import datetime

from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Project(models.Model):
    """Project表"""
    env_id = models.IntegerField(verbose_name='环境id')
    user_name = models.CharField(max_length=255, verbose_name='测试人员名称')
    project_name = models.CharField(max_length=255, verbose_name='项目名称')
    arm = models.CharField( max_length=255, verbose_name='架构')
    hwinfo_machineinfo_serialnumber = models.CharField(max_length=255,verbose_name='环境表中的hwinfo_machineinfo_serialnumber')
    os_version = models.CharField(null=True, blank=True, max_length=255, verbose_name='操作系统版本')
    message = models.CharField(null=True, blank=True, max_length=255, verbose_name='项目描述')
    times = models.IntegerField(verbose_name='第几次测试')
    test_time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)
    cpu2006 = models.BooleanField(default=False, verbose_name='cpu2006数据')
    cpu2017 = models.BooleanField(default=False, verbose_name='cpu2017数据')
    fio = models.BooleanField(default=False, verbose_name='fio数据')
    iozone = models.BooleanField(default=False, verbose_name='iozone数据')
    jvm2008 = models.BooleanField(default=False, verbose_name='jvm2008数据')
    lmbench = models.BooleanField(default=False, verbose_name='lmbench数据')
    stream = models.BooleanField(default=False, verbose_name='stream数据')
    unixbench = models.BooleanField(default=False, verbose_name='unxibench数据')

    class Meta:
        db_table = 'project'
