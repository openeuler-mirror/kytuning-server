from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Fio(models.Model):
    """fio表"""
    RwType = (
        ("read", "read"),
        ("write", "write"),
        ("randread", "randread"),
        ("randwrite", "randwrite"),
    )
    env_id = models.IntegerField(verbose_name='环境id')
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    rw = models.CharField(choices=RwType, max_length=20, verbose_name="rw")
    bs = models.CharField(max_length=20, verbose_name="bs")
    io = models.CharField(max_length=20, verbose_name="io")
    iops = models.CharField(max_length=20, verbose_name="iops")
    bw = models.CharField(max_length=20, verbose_name="bw")
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'fio'
