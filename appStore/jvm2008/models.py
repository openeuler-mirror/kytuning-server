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
    tune_type= models.CharField(choices=TuneType, max_length=10, verbose_name='TuneType')
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    compiler = models.FloatField(verbose_name="compiler")
    compress = models.FloatField(verbose_name="compress")
    crypto = models.FloatField(verbose_name="crypto")
    derby = models.FloatField(verbose_name="derby")
    mpegaudio = models.FloatField(verbose_name="mpegaudio")
    scimark_large = models.FloatField(verbose_name="scimark.large")
    scimark_small = models.FloatField(verbose_name="scimark.small")
    serial = models.FloatField(verbose_name="serial")
    startup = models.FloatField(verbose_name="startup")
    sunflow = models.FloatField(verbose_name="sunflow")
    xml = models.FloatField(verbose_name="xml")
    Noncompliant_pomposite_result = models.FloatField(verbose_name="Noncompliant pomposite result")

    class Meta:
        db_table = 'jvm2008'


















