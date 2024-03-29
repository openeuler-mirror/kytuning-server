from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Iozone(models.Model):
    """iozone表"""
    env_id = models.IntegerField(verbose_name='环境id')
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    testcase_name = models.CharField(max_length=10, verbose_name='testcase name') #testcase_name=haif、full、double
    file_size = models.FloatField(verbose_name="文件大小")
    block_size = models.FloatField(verbose_name="块大小")
    Write_test = models.FloatField(verbose_name="写测试（KB/s）")
    Rewrite_test = models.FloatField(verbose_name="重写测试（KB/s）")
    read_test = models.FloatField(verbose_name="读测试（KB/s）")
    reread_test = models.FloatField(verbose_name="重读测试（KB/s）")
    random_read_test = models.FloatField(verbose_name="随机读测试（KB/s）")
    random_write_test = models.FloatField(verbose_name="随机写测试（KB/s）")
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'iozone'
