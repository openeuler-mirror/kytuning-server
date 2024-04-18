from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Iozone(models.Model):
    """iozone表"""
    env_id = models.IntegerField(verbose_name='环境id')
    execute_cmd = models.CharField(max_length=255, verbose_name='执行命令',null=True,blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True,blank=True)
    testcase_name = models.CharField(max_length=10, verbose_name='testcase name') #testcase_name=haif、full、double
    file_size = models.FloatField(verbose_name="文件大小")
    block_size = models.FloatField(verbose_name="块大小",null=True,blank=True)
    write_test = models.FloatField(verbose_name="写测试（KB/s）",null=True,blank=True)
    rewrite_test = models.FloatField(verbose_name="重写测试（KB/s）",null=True,blank=True)
    read_test = models.FloatField(verbose_name="读测试（KB/s）",null=True,blank=True)
    reread_test = models.FloatField(verbose_name="重读测试（KB/s）",null=True,blank=True)
    random_read_test = models.FloatField(verbose_name="随机读测试（KB/s）",null=True,blank=True)
    random_write_test = models.FloatField(verbose_name="随机写测试（KB/s）",null=True,blank=True)
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'iozone'
