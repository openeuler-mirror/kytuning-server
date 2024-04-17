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
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    Dhrystone = models.FloatField(verbose_name='Dhrystone 2 using register variables(lps)')
    Double_Precision = models.FloatField(verbose_name='Double-Precision Whetstone(MWIPS)')
    execl_throughput = models.FloatField(verbose_name='Execl Throughput(lps)')
    file_copy_1024 = models.FloatField(verbose_name='File Copy 1024 bufsize 2000 maxblocks(KBps)')
    file_copy_256 = models.FloatField(verbose_name='File Copy 256 bufsize 500 maxblocks(KBps)')
    file_copy_4096 = models.FloatField(verbose_name='File Copy 4096 bufsize 8000 maxblocks(KBps)')
    pipe_throughput = models.FloatField(verbose_name='Pipe Throughput(lps)')
    pipe_based = models.FloatField(verbose_name='Pipe-based Context Switching(lps)')
    process_creation = models.FloatField(verbose_name='Process Creation(lps)')
    shell_scripts_1 = models.FloatField(verbose_name='Shell Scripts (1 concurrent)(lpm)')
    shell_scripts_8 = models.FloatField(verbose_name='Shell Scripts (8 concurrent)(lpm)')
    system_call_overhead = models.FloatField(verbose_name='System Call Overhead(lps)')
    index_score = models.FloatField(verbose_name='Index Score(sum)')
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)
    # multi_thread = models.CharField(choices=ThreadType, max_length=10, verbose_name='多线程')
    # multi_execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    # multi_modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    # # modify_parameters = models.TextField(null=True, blank=True, verbose_name='修改参数') #如果是很多的化可以使用text文本类型
    # multi_Dhrystone = models.FloatField(verbose_name='multi Dhrystone 2 using register variables(lps)')
    # multi_Double_Precision = models.FloatField(verbose_name='multi Double-Precision Whetstone(MWIPS)')
    # multi_execl_throughput = models.FloatField(verbose_name='multi Execl Throughput(lps)')
    # multi_file_copy_1024 = models.FloatField(verbose_name='multi File Copy 1024 bufsize 2000 maxblocks(KBps)')
    # multi_file_copy_256 = models.FloatField(verbose_name='multi File Copy 256 bufsize 500 maxblocks(KBps)')
    # multi_file_copy_4096 = models.FloatField(verbose_name='multi File Copy 4096 bufsize 8000 maxblocks(KBps)')
    # multi_pipe_throughput = models.FloatField(verbose_name='multi Pipe Throughput(lps)')
    # multi_pipe_based = models.FloatField(verbose_name='multi Pipe-based Context Switching(lps)')
    # multi_process_creation = models.FloatField(verbose_name='multi Process Creation(lps)')
    # multi_shell_scripts_1 = models.FloatField(verbose_name='multi Shell Scripts (1 concurrent)(lpm)')
    # multi_shell_scripts_8 = models.FloatField(verbose_name='multi Shell Scripts (8 concurrent)(lpm)')
    # multi_system_call_overhead = models.FloatField(verbose_name='multi System Call Overhead(lps)')
    # multi_index_score = models.FloatField(verbose_name='multi Index Score(sum)')
    # multi_test_time = models.DateTimeField(verbose_name="multi 测试时间", default=timezone.now)


    class Meta:
        db_table = 'unixbench'
