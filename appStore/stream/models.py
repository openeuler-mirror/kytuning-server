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
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    # modify_parameters = models.TextField(null=True, blank=True, verbose_name='修改参数') #如果是很多的化可以使用text文本类型
    single_thread = models.CharField(choices=ThreadType, max_length=10, verbose_name='单线程')
    single_array_size = models.IntegerField(verbose_name='single_array_size')
    single_copy = models.FloatField(verbose_name='single_copy')
    single_scale = models.FloatField(verbose_name='single_scale')
    single_add = models.FloatField(verbose_name='single_add')
    single_triad = models.FloatField(verbose_name='single_triad')
    multi_threading = models.CharField(choices=ThreadType, max_length=10, verbose_name='多线程')
    multi_array_size = models.IntegerField(verbose_name='multi_array_size')
    multi_copy = models.FloatField(verbose_name='multi_copy')
    multi_scale = models.FloatField(verbose_name='multi_scale')
    multi_add = models.FloatField(verbose_name='multi_add')
    multi_triad = models.FloatField(verbose_name='multi_triad')
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'stream'
