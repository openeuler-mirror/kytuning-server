from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Project(models.Model):
    """Project表"""
    env_id = models.IntegerField(verbose_name='环境id')
    project_name = models.CharField(max_length=255, verbose_name='项目名称')
    arm = models.CharField( max_length=255, verbose_name='架构')
    hwinfo_machineinfo_serialnumber = models.CharField(max_length=255,verbose_name='环境表中的hwinfo_machineinfo_serialnumber')
    os_version = models.CharField(null=True, blank=True, max_length=255, verbose_name='操作系统版本')
    times = models.IntegerField(verbose_name='第几次测试')
    test_time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)

    class Meta:
        db_table = 'project'
