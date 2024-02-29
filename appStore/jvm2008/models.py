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
    base= models.CharField(choices=TuneType, max_length=10, verbose_name='base')
    base_execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='base 执行命令')
    base_modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='base 修改参数')
    base_compiler = models.FloatField(verbose_name="base compiler")
    base_compress = models.FloatField(verbose_name="base compress")
    base_crypto = models.FloatField(verbose_name="base crypto")
    base_derby = models.FloatField(verbose_name="base derby")
    base_mpegaudio = models.FloatField(verbose_name="base mpegaudio")
    base_scimark_large = models.FloatField(verbose_name="base scimark.large")
    base_scimark_small = models.FloatField(verbose_name="base scimark.small")
    base_serial = models.FloatField(verbose_name="base serial")
    base_startup = models.FloatField(verbose_name="base startup")
    base_sunflow = models.FloatField(verbose_name="base sunflow")
    base_xml = models.FloatField(verbose_name="base xml")
    base_Noncompliant_pomposite_result = models.FloatField(verbose_name="base Noncompliant pomposite result")
    base_test_time = models.DateTimeField(verbose_name="base 测试时间", default=timezone.now)
    
    peak = models.CharField(choices=TuneType, max_length=10, verbose_name='peak')
    peak_execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    peak_modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    peak_compiler = models.FloatField(verbose_name="peak compiler")
    peak_compress = models.FloatField(verbose_name="peak compress")
    peak_crypto = models.FloatField(verbose_name="peak crypto")
    peak_derby = models.FloatField(verbose_name="peak derby")
    peak_mpegaudio = models.FloatField(verbose_name="peak mpegaudio")
    peak_scimark_large = models.FloatField(verbose_name="peak scimark.large")
    peak_scimark_small = models.FloatField(verbose_name="peak scimark.small")
    peak_serial = models.FloatField(verbose_name="peak serial")
    peak_startup = models.FloatField(verbose_name="peak startup")
    peak_sunflow = models.FloatField(verbose_name="peak sunflow")
    peak_xml = models.FloatField(verbose_name="peak xml")
    peak_Noncompliant_pomposite_result = models.FloatField(verbose_name="peak Noncompliant pomposite result")
    peak_test_time = models.DateTimeField(verbose_name="peak 测试时间", default=timezone.now)

    class Meta:
        db_table = 'jvm2008'


















