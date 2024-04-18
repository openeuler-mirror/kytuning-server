from django.db import models
import django.utils.timezone as timezone



# Create your models here.

class Cpu2006(models.Model):
    """cpu2006表"""
    ThreadType = (
        ("单线程", "单线程"),
        ("多线程", "多线程"),
    )
    TuneType = (
        ("base", "base"),
        ("peak", "peak"),
    )
    DType = (
        ("fp", "fp"),
        ("int", "int"),
    )
    env_id = models.IntegerField(verbose_name='环境id')
    thread = models.CharField(choices=ThreadType, max_length=10, verbose_name='线程数')
    execute_cmd = models.CharField(max_length=255, verbose_name='执行命令',null=True, blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True, blank=True)
    dtype = models.CharField(choices=DType, max_length=10, verbose_name='dtype')
    tuneType = models.CharField(choices=TuneType, max_length=10, verbose_name='tune')
    int_400_perlbench = models.FloatField(verbose_name="400.perlbench",null=True,blank=True)
    int_401_bzip2 = models.FloatField(verbose_name="401.bzip2",null=True,blank=True)
    int_403_gcc = models.FloatField(verbose_name="403.gcc",null=True,blank=True)
    int_429_mcf = models.FloatField(verbose_name="429.mcf",null=True,blank=True)
    int_445_gobmk = models.FloatField(verbose_name="445.gobmk",null=True,blank=True)
    int_456_hmmer = models.FloatField(verbose_name="456.hmmer",null=True,blank=True)
    int_458_sjeng = models.FloatField(verbose_name="458.sjeng",null=True,blank=True)
    int_462_libquantum = models.FloatField(verbose_name="462.libquantum",null=True,blank=True)
    int_464_h264ref = models.FloatField(verbose_name="464.h264ref",null=True,blank=True)
    int_471_omnetpp = models.FloatField(verbose_name="471.omnetpp",null=True,blank=True)
    int_473_astar = models.FloatField(verbose_name="473.astar",null=True,blank=True)
    int_483_xalancbmk = models.FloatField(verbose_name="483.xalancbmk",null=True,blank=True)
    int_SPECint_2006 = models.FloatField(verbose_name="SPECint_2006",null=True,blank=True)
    fp_410_bwaves = models.FloatField(verbose_name="410.bwaves",null=True,blank=True)
    fp_416_gamess = models.FloatField(verbose_name="416.gamess",null=True,blank=True)
    fp_433_milc = models.FloatField(verbose_name="433.milc",null=True,blank=True)
    fp_434_zeusmp = models.FloatField(verbose_name="434.zeusmp",null=True,blank=True)
    fp_435_gromacs = models.FloatField(verbose_name="435.gromacs",null=True,blank=True)
    fp_436_cactusADM = models.FloatField(verbose_name="436.cactusADM",null=True,blank=True)
    fp_437_leslie3d = models.FloatField(verbose_name="437.leslie3d",null=True,blank=True)
    fp_444_namd = models.FloatField(verbose_name="444.namd",null=True,blank=True)
    fp_447_dealII = models.FloatField(verbose_name="447.dealII",null=True,blank=True)
    fp_450_soplex = models.FloatField(verbose_name="450.soplex",null=True,blank=True)
    fp_453_povray = models.FloatField(verbose_name="453.povray",null=True,blank=True)
    fp_454_calculix = models.FloatField(verbose_name="454.calculix",null=True,blank=True)
    fp_459_GemsFDTD = models.FloatField(verbose_name="459.GemsFDTD",null=True,blank=True)
    fp_465_tonto = models.FloatField(verbose_name="465.tonto",null=True,blank=True)
    fp_470_lbm = models.FloatField(verbose_name="470.lbm",null=True,blank=True)
    fp_481_wrf = models.FloatField(verbose_name="481.wrf",null=True,blank=True)
    fp_482_sphinx3 = models.FloatField(verbose_name="482.sphinx3",null=True,blank=True)
    fp_SPECfp_2006 = models.FloatField(verbose_name="SPECfp_2006",null=True,blank=True)
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'cpu2006'


