from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Unixbench(models.Model):
    """cpu_2006表"""
    ThreadType = (
        ("单线程", "单线程"),
        ("多线程", "多线程"),
    )
    env_id = models.IntegerField(verbose_name='环境id')
    thread = models.CharField(choices=ThreadType, max_length=10, verbose_name='线程数')
    mark_name = models.CharField(max_length=50, verbose_name='文件名称，确保哪两条数据是一组')
    execute_cmd = models.CharField(max_length=255, verbose_name='执行命令',null=True,blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True,blank=True)
    Dhrystone = models.FloatField(verbose_name='Dhrystone 2 using register variables(lps)',null=True,blank=True)
    Double_Precision = models.FloatField(verbose_name='Double-Precision Whetstone(MWIPS)',null=True,blank=True)
    execl_throughput = models.FloatField(verbose_name='Execl Throughput(lps)',null=True,blank=True)
    file_copy_1024 = models.FloatField(verbose_name='File Copy 1024 bufsize 2000 maxblocks(KBps)',null=True,blank=True)
    file_copy_256 = models.FloatField(verbose_name='File Copy 256 bufsize 500 maxblocks(KBps)',null=True,blank=True)
    file_copy_4096 = models.FloatField(verbose_name='File Copy 4096 bufsize 8000 maxblocks(KBps)',null=True,blank=True)
    pipe_throughput = models.FloatField(verbose_name='Pipe Throughput(lps)',null=True,blank=True)
    pipe_based = models.FloatField(verbose_name='Pipe-based Context Switching(lps)',null=True,blank=True)
    process_creation = models.FloatField(verbose_name='Process Creation(lps)',null=True,blank=True)
    shell_scripts_1 = models.FloatField(verbose_name='Shell Scripts (1 concurrent)(lpm)',null=True,blank=True)
    shell_scripts_8 = models.FloatField(verbose_name='Shell Scripts (8 concurrent)(lpm)',null=True,blank=True)
    system_call_overhead = models.FloatField(verbose_name='System Call Overhead(lps)',null=True,blank=True)
    index_score = models.FloatField(verbose_name='Index Score(sum)',null=True,blank=True)
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'unixbench'
