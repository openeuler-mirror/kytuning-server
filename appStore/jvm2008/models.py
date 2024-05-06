from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Jvm2008(models.Model):
    """Jvm2008表"""
    TuneType = (
        ("base", "base"),
        ("peak", "peak"),
    )
    env_id = models.IntegerField(verbose_name='环境id')
    mark_name = models.CharField(max_length=50, verbose_name='文件名称，确保哪两条数据是一组')
    tune_type= models.CharField(choices=TuneType, max_length=10, verbose_name='TuneType')
    execute_cmd = models.CharField(max_length=255, verbose_name='执行命令',null=True,blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True,blank=True)
    compiler = models.FloatField(verbose_name="compiler",null=True,blank=True)
    compress = models.FloatField(verbose_name="compress",null=True,blank=True)
    crypto = models.FloatField(verbose_name="crypto",null=True,blank=True)
    derby = models.FloatField(verbose_name="derby",null=True,blank=True)
    mpegaudio = models.FloatField(verbose_name="mpegaudio",null=True,blank=True)
    scimark_large = models.FloatField(verbose_name="scimark.large",null=True,blank=True)
    scimark_small = models.FloatField(verbose_name="scimark.small",null=True,blank=True)
    serial = models.FloatField(verbose_name="serial",null=True,blank=True)
    startup = models.FloatField(verbose_name="startup",null=True,blank=True)
    sunflow = models.FloatField(verbose_name="sunflow",null=True,blank=True)
    xml = models.FloatField(verbose_name="xml",null=True,blank=True)
    Noncompliant_pomposite_result = models.FloatField(verbose_name="Noncompliant pomposite result",null=True,blank=True)

    class Meta:
        db_table = 'jvm2008'
