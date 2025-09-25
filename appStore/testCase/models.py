from django.db import models


# Create your models here.
class TestCase(models.Model):
    """测试案例表"""
    ThreadType = (
        ("单线程", "单线程"),
        ("多线程", "多线程"),
    )
    project_name = models.CharField(max_length=50, verbose_name='项目名称')
    ip = models.CharField(max_length=50, verbose_name='IP地址')
    stream = models.IntegerField(default=0, verbose_name='几组stream数据')
    lmbench = models.IntegerField(default=0, verbose_name='几组lmbench数据')
    unixbench = models.IntegerField(default=0, verbose_name='几组unxibench数据')
    fio = models.IntegerField(default=0, verbose_name='几组fio数据')
    iozone = models.IntegerField(default=0, verbose_name='几组iozone数据')
    jvm2008 = models.IntegerField(default=0, verbose_name='几组jvm2008数据')
    cpu2006 = models.IntegerField(default=0, verbose_name='几组cpu2006数据')
    cpu2017 = models.IntegerField(default=0, verbose_name='几组cpu2017数据')
    user_name = models.CharField(max_length=255, verbose_name='测试人员', )
    test_result = models.CharField(max_length=255, verbose_name='测试结果反馈', null=True, blank=True)  # 如果有多项也是拼接
    result_log_name = models.CharField(max_length=255, verbose_name='日志文件名称的base部分')

    class Meta:
        db_table = 'testCase'
