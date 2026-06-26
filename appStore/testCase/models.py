import django.utils.timezone as timezone
from django.db import models

# Create your models here.
class TestCase(models.Model):
    """测试案例表"""
    testType = (
        ("日常测试", "日常测试"),
        ("监控测试", "监控测试"),
        ("自动化分析测试", "自动化测试"),
    )
    test_type = models.CharField(max_length=50, verbose_name='测试类型', choices=testType)
    compar_data = models.TextField(verbose_name='对比数据，用于自动化分析测试', null=True, blank=True)
    kojifile_addr = models.TextField(verbose_name='kojifei地址，用于自动化监控测试', null=True, blank=True)
    iso = models.TextField(verbose_name='用于自动化监控测试自动化安装操作系统', null=True, blank=True)
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
    user_name = models.CharField(max_length=255, verbose_name='测试人员')
    test_result = models.TextField(verbose_name='测试结果反馈', null=True, blank=True)  # 如果有多项也是拼接
    result_log_name = models.CharField(max_length=255, verbose_name='日志文件路径的base部分')
    is_error = models.BooleanField(default=False, verbose_name="是否是错误列表所需要的")
    test_time = models.DateTimeField(verbose_name="记录时间", default=timezone.now)


    class Meta:
        db_table = 'test_case'
