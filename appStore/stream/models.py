from datetime import datetime

from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Project(models.Model):
    """Project表"""
    env_id = models.IntegerField(verbose_name='环境id')
    user_name = models.CharField(max_length=255, verbose_name='测试人员名称')
    project_name = models.CharField(max_length=255, verbose_name='项目名称',null=True,blank=True)
    arm = models.CharField( max_length=255, verbose_name='架构',null=True,blank=True)
    hwinfo_machineinfo_serialnumber = models.CharField(max_length=255,verbose_name='环境表中的hwinfo_machineinfo_serialnumber',null=True,blank=True)
    os_version = models.CharField(max_length=255, verbose_name='操作系统版本',null=True,blank=True)
    message = models.CharField(max_length=255, verbose_name='项目描述',null=True,blank=True)
    times = models.IntegerField(verbose_name='第几次测试')
    cpu2006 = models.BooleanField(default=False, verbose_name='cpu2006数据')
    cpu2017 = models.BooleanField(default=False, verbose_name='cpu2017数据')
    fio = models.BooleanField(default=False, verbose_name='fio数据')
    iozone = models.BooleanField(default=False, verbose_name='iozone数据')
    jvm2008 = models.BooleanField(default=False, verbose_name='jvm2008数据')
    lmbench = models.BooleanField(default=False, verbose_name='lmbench数据')
    stream = models.BooleanField(default=False, verbose_name='stream数据')
    unixbench = models.BooleanField(default=False, verbose_name='unxibench数据')
    test_time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)

    class Meta:
        db_table = 'project'
