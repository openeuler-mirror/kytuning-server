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
    execute_cmd = models.CharField(max_length=255, verbose_name='执行命令',null=True,blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True,blank=True)
    mark_name = models.CharField(max_length=50, verbose_name='文件名称，确保哪两条数据是一组')
    rw = models.CharField(choices=RwType, max_length=20, verbose_name="rw")
    bs = models.CharField(max_length=20, verbose_name="bs")
    io = models.CharField(max_length=20, verbose_name="io")
    iops = models.CharField(max_length=20, verbose_name="iops")
    bw = models.CharField(max_length=20, verbose_name="bw")

    class Meta:
        db_table = 'fio'
