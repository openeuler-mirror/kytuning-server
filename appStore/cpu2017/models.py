from django.db import models
import django.utils.timezone as timezone



# Create your models here.

class Cpu2017(models.Model):
    """cpu_2006表"""
    ThreadType = (
        ("单线程", "单线程"),
        ("多线程", "多线程"),
    )
    DType = (
        ("fp", "fp"),
        ("int", "int"),
    )
    TuneType = (
        ("base", "base"),
        ("peak", "peak"),
    )
    env_id = models.IntegerField(verbose_name='环境id')
    thread = models.CharField(choices=ThreadType, max_length=10, verbose_name='线程数')
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    dtype = models.CharField(choices=DType, max_length=10, verbose_name='dtype')
    tuneType = models.CharField(choices=TuneType, max_length=10, verbose_name='tune')
    int_500_perlbench_r = models.FloatField(verbose_name="500.perlbench_r", null=True, blank=True)
    int_502_gcc_r = models.FloatField(verbose_name="502.gcc_r", null=True, blank=True)
    int_505_mcf_r = models.FloatField(verbose_name="505.mcf_r", null=True, blank=True)
    int_520_omnetpp_r = models.FloatField(verbose_name="520.omnetpp_r", null=True, blank=True)
    int_523_xalancbmk_r = models.FloatField(verbose_name="523.xalancbmk_r", null=True, blank=True)
    int_525_x264_r = models.FloatField(verbose_name="525.x264_r", null=True, blank=True)
    int_531_deepsjeng_r = models.FloatField(verbose_name="531.deepsjeng_r", null=True, blank=True)
    int_541_leela_r = models.FloatField(verbose_name="541.leela_r", null=True, blank=True)
    int_548_exchange2_r = models.FloatField(verbose_name="548.exchange2_r", null=True, blank=True)
    int_557_xz_r = models.FloatField(verbose_name="557.xz_r", null=True, blank=True)
    int_SPECrate2017_int = models.FloatField(verbose_name="SPECrate2017_int", null=True, blank=True)
    fp_503_bwaves_r = models.FloatField(verbose_name="503.bwaves_r", null=True, blank=True)
    fp_507_cactuBSSN_r = models.FloatField(verbose_name="507.cactuBSSN_r", null=True, blank=True)
    fp_508_namd_r = models.FloatField(verbose_name="508.namd_r", null=True, blank=True)
    fp_510_parest_r = models.FloatField(verbose_name="510.parest_r", null=True, blank=True)
    fp_511_povray_r = models.FloatField(verbose_name="511.povray_r", null=True, blank=True)
    fp_519_lbm_r = models.FloatField(verbose_name="519.lbm_r", null=True, blank=True)
    fp_521_wrf_r = models.FloatField(verbose_name="521.wrf_r ", null=True, blank=True)
    fp_526_blender_r = models.FloatField(verbose_name="526.blender_r", null=True, blank=True)
    fp_527_cam4_r = models.FloatField(verbose_name="527.cam4_r", null=True, blank=True)
    fp_538_imagick_r = models.FloatField(verbose_name="538.imagick_r", null=True, blank=True)
    fp_544_nab_r = models.FloatField(verbose_name="544.nab_r", null=True, blank=True)
    fp_549_fotonik3d_r = models.FloatField(verbose_name="549.fotonik3d_r", null=True, blank=True)
    fp_554_roms_r = models.FloatField(verbose_name="554.roms_r", null=True, blank=True)
    fp_PECrate2017_fp = models.FloatField(verbose_name="SPECrate2017_fp", null=True, blank=True)
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'cpu_2017'
