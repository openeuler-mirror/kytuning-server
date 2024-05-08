import numpy as np

# Create your views here.
from rest_framework import status

from appStore.cpu2006.models import Cpu2006
from appStore.cpu2006.serializers import Cpu2006Serializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class Cpu2006ViewSet(CusModelViewSet):
    """
    Cpu2006数据管理
    """
    queryset = Cpu2006.objects.all().order_by('id')
    serializer_class = Cpu2006Serializer

    # def list(self, request, *args, **kwargs):
    #     """
    #     返回列表
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     env_id = request.GET.get('env_id')
    #     queryset = Cpu2006.objects.filter(env_id=env_id).all()
    #     queryset = self.filter_queryset(queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return json_response(serializer.data, status.HTTP_200_OK, '列表')

    def get_data(self, serializer_):
        serializer = self.get_serializer(serializer_, many=True)
        # 初始化数据为空 否则如果下面只获取的单线程或者多线程另外一组获取不到可能会报错
        execute_cmd = serializer.data[0]['execute_cmd']
        modify_parameters = serializer.data[0]['modify_parameters']

        base_single_int_400_perlbench = ''
        base_single_int_401_bzip2 = ''
        base_single_int_403_gcc = ''
        base_single_int_429_mcf = ''
        base_single_int_445_gobmk = ''
        base_single_int_456_hmmer = ''
        base_single_int_458_sjeng = ''
        base_single_int_462_libquantum = ''
        base_single_int_464_h264ref = ''
        base_single_int_471_omnetpp = ''
        base_single_int_473_astar = ''
        base_single_int_483_xalancbmk = ''
        base_single_int_SPECint_2006 = ''
        base_single_fp_410_bwaves = ''
        base_single_fp_416_gamess = ''
        base_single_fp_433_milc = ''
        base_single_fp_434_zeusmp = ''
        base_single_fp_435_gromacs = ''
        base_single_fp_436_cactusADM = ''
        base_single_fp_437_leslie3d = ''
        base_single_fp_444_namd = ''
        base_single_fp_447_dealII = ''
        base_single_fp_450_soplex = ''
        base_single_fp_453_povray = ''
        base_single_fp_454_calculix = ''
        base_single_fp_459_GemsFDTD = ''
        base_single_fp_465_tonto = ''
        base_single_fp_470_lbm = ''
        base_single_fp_481_wrf = ''
        base_single_fp_482_sphinx3 = ''
        base_single_fp_SPECfp_2006 = ''

        base_multi_int_400_perlbench = ''
        base_multi_int_401_bzip2 = ''
        base_multi_int_403_gcc = ''
        base_multi_int_429_mcf = ''
        base_multi_int_445_gobmk = ''
        base_multi_int_456_hmmer = ''
        base_multi_int_458_sjeng = ''
        base_multi_int_462_libquantum = ''
        base_multi_int_464_h264ref = ''
        base_multi_int_471_omnetpp = ''
        base_multi_int_473_astar = ''
        base_multi_int_483_xalancbmk = ''
        base_multi_int_SPECint_2006 = ''
        base_multi_fp_410_bwaves = ''
        base_multi_fp_416_gamess = ''
        base_multi_fp_433_milc = ''
        base_multi_fp_434_zeusmp = ''
        base_multi_fp_435_gromacs = ''
        base_multi_fp_436_cactusADM = ''
        base_multi_fp_437_leslie3d = ''
        base_multi_fp_444_namd = ''
        base_multi_fp_447_dealII = ''
        base_multi_fp_450_soplex = ''
        base_multi_fp_453_povray = ''
        base_multi_fp_454_calculix = ''
        base_multi_fp_459_GemsFDTD = ''
        base_multi_fp_465_tonto = ''
        base_multi_fp_470_lbm = ''
        base_multi_fp_481_wrf = ''
        base_multi_fp_482_sphinx3 = ''
        base_multi_fp_SPECfp_2006 = ''

        peak_single_int_400_perlbench = ''
        peak_single_int_401_bzip2 = ''
        peak_single_int_403_gcc = ''
        peak_single_int_429_mcf = ''
        peak_single_int_445_gobmk = ''
        peak_single_int_456_hmmer = ''
        peak_single_int_458_sjeng = ''
        peak_single_int_462_libquantum = ''
        peak_single_int_464_h264ref = ''
        peak_single_int_471_omnetpp = ''
        peak_single_int_473_astar = ''
        peak_single_int_483_xalancbmk = ''
        peak_single_int_SPECint_2006 = ''
        peak_single_fp_410_bwaves = ''
        peak_single_fp_416_gamess = ''
        peak_single_fp_433_milc = ''
        peak_single_fp_434_zeusmp = ''
        peak_single_fp_435_gromacs = ''
        peak_single_fp_436_cactusADM = ''
        peak_single_fp_437_leslie3d = ''
        peak_single_fp_444_namd = ''
        peak_single_fp_447_dealII = ''
        peak_single_fp_450_soplex = ''
        peak_single_fp_453_povray = ''
        peak_single_fp_454_calculix = ''
        peak_single_fp_459_GemsFDTD = ''
        peak_single_fp_465_tonto = ''
        peak_single_fp_470_lbm = ''
        peak_single_fp_481_wrf = ''
        peak_single_fp_482_sphinx3 = ''
        peak_single_fp_SPECfp_2006 = ''

        peak_multi_int_400_perlbench = ''
        peak_multi_int_401_bzip2 = ''
        peak_multi_int_403_gcc = ''
        peak_multi_int_429_mcf = ''
        peak_multi_int_445_gobmk = ''
        peak_multi_int_456_hmmer = ''
        peak_multi_int_458_sjeng = ''
        peak_multi_int_462_libquantum = ''
        peak_multi_int_464_h264ref = ''
        peak_multi_int_471_omnetpp = ''
        peak_multi_int_473_astar = ''
        peak_multi_int_483_xalancbmk = ''
        peak_multi_int_SPECint_2006 = ''
        peak_multi_fp_410_bwaves = ''
        peak_multi_fp_416_gamess = ''
        peak_multi_fp_433_milc = ''
        peak_multi_fp_434_zeusmp = ''
        peak_multi_fp_435_gromacs = ''
        peak_multi_fp_436_cactusADM = ''
        peak_multi_fp_437_leslie3d = ''
        peak_multi_fp_444_namd = ''
        peak_multi_fp_447_dealII = ''
        peak_multi_fp_450_soplex = ''
        peak_multi_fp_453_povray = ''
        peak_multi_fp_454_calculix = ''
        peak_multi_fp_459_GemsFDTD = ''
        peak_multi_fp_465_tonto = ''
        peak_multi_fp_470_lbm = ''
        peak_multi_fp_481_wrf = ''
        peak_multi_fp_482_sphinx3 = ''
        peak_multi_fp_SPECfp_2006 = ''

        # thread dtype tuneType
        # 先判断数据的TuneType确定是base还是peak
        # 在判断数据的thread确定是单线程还是多线程
        # 在判断tuneType确定是int还是fp
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            for data in serializer.data:
                # 判断数据的TuneType确定是base还是peak
                if data['tuneType'] == 'base':
                    if data['thread'] == '单线程':
                        if data['dtype'] == 'int':
                            base_single_int_400_perlbench = data['int_400_perlbench']
                            base_single_int_401_bzip2 = data['int_401_bzip2']
                            base_single_int_403_gcc = data['int_403_gcc']
                            base_single_int_429_mcf = data['int_429_mcf']
                            base_single_int_445_gobmk = data['int_445_gobmk']
                            base_single_int_456_hmmer = data['int_456_hmmer']
                            base_single_int_458_sjeng = data['int_458_sjeng']
                            base_single_int_462_libquantum = data['int_462_libquantum']
                            base_single_int_464_h264ref = data['int_464_h264ref']
                            base_single_int_471_omnetpp = data['int_471_omnetpp']
                            base_single_int_473_astar = data['int_473_astar']
                            base_single_int_483_xalancbmk = data['int_483_xalancbmk']
                            base_single_int_SPECint_2006 = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            base_single_fp_410_bwaves = data['fp_410_bwaves']
                            base_single_fp_416_gamess = data['fp_416_gamess']
                            base_single_fp_433_milc = data['fp_433_milc']
                            base_single_fp_434_zeusmp = data['fp_434_zeusmp']
                            base_single_fp_435_gromacs = data['fp_435_gromacs']
                            base_single_fp_436_cactusADM = data['fp_436_cactusADM']
                            base_single_fp_437_leslie3d = data['fp_437_leslie3d']
                            base_single_fp_444_namd = data['fp_444_namd']
                            base_single_fp_447_dealII = data['fp_447_dealII']
                            base_single_fp_450_soplex = data['fp_450_soplex']
                            base_single_fp_453_povray = data['fp_453_povray']
                            base_single_fp_454_calculix = data['fp_454_calculix']
                            base_single_fp_459_GemsFDTD = data['fp_459_GemsFDTD']
                            base_single_fp_465_tonto = data['fp_465_tonto']
                            base_single_fp_470_lbm = data['fp_470_lbm']
                            base_single_fp_481_wrf = data['fp_481_wrf']
                            base_single_fp_482_sphinx3 = data['fp_482_sphinx3']
                            base_single_fp_SPECfp_2006 = data['fp_SPECfp_2006']
                    elif data['thread'] == '多线程':
                        if data['dtype'] == 'int':
                            base_multi_int_400_perlbench = data['int_400_perlbench']
                            base_multi_int_401_bzip2 = data['int_401_bzip2']
                            base_multi_int_403_gcc = data['int_403_gcc']
                            base_multi_int_429_mcf = data['int_429_mcf']
                            base_multi_int_445_gobmk = data['int_445_gobmk']
                            base_multi_int_456_hmmer = data['int_456_hmmer']
                            base_multi_int_458_sjeng = data['int_458_sjeng']
                            base_multi_int_462_libquantum = data['int_462_libquantum']
                            base_multi_int_464_h264ref = data['int_464_h264ref']
                            base_multi_int_471_omnetpp = data['int_471_omnetpp']
                            base_multi_int_473_astar = data['int_473_astar']
                            base_multi_int_483_xalancbmk = data['int_483_xalancbmk']
                            base_multi_int_SPECint_2006 = data['int_SPECint_2006']

                        elif data['dtype'] == 'fp':
                            base_multi_fp_410_bwaves = data['fp_410_bwaves']
                            base_multi_fp_416_gamess = data['fp_416_gamess']
                            base_multi_fp_433_milc = data['fp_433_milc']
                            base_multi_fp_434_zeusmp = data['fp_434_zeusmp']
                            base_multi_fp_435_gromacs = data['fp_435_gromacs']
                            base_multi_fp_436_cactusADM = data['fp_436_cactusADM']
                            base_multi_fp_437_leslie3d = data['fp_437_leslie3d']
                            base_multi_fp_444_namd = data['fp_444_namd']
                            base_multi_fp_447_dealII = data['fp_447_dealII']
                            base_multi_fp_450_soplex = data['fp_450_soplex']
                            base_multi_fp_453_povray = data['fp_453_povray']
                            base_multi_fp_454_calculix = data['fp_454_calculix']
                            base_multi_fp_459_GemsFDTD = data['fp_459_GemsFDTD']
                            base_multi_fp_465_tonto = data['fp_465_tonto']
                            base_multi_fp_470_lbm = data['fp_470_lbm']
                            base_multi_fp_481_wrf = data['fp_481_wrf']
                            base_multi_fp_482_sphinx3 = data['fp_482_sphinx3']
                            base_multi_fp_SPECfp_2006 = data['fp_SPECfp_2006']
                elif data['tuneType'] == 'peak':
                    if data['thread'] == '单线程':
                        if data['dtype'] == 'int':
                            peak_single_int_400_perlbench = data['int_400_perlbench']
                            peak_single_int_401_bzip2 = data['int_401_bzip2']
                            peak_single_int_403_gcc = data['int_403_gcc']
                            peak_single_int_429_mcf = data['int_429_mcf']
                            peak_single_int_445_gobmk = data['int_445_gobmk']
                            peak_single_int_456_hmmer = data['int_456_hmmer']
                            peak_single_int_458_sjeng = data['int_458_sjeng']
                            peak_single_int_462_libquantum = data['int_462_libquantum']
                            peak_single_int_464_h264ref = data['int_464_h264ref']
                            peak_single_int_471_omnetpp = data['int_471_omnetpp']
                            peak_single_int_473_astar = data['int_473_astar']
                            peak_single_int_483_xalancbmk = data['int_483_xalancbmk']
                            peak_single_int_SPECint_2006 = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            peak_single_fp_410_bwaves = data['fp_410_bwaves']
                            peak_single_fp_416_gamess = data['fp_416_gamess']
                            peak_single_fp_433_milc = data['fp_433_milc']
                            peak_single_fp_434_zeusmp = data['fp_434_zeusmp']
                            peak_single_fp_435_gromacs = data['fp_435_gromacs']
                            peak_single_fp_436_cactusADM = data['fp_436_cactusADM']
                            peak_single_fp_437_leslie3d = data['fp_437_leslie3d']
                            peak_single_fp_444_namd = data['fp_444_namd']
                            peak_single_fp_447_dealII = data['fp_447_dealII']
                            peak_single_fp_450_soplex = data['fp_450_soplex']
                            peak_single_fp_453_povray = data['fp_453_povray']
                            peak_single_fp_454_calculix = data['fp_454_calculix']
                            peak_single_fp_459_GemsFDTD = data['fp_459_GemsFDTD']
                            peak_single_fp_465_tonto = data['fp_465_tonto']
                            peak_single_fp_470_lbm = data['fp_470_lbm']
                            peak_single_fp_481_wrf = data['fp_481_wrf']
                            peak_single_fp_482_sphinx3 = data['fp_482_sphinx3']
                            peak_single_fp_SPECfp_2006 = data['fp_SPECfp_2006']
                    elif data['thread'] == '多线程':
                        if data['dtype'] == 'int':
                            peak_multi_int_400_perlbench = data['int_400_perlbench']
                            peak_multi_int_401_bzip2 = data['int_401_bzip2']
                            peak_multi_int_403_gcc = data['int_403_gcc']
                            peak_multi_int_429_mcf = data['int_429_mcf']
                            peak_multi_int_445_gobmk = data['int_445_gobmk']
                            peak_multi_int_456_hmmer = data['int_456_hmmer']
                            peak_multi_int_458_sjeng = data['int_458_sjeng']
                            peak_multi_int_462_libquantum = data['int_462_libquantum']
                            peak_multi_int_464_h264ref = data['int_464_h264ref']
                            peak_multi_int_471_omnetpp = data['int_471_omnetpp']
                            peak_multi_int_473_astar = data['int_473_astar']
                            peak_multi_int_483_xalancbmk = data['int_483_xalancbmk']
                            peak_multi_int_SPECint_2006 = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            peak_multi_fp_410_bwaves = data['fp_410_bwaves']
                            peak_multi_fp_416_gamess = data['fp_416_gamess']
                            peak_multi_fp_433_milc = data['fp_433_milc']
                            peak_multi_fp_434_zeusmp = data['fp_434_zeusmp']
                            peak_multi_fp_435_gromacs = data['fp_435_gromacs']
                            peak_multi_fp_436_cactusADM = data['fp_436_cactusADM']
                            peak_multi_fp_437_leslie3d = data['fp_437_leslie3d']
                            peak_multi_fp_444_namd = data['fp_444_namd']
                            peak_multi_fp_447_dealII = data['fp_447_dealII']
                            peak_multi_fp_450_soplex = data['fp_450_soplex']
                            peak_multi_fp_453_povray = data['fp_453_povray']
                            peak_multi_fp_454_calculix = data['fp_454_calculix']
                            peak_multi_fp_459_GemsFDTD = data['fp_459_GemsFDTD']
                            peak_multi_fp_465_tonto = data['fp_465_tonto']
                            peak_multi_fp_470_lbm = data['fp_470_lbm']
                            peak_multi_fp_481_wrf = data['fp_481_wrf']
                            peak_multi_fp_482_sphinx3 = data['fp_482_sphinx3']
                            peak_multi_fp_SPECfp_2006 = data['fp_SPECfp_2006']
        else:
            base_single_data_ = serializer_.filter(tuneType='base').filter(thread='单线程')
            base_multi_data_ = serializer_.filter(tuneType='base').filter(thread='多线程')
            peak_single_data_ = serializer_.filter(tuneType='peak').filter(thread='单线程')
            peak_multi_data_ = serializer_.filter(tuneType='peak').filter(thread='多线程')

            # 将每个字典转换为NumPy数组
            base_single_int_400_perlbench_list = [d.int_400_perlbench for d in base_single_data_ if d.int_400_perlbench is not None]
            base_single_int_401_bzip2_list = [d.int_401_bzip2 for d in base_single_data_ if d.int_401_bzip2 is not None]
            base_single_int_403_gcc_list = [d.int_403_gcc for d in base_single_data_ if d.int_403_gcc is not None]
            base_single_int_429_mcf_list = [d.int_429_mcf for d in base_single_data_ if d.int_429_mcf is not None]
            base_single_int_445_gobmk_list = [d.int_445_gobmk for d in base_single_data_ if d.int_445_gobmk is not None]
            base_single_int_456_hmmer_list = [d.int_456_hmmer for d in base_single_data_ if d.int_456_hmmer is not None]
            base_single_int_458_sjeng_list = [d.int_458_sjeng for d in base_single_data_ if d.int_458_sjeng is not None]
            base_single_int_462_libquantum_list = [d.int_462_libquantum for d in base_single_data_ if d.int_462_libquantum is not None]
            base_single_int_464_h264ref_list = [d.int_464_h264ref for d in base_single_data_ if d.int_464_h264ref is not None]
            base_single_int_471_omnetpp_list = [d.int_471_omnetpp for d in base_single_data_ if d.int_471_omnetpp is not None]
            base_single_int_473_astar_list = [d.int_473_astar for d in base_single_data_ if d.int_473_astar is not None]
            base_single_int_483_xalancbmk_list = [d.int_483_xalancbmk for d in base_single_data_ if d.int_483_xalancbmk is not None]
            base_single_int_SPECint_2006_list = [d.int_SPECint_2006 for d in base_single_data_ if d.int_SPECint_2006 is not None]
            base_single_fp_410_bwaves_list = [d.fp_410_bwaves for d in base_single_data_ if d.fp_410_bwaves is not None]
            base_single_fp_416_gamess_list = [d.fp_416_gamess for d in base_single_data_ if d.fp_416_gamess is not None]
            base_single_fp_433_milc_list = [d.fp_433_milc for d in base_single_data_ if d.fp_433_milc is not None]
            base_single_fp_434_zeusmp_list = [d.fp_434_zeusmp for d in base_single_data_ if d.fp_434_zeusmp is not None]
            base_single_fp_435_gromacs_list = [d.fp_435_gromacs for d in base_single_data_ if d.fp_435_gromacs is not None]
            base_single_fp_436_cactusADM_list = [d.fp_436_cactusADM for d in base_single_data_ if d.fp_436_cactusADM is not None]
            base_single_fp_437_leslie3d_list = [d.fp_437_leslie3d for d in base_single_data_ if d.fp_437_leslie3d is not None]
            base_single_fp_444_namd_list = [d.fp_444_namd for d in base_single_data_ if d.fp_444_namd is not None]
            base_single_fp_447_dealII_list = [d.fp_447_dealII for d in base_single_data_ if d.fp_447_dealII is not None]
            base_single_fp_450_soplex_list = [d.fp_450_soplex for d in base_single_data_ if d.fp_450_soplex is not None]
            base_single_fp_453_povray_list = [d.fp_453_povray for d in base_single_data_ if d.fp_453_povray is not None]
            base_single_fp_454_calculix_list = [d.fp_454_calculix for d in base_single_data_ if d.fp_454_calculix is not None]
            base_single_fp_459_GemsFDTD_list = [d.fp_459_GemsFDTD for d in base_single_data_ if d.fp_459_GemsFDTD is not None]
            base_single_fp_465_tonto_list = [d.fp_465_tonto for d in base_single_data_ if d.fp_465_tonto is not None]
            base_single_fp_470_lbm_list = [d.fp_470_lbm for d in base_single_data_ if d.fp_470_lbm is not None]
            base_single_fp_481_wrf_list = [d.fp_481_wrf for d in base_single_data_ if d.fp_481_wrf is not None]
            base_single_fp_482_sphinx3_list = [d.fp_482_sphinx3 for d in base_single_data_ if d.fp_482_sphinx3 is not None]
            base_single_fp_SPECfp_2006_list = [d.fp_SPECfp_2006 for d in base_single_data_ if d.fp_SPECfp_2006 is not None]
            base_multi_int_400_perlbench_list = [d.int_400_perlbench for d in base_multi_data_ if d.int_400_perlbench is not None]
            base_multi_int_401_bzip2_list = [d.int_401_bzip2 for d in base_multi_data_ if d.int_401_bzip2 is not None]
            base_multi_int_403_gcc_list = [d.int_403_gcc for d in base_multi_data_ if d.int_403_gcc is not None]
            base_multi_int_429_mcf_list = [d.int_429_mcf for d in base_multi_data_ if d.int_429_mcf is not None]
            base_multi_int_445_gobmk_list = [d.int_445_gobmk for d in base_multi_data_ if d.int_445_gobmk is not None]
            base_multi_int_456_hmmer_list = [d.int_456_hmmer for d in base_multi_data_ if d.int_456_hmmer is not None]
            base_multi_int_458_sjeng_list = [d.int_458_sjeng for d in base_multi_data_ if d.int_458_sjeng is not None]
            base_multi_int_462_libquantum_list = [d.int_462_libquantum for d in base_multi_data_ if d.int_462_libquantum is not None]
            base_multi_int_464_h264ref_list = [d.int_464_h264ref for d in base_multi_data_ if d.int_464_h264ref is not None]
            base_multi_int_471_omnetpp_list = [d.int_471_omnetpp for d in base_multi_data_ if d.int_471_omnetpp is not None]
            base_multi_int_473_astar_list = [d.int_473_astar for d in base_multi_data_ if d.int_473_astar is not None]
            base_multi_int_483_xalancbmk_list = [d.int_483_xalancbmk for d in base_multi_data_ if d.int_483_xalancbmk is not None]
            base_multi_int_SPECint_2006_list = [d.int_SPECint_2006 for d in base_multi_data_ if d.int_SPECint_2006 is not None]
            base_multi_fp_410_bwaves_list = [d.fp_410_bwaves for d in base_multi_data_ if d.fp_410_bwaves is not None]
            base_multi_fp_416_gamess_list = [d.fp_416_gamess for d in base_multi_data_ if d.fp_416_gamess is not None]
            base_multi_fp_433_milc_list = [d.fp_433_milc for d in base_multi_data_ if d.fp_433_milc is not None]
            base_multi_fp_434_zeusmp_list = [d.fp_434_zeusmp for d in base_multi_data_ if d.fp_434_zeusmp is not None]
            base_multi_fp_435_gromacs_list = [d.fp_435_gromacs for d in base_multi_data_ if d.fp_435_gromacs is not None]
            base_multi_fp_436_cactusADM_list = [d.fp_436_cactusADM for d in base_multi_data_ if d.fp_436_cactusADM is not None]
            base_multi_fp_437_leslie3d_list = [d.fp_437_leslie3d for d in base_multi_data_ if d.fp_437_leslie3d is not None]
            base_multi_fp_444_namd_list = [d.fp_444_namd for d in base_multi_data_ if d.fp_444_namd is not None]
            base_multi_fp_447_dealII_list = [d.fp_447_dealII for d in base_multi_data_ if d.fp_447_dealII is not None]
            base_multi_fp_450_soplex_list = [d.fp_450_soplex for d in base_multi_data_ if d.fp_450_soplex is not None]
            base_multi_fp_453_povray_list = [d.fp_453_povray for d in base_multi_data_ if d.fp_453_povray is not None]
            base_multi_fp_454_calculix_list = [d.fp_454_calculix for d in base_multi_data_ if d.fp_454_calculix is not None]
            base_multi_fp_459_GemsFDTD_list = [d.fp_459_GemsFDTD for d in base_multi_data_ if d.fp_459_GemsFDTD is not None]
            base_multi_fp_465_tonto_list = [d.fp_465_tonto for d in base_multi_data_ if d.fp_465_tonto is not None]
            base_multi_fp_470_lbm_list = [d.fp_470_lbm for d in base_multi_data_ if d.fp_470_lbm is not None]
            base_multi_fp_481_wrf_list = [d.fp_481_wrf for d in base_multi_data_ if d.fp_481_wrf is not None]
            base_multi_fp_482_sphinx3_list = [d.fp_482_sphinx3 for d in base_multi_data_ if d.fp_482_sphinx3 is not None]
            base_multi_fp_SPECfp_2006_list = [d.fp_SPECfp_2006 for d in base_multi_data_ if d.fp_SPECfp_2006 is not None]
            peak_single_int_400_perlbench_list = [d.int_400_perlbench for d in peak_single_data_ if d.int_400_perlbench is not None]
            peak_single_int_401_bzip2_list = [d.int_401_bzip2 for d in peak_single_data_ if d.int_401_bzip2 is not None]
            peak_single_int_403_gcc_list = [d.int_403_gcc for d in peak_single_data_ if d.int_403_gcc is not None]
            peak_single_int_429_mcf_list = [d.int_429_mcf for d in peak_single_data_ if d.int_429_mcf is not None]
            peak_single_int_445_gobmk_list = [d.int_445_gobmk for d in peak_single_data_ if d.int_445_gobmk is not None]
            peak_single_int_456_hmmer_list = [d.int_456_hmmer for d in peak_single_data_ if d.int_456_hmmer is not None]
            peak_single_int_458_sjeng_list = [d.int_458_sjeng for d in peak_single_data_ if d.int_458_sjeng is not None]
            peak_single_int_462_libquantum_list = [d.int_462_libquantum for d in peak_single_data_ if d.int_462_libquantum is not None]
            peak_single_int_464_h264ref_list = [d.int_464_h264ref for d in peak_single_data_ if d.int_464_h264ref is not None]
            peak_single_int_471_omnetpp_list = [d.int_471_omnetpp for d in peak_single_data_ if d.int_471_omnetpp is not None]
            peak_single_int_473_astar_list = [d.int_473_astar for d in peak_single_data_ if d.int_473_astar is not None]
            peak_single_int_483_xalancbmk_list = [d.int_483_xalancbmk for d in peak_single_data_ if d.int_483_xalancbmk is not None]
            peak_single_int_SPECint_2006_list = [d.int_SPECint_2006 for d in peak_single_data_ if d.int_SPECint_2006 is not None]
            peak_single_fp_410_bwaves_list = [d.fp_410_bwaves for d in peak_single_data_ if d.fp_410_bwaves is not None]
            peak_single_fp_416_gamess_list = [d.fp_416_gamess for d in peak_single_data_ if d.fp_416_gamess is not None]
            peak_single_fp_433_milc_list = [d.fp_433_milc for d in peak_single_data_ if d.fp_433_milc is not None]
            peak_single_fp_434_zeusmp_list = [d.fp_434_zeusmp for d in peak_single_data_ if d.fp_434_zeusmp is not None]
            peak_single_fp_435_gromacs_list = [d.fp_435_gromacs for d in peak_single_data_ if d.fp_435_gromacs is not None]
            peak_single_fp_436_cactusADM_list = [d.fp_436_cactusADM for d in peak_single_data_ if d.fp_436_cactusADM is not None]
            peak_single_fp_437_leslie3d_list = [d.fp_437_leslie3d for d in peak_single_data_ if d.fp_437_leslie3d is not None]
            peak_single_fp_444_namd_list = [d.fp_444_namd for d in peak_single_data_ if d.fp_444_namd is not None]
            peak_single_fp_447_dealII_list = [d.fp_447_dealII for d in peak_single_data_ if d.fp_447_dealII is not None]
            peak_single_fp_450_soplex_list = [d.fp_450_soplex for d in peak_single_data_ if d.fp_450_soplex is not None]
            peak_single_fp_453_povray_list = [d.fp_453_povray for d in peak_single_data_ if d.fp_453_povray is not None]
            peak_single_fp_454_calculix_list = [d.fp_454_calculix for d in peak_single_data_ if d.fp_454_calculix is not None]
            peak_single_fp_459_GemsFDTD_list = [d.fp_459_GemsFDTD for d in peak_single_data_ if d.fp_459_GemsFDTD is not None]
            peak_single_fp_465_tonto_list = [d.fp_465_tonto for d in peak_single_data_ if d.fp_465_tonto is not None]
            peak_single_fp_470_lbm_list = [d.fp_470_lbm for d in peak_single_data_ if d.fp_470_lbm is not None]
            peak_single_fp_481_wrf_list = [d.fp_481_wrf for d in peak_single_data_ if d.fp_481_wrf is not None]
            peak_single_fp_482_sphinx3_list = [d.fp_482_sphinx3 for d in peak_single_data_ if d.fp_482_sphinx3 is not None]
            peak_single_fp_SPECfp_2006_list = [d.fp_SPECfp_2006 for d in peak_single_data_ if d.fp_SPECfp_2006 is not None]
            peak_multi_int_400_perlbench_list = [d.int_400_perlbench for d in peak_multi_data_ if d.int_400_perlbench is not None]
            peak_multi_int_401_bzip2_list = [d.int_401_bzip2 for d in peak_multi_data_ if d.int_401_bzip2 is not None]
            peak_multi_int_403_gcc_list = [d.int_403_gcc for d in peak_multi_data_ if d.int_403_gcc is not None]
            peak_multi_int_429_mcf_list = [d.int_429_mcf for d in peak_multi_data_ if d.int_429_mcf is not None]
            peak_multi_int_445_gobmk_list = [d.int_445_gobmk for d in peak_multi_data_ if d.int_445_gobmk is not None]
            peak_multi_int_456_hmmer_list = [d.int_456_hmmer for d in peak_multi_data_ if d.int_456_hmmer is not None]
            peak_multi_int_458_sjeng_list = [d.int_458_sjeng for d in peak_multi_data_ if d.int_458_sjeng is not None]
            peak_multi_int_462_libquantum_list = [d.int_462_libquantum for d in peak_multi_data_ if d.int_462_libquantum is not None]
            peak_multi_int_464_h264ref_list = [d.int_464_h264ref for d in peak_multi_data_ if d.int_464_h264ref is not None]
            peak_multi_int_471_omnetpp_list = [d.int_471_omnetpp for d in peak_multi_data_ if d.int_471_omnetpp is not None]
            peak_multi_int_473_astar_list = [d.int_473_astar for d in peak_multi_data_ if d.int_473_astar is not None]
            peak_multi_int_483_xalancbmk_list = [d.int_483_xalancbmk for d in peak_multi_data_ if d.int_483_xalancbmk is not None]
            peak_multi_int_SPECint_2006_list = [d.int_SPECint_2006 for d in peak_multi_data_ if d.int_SPECint_2006 is not None]
            peak_multi_fp_410_bwaves_list = [d.fp_410_bwaves for d in peak_multi_data_ if d.fp_410_bwaves is not None]
            peak_multi_fp_416_gamess_list = [d.fp_416_gamess for d in peak_multi_data_ if d.fp_416_gamess is not None]
            peak_multi_fp_433_milc_list = [d.fp_433_milc for d in peak_multi_data_ if d.fp_433_milc is not None]
            peak_multi_fp_434_zeusmp_list = [d.fp_434_zeusmp for d in peak_multi_data_ if d.fp_434_zeusmp is not None]
            peak_multi_fp_435_gromacs_list = [d.fp_435_gromacs for d in peak_multi_data_ if d.fp_435_gromacs is not None]
            peak_multi_fp_436_cactusADM_list = [d.fp_436_cactusADM for d in peak_multi_data_ if d.fp_436_cactusADM is not None]
            peak_multi_fp_437_leslie3d_list = [d.fp_437_leslie3d for d in peak_multi_data_ if d.fp_437_leslie3d is not None]
            peak_multi_fp_444_namd_list = [d.fp_444_namd for d in peak_multi_data_ if d.fp_444_namd is not None]
            peak_multi_fp_447_dealII_list = [d.fp_447_dealII for d in peak_multi_data_ if d.fp_447_dealII is not None]
            peak_multi_fp_450_soplex_list = [d.fp_450_soplex for d in peak_multi_data_ if d.fp_450_soplex is not None]
            peak_multi_fp_453_povray_list = [d.fp_453_povray for d in peak_multi_data_ if d.fp_453_povray is not None]
            peak_multi_fp_454_calculix_list = [d.fp_454_calculix for d in peak_multi_data_ if d.fp_454_calculix is not None]
            peak_multi_fp_459_GemsFDTD_list = [d.fp_459_GemsFDTD for d in peak_multi_data_ if d.fp_459_GemsFDTD is not None]
            peak_multi_fp_465_tonto_list = [d.fp_465_tonto for d in peak_multi_data_ if d.fp_465_tonto is not None]
            peak_multi_fp_470_lbm_list = [d.fp_470_lbm for d in peak_multi_data_ if d.fp_470_lbm is not None]
            peak_multi_fp_481_wrf_list = [d.fp_481_wrf for d in peak_multi_data_ if d.fp_481_wrf is not None]
            peak_multi_fp_482_sphinx3_list = [d.fp_482_sphinx3 for d in peak_multi_data_ if d.fp_482_sphinx3 is not None]
            peak_multi_fp_SPECfp_2006_list = [d.fp_SPECfp_2006 for d in peak_multi_data_ if d.fp_SPECfp_2006 is not None]

            # 计算每个数组的平均值
            base_single_int_400_perlbench = np.mean(base_single_int_400_perlbench_list).round(2)
            base_single_int_401_bzip2 = np.mean(base_single_int_401_bzip2_list).round(2)
            base_single_int_403_gcc = np.mean(base_single_int_403_gcc_list).round(2)
            base_single_int_429_mcf = np.mean(base_single_int_429_mcf_list).round(2)
            base_single_int_445_gobmk = np.mean(base_single_int_445_gobmk_list).round(2)
            base_single_int_456_hmmer = np.mean(base_single_int_456_hmmer_list).round(2)
            base_single_int_458_sjeng = np.mean(base_single_int_458_sjeng_list).round(2)
            base_single_int_462_libquantum = np.mean(base_single_int_462_libquantum_list).round(2)
            base_single_int_464_h264ref = np.mean(base_single_int_464_h264ref_list).round(2)
            base_single_int_471_omnetpp = np.mean(base_single_int_471_omnetpp_list).round(2)
            base_single_int_473_astar = np.mean(base_single_int_473_astar_list).round(2)
            base_single_int_483_xalancbmk = np.mean(base_single_int_483_xalancbmk_list).round(2)
            base_single_int_SPECint_2006 = np.mean(base_single_int_SPECint_2006_list).round(2)
            base_single_fp_410_bwaves = np.mean(base_single_fp_410_bwaves_list).round(2)
            base_single_fp_416_gamess = np.mean(base_single_fp_416_gamess_list).round(2)
            base_single_fp_433_milc = np.mean(base_single_fp_433_milc_list).round(2)
            base_single_fp_434_zeusmp = np.mean(base_single_fp_434_zeusmp_list).round(2)
            base_single_fp_435_gromacs = np.mean(base_single_fp_435_gromacs_list).round(2)
            base_single_fp_436_cactusADM = np.mean(base_single_fp_436_cactusADM_list).round(2)
            base_single_fp_437_leslie3d = np.mean(base_single_fp_437_leslie3d_list).round(2)
            base_single_fp_444_namd = np.mean(base_single_fp_444_namd_list).round(2)
            base_single_fp_447_dealII = np.mean(base_single_fp_447_dealII_list).round(2)
            base_single_fp_450_soplex = np.mean(base_single_fp_450_soplex_list).round(2)
            base_single_fp_453_povray = np.mean(base_single_fp_453_povray_list).round(2)
            base_single_fp_454_calculix = np.mean(base_single_fp_454_calculix_list).round(2)
            base_single_fp_459_GemsFDTD = np.mean(base_single_fp_459_GemsFDTD_list).round(2)
            base_single_fp_465_tonto = np.mean(base_single_fp_465_tonto_list).round(2)
            base_single_fp_470_lbm = np.mean(base_single_fp_470_lbm_list).round(2)
            base_single_fp_481_wrf = np.mean(base_single_fp_481_wrf_list).round(2)
            base_single_fp_482_sphinx3 = np.mean(base_single_fp_482_sphinx3_list).round(2)
            base_single_fp_SPECfp_2006 = np.mean(base_single_fp_SPECfp_2006_list).round(2)
            base_multi_int_400_perlbench = np.mean(base_multi_int_400_perlbench_list).round(2)
            base_multi_int_401_bzip2 = np.mean(base_multi_int_401_bzip2_list).round(2)
            base_multi_int_403_gcc = np.mean(base_multi_int_403_gcc_list).round(2)
            base_multi_int_429_mcf = np.mean(base_multi_int_429_mcf_list).round(2)
            base_multi_int_445_gobmk = np.mean(base_multi_int_445_gobmk_list).round(2)
            base_multi_int_456_hmmer = np.mean(base_multi_int_456_hmmer_list).round(2)
            base_multi_int_458_sjeng = np.mean(base_multi_int_458_sjeng_list).round(2)
            base_multi_int_462_libquantum = np.mean(base_multi_int_462_libquantum_list).round(2)
            base_multi_int_464_h264ref = np.mean(base_multi_int_464_h264ref_list).round(2)
            base_multi_int_471_omnetpp = np.mean(base_multi_int_471_omnetpp_list).round(2)
            base_multi_int_473_astar = np.mean(base_multi_int_473_astar_list).round(2)
            base_multi_int_483_xalancbmk = np.mean(base_multi_int_483_xalancbmk_list).round(2)
            base_multi_int_SPECint_2006 = np.mean(base_multi_int_SPECint_2006_list).round(2)
            base_multi_fp_410_bwaves = np.mean(base_multi_fp_410_bwaves_list).round(2)
            base_multi_fp_416_gamess = np.mean(base_multi_fp_416_gamess_list).round(2)
            base_multi_fp_433_milc = np.mean(base_multi_fp_433_milc_list).round(2)
            base_multi_fp_434_zeusmp = np.mean(base_multi_fp_434_zeusmp_list).round(2)
            base_multi_fp_435_gromacs = np.mean(base_multi_fp_435_gromacs_list).round(2)
            base_multi_fp_436_cactusADM = np.mean(base_multi_fp_436_cactusADM_list).round(2)
            base_multi_fp_437_leslie3d = np.mean(base_multi_fp_437_leslie3d_list).round(2)
            base_multi_fp_444_namd = np.mean(base_multi_fp_444_namd_list).round(2)
            base_multi_fp_447_dealII = np.mean(base_multi_fp_447_dealII_list).round(2)
            base_multi_fp_450_soplex = np.mean(base_multi_fp_450_soplex_list).round(2)
            base_multi_fp_453_povray = np.mean(base_multi_fp_453_povray_list).round(2)
            base_multi_fp_454_calculix = np.mean(base_multi_fp_454_calculix_list).round(2)
            base_multi_fp_459_GemsFDTD = np.mean(base_multi_fp_459_GemsFDTD_list).round(2)
            base_multi_fp_465_tonto = np.mean(base_multi_fp_465_tonto_list).round(2)
            base_multi_fp_470_lbm = np.mean(base_multi_fp_470_lbm_list).round(2)
            base_multi_fp_481_wrf = np.mean(base_multi_fp_481_wrf_list).round(2)
            base_multi_fp_482_sphinx3 = np.mean(base_multi_fp_482_sphinx3_list).round(2)
            base_multi_fp_SPECfp_2006 = np.mean(base_multi_fp_SPECfp_2006_list).round(2)
            peak_single_int_400_perlbench = np.mean(peak_single_int_400_perlbench_list).round(2)
            peak_single_int_401_bzip2 = np.mean(peak_single_int_401_bzip2_list).round(2)
            peak_single_int_403_gcc = np.mean(peak_single_int_403_gcc_list).round(2)
            peak_single_int_429_mcf = np.mean(peak_single_int_429_mcf_list).round(2)
            peak_single_int_445_gobmk = np.mean(peak_single_int_445_gobmk_list).round(2)
            peak_single_int_456_hmmer = np.mean(peak_single_int_456_hmmer_list).round(2)
            peak_single_int_458_sjeng = np.mean(peak_single_int_458_sjeng_list).round(2)
            peak_single_int_462_libquantum = np.mean(peak_single_int_462_libquantum_list).round(2)
            peak_single_int_464_h264ref = np.mean(peak_single_int_464_h264ref_list).round(2)
            peak_single_int_471_omnetpp = np.mean(peak_single_int_471_omnetpp_list).round(2)
            peak_single_int_473_astar = np.mean(peak_single_int_473_astar_list).round(2)
            peak_single_int_483_xalancbmk = np.mean(peak_single_int_483_xalancbmk_list).round(2)
            peak_single_int_SPECint_2006 = np.mean(peak_single_int_SPECint_2006_list).round(2)
            peak_single_fp_410_bwaves = np.mean(peak_single_fp_410_bwaves_list).round(2)
            peak_single_fp_416_gamess = np.mean(peak_single_fp_416_gamess_list).round(2)
            peak_single_fp_433_milc = np.mean(peak_single_fp_433_milc_list).round(2)
            peak_single_fp_434_zeusmp = np.mean(peak_single_fp_434_zeusmp_list).round(2)
            peak_single_fp_435_gromacs = np.mean(peak_single_fp_435_gromacs_list).round(2)
            peak_single_fp_436_cactusADM = np.mean(peak_single_fp_436_cactusADM_list).round(2)
            peak_single_fp_437_leslie3d = np.mean(peak_single_fp_437_leslie3d_list).round(2)
            peak_single_fp_444_namd = np.mean(peak_single_fp_444_namd_list).round(2)
            peak_single_fp_447_dealII = np.mean(peak_single_fp_447_dealII_list).round(2)
            peak_single_fp_450_soplex = np.mean(peak_single_fp_450_soplex_list).round(2)
            peak_single_fp_453_povray = np.mean(peak_single_fp_453_povray_list).round(2)
            peak_single_fp_454_calculix = np.mean(peak_single_fp_454_calculix_list).round(2)
            peak_single_fp_459_GemsFDTD = np.mean(peak_single_fp_459_GemsFDTD_list).round(2)
            peak_single_fp_465_tonto = np.mean(peak_single_fp_465_tonto_list).round(2)
            peak_single_fp_470_lbm = np.mean(peak_single_fp_470_lbm_list).round(2)
            peak_single_fp_481_wrf = np.mean(peak_single_fp_481_wrf_list).round(2)
            peak_single_fp_482_sphinx3 = np.mean(peak_single_fp_482_sphinx3_list).round(2)
            peak_single_fp_SPECfp_2006 = np.mean(peak_single_fp_SPECfp_2006_list).round(2)
            peak_multi_int_400_perlbench = np.mean(peak_multi_int_400_perlbench_list).round(2)
            peak_multi_int_401_bzip2 = np.mean(peak_multi_int_401_bzip2_list).round(2)
            peak_multi_int_403_gcc = np.mean(peak_multi_int_403_gcc_list).round(2)
            peak_multi_int_429_mcf = np.mean(peak_multi_int_429_mcf_list).round(2)
            peak_multi_int_445_gobmk = np.mean(peak_multi_int_445_gobmk_list).round(2)
            peak_multi_int_456_hmmer = np.mean(peak_multi_int_456_hmmer_list).round(2)
            peak_multi_int_458_sjeng = np.mean(peak_multi_int_458_sjeng_list).round(2)
            peak_multi_int_462_libquantum = np.mean(peak_multi_int_462_libquantum_list).round(2)
            peak_multi_int_464_h264ref = np.mean(peak_multi_int_464_h264ref_list).round(2)
            peak_multi_int_471_omnetpp = np.mean(peak_multi_int_471_omnetpp_list).round(2)
            peak_multi_int_473_astar = np.mean(peak_multi_int_473_astar_list).round(2)
            peak_multi_int_483_xalancbmk = np.mean(peak_multi_int_483_xalancbmk_list).round(2)
            peak_multi_int_SPECint_2006 = np.mean(peak_multi_int_SPECint_2006_list).round(2)
            peak_multi_fp_410_bwaves = np.mean(peak_multi_fp_410_bwaves_list).round(2)
            peak_multi_fp_416_gamess = np.mean(peak_multi_fp_416_gamess_list).round(2)
            peak_multi_fp_433_milc = np.mean(peak_multi_fp_433_milc_list).round(2)
            peak_multi_fp_434_zeusmp = np.mean(peak_multi_fp_434_zeusmp_list).round(2)
            peak_multi_fp_435_gromacs = np.mean(peak_multi_fp_435_gromacs_list).round(2)
            peak_multi_fp_436_cactusADM = np.mean(peak_multi_fp_436_cactusADM_list).round(2)
            peak_multi_fp_437_leslie3d = np.mean(peak_multi_fp_437_leslie3d_list).round(2)
            peak_multi_fp_444_namd = np.mean(peak_multi_fp_444_namd_list).round(2)
            peak_multi_fp_447_dealII = np.mean(peak_multi_fp_447_dealII_list).round(2)
            peak_multi_fp_450_soplex = np.mean(peak_multi_fp_450_soplex_list).round(2)
            peak_multi_fp_453_povray = np.mean(peak_multi_fp_453_povray_list).round(2)
            peak_multi_fp_454_calculix = np.mean(peak_multi_fp_454_calculix_list).round(2)
            peak_multi_fp_459_GemsFDTD = np.mean(peak_multi_fp_459_GemsFDTD_list).round(2)
            peak_multi_fp_465_tonto = np.mean(peak_multi_fp_465_tonto_list).round(2)
            peak_multi_fp_470_lbm = np.mean(peak_multi_fp_470_lbm_list).round(2)
            peak_multi_fp_481_wrf = np.mean(peak_multi_fp_481_wrf_list).round(2)
            peak_multi_fp_482_sphinx3 = np.mean(peak_multi_fp_482_sphinx3_list).round(2)
            peak_multi_fp_SPECfp_2006 = np.mean(peak_multi_fp_SPECfp_2006_list).round(2)

        new_data = {'execute_cmd': execute_cmd,
                    'modify_parameters': modify_parameters,

                    'base_single_int_400_perlbench': base_single_int_400_perlbench,
                    'base_single_int_401_bzip2': base_single_int_401_bzip2,
                    'base_single_int_403_gcc': base_single_int_403_gcc,
                    'base_single_int_429_mcf': base_single_int_429_mcf,
                    'base_single_int_445_gobmk': base_single_int_445_gobmk,
                    'base_single_int_456_hmmer': base_single_int_456_hmmer,
                    'base_single_int_458_sjeng': base_single_int_458_sjeng,
                    'base_single_int_462_libquantum': base_single_int_462_libquantum,
                    'base_single_int_464_h264ref': base_single_int_464_h264ref,
                    'base_single_int_471_omnetpp': base_single_int_471_omnetpp,
                    'base_single_int_473_astar': base_single_int_473_astar,
                    'base_single_int_483_xalancbmk': base_single_int_483_xalancbmk,
                    'base_single_int_SPECint_2006': base_single_int_SPECint_2006,
                    'base_single_fp_410_bwaves': base_single_fp_410_bwaves,
                    'base_single_fp_416_gamess': base_single_fp_416_gamess,
                    'base_single_fp_433_milc': base_single_fp_433_milc,
                    'base_single_fp_434_zeusmp': base_single_fp_434_zeusmp,
                    'base_single_fp_435_gromacs': base_single_fp_435_gromacs,
                    'base_single_fp_436_cactusADM': base_single_fp_436_cactusADM,
                    'base_single_fp_437_leslie3d': base_single_fp_437_leslie3d,
                    'base_single_fp_444_namd': base_single_fp_444_namd,
                    'base_single_fp_447_dealII': base_single_fp_447_dealII,
                    'base_single_fp_450_soplex': base_single_fp_450_soplex,
                    'base_single_fp_453_povray': base_single_fp_453_povray,
                    'base_single_fp_454_calculix': base_single_fp_454_calculix,
                    'base_single_fp_459_GemsFDTD': base_single_fp_459_GemsFDTD,
                    'base_single_fp_465_tonto': base_single_fp_465_tonto,
                    'base_single_fp_470_lbm': base_single_fp_470_lbm,
                    'base_single_fp_481_wrf': base_single_fp_481_wrf,
                    'base_single_fp_482_sphinx3': base_single_fp_482_sphinx3,
                    'base_single_fp_SPECfp_2006': base_single_fp_SPECfp_2006,
                    'base_multi_int_400_perlbench': base_multi_int_400_perlbench,
                    'base_multi_int_401_bzip2': base_multi_int_401_bzip2,
                    'base_multi_int_403_gcc': base_multi_int_403_gcc,
                    'base_multi_int_429_mcf': base_multi_int_429_mcf,
                    'base_multi_int_445_gobmk': base_multi_int_445_gobmk,
                    'base_multi_int_456_hmmer': base_multi_int_456_hmmer,
                    'base_multi_int_458_sjeng': base_multi_int_458_sjeng,
                    'base_multi_int_462_libquantum': base_multi_int_462_libquantum,
                    'base_multi_int_464_h264ref': base_multi_int_464_h264ref,
                    'base_multi_int_471_omnetpp': base_multi_int_471_omnetpp,
                    'base_multi_int_473_astar': base_multi_int_473_astar,
                    'base_multi_int_483_xalancbmk': base_multi_int_483_xalancbmk,
                    'base_multi_int_SPECint_2006': base_multi_int_SPECint_2006,
                    'base_multi_fp_410_bwaves': base_multi_fp_410_bwaves,
                    'base_multi_fp_416_gamess': base_multi_fp_416_gamess,
                    'base_multi_fp_433_milc': base_multi_fp_433_milc,
                    'base_multi_fp_434_zeusmp': base_multi_fp_434_zeusmp,
                    'base_multi_fp_435_gromacs': base_multi_fp_435_gromacs,
                    'base_multi_fp_436_cactusADM': base_multi_fp_436_cactusADM,
                    'base_multi_fp_437_leslie3d': base_multi_fp_437_leslie3d,
                    'base_multi_fp_444_namd': base_multi_fp_444_namd,
                    'base_multi_fp_447_dealII': base_multi_fp_447_dealII,
                    'base_multi_fp_450_soplex': base_multi_fp_450_soplex,
                    'base_multi_fp_453_povray': base_multi_fp_453_povray,
                    'base_multi_fp_454_calculix': base_multi_fp_454_calculix,
                    'base_multi_fp_459_GemsFDTD': base_multi_fp_459_GemsFDTD,
                    'base_multi_fp_465_tonto': base_multi_fp_465_tonto,
                    'base_multi_fp_470_lbm': base_multi_fp_470_lbm,
                    'base_multi_fp_481_wrf': base_multi_fp_481_wrf,
                    'base_multi_fp_482_sphinx3': base_multi_fp_482_sphinx3,
                    'base_multi_fp_SPECfp_2006': base_multi_fp_SPECfp_2006,
                    'peak_single_int_400_perlbench': peak_single_int_400_perlbench,
                    'peak_single_int_401_bzip2': peak_single_int_401_bzip2,
                    'peak_single_int_403_gcc': peak_single_int_403_gcc,
                    'peak_single_int_429_mcf': peak_single_int_429_mcf,
                    'peak_single_int_445_gobmk': peak_single_int_445_gobmk,
                    'peak_single_int_456_hmmer': peak_single_int_456_hmmer,
                    'peak_single_int_458_sjeng': peak_single_int_458_sjeng,
                    'peak_single_int_462_libquantum': peak_single_int_462_libquantum,
                    'peak_single_int_464_h264ref': peak_single_int_464_h264ref,
                    'peak_single_int_471_omnetpp': peak_single_int_471_omnetpp,
                    'peak_single_int_473_astar': peak_single_int_473_astar,
                    'peak_single_int_483_xalancbmk': peak_single_int_483_xalancbmk,
                    'peak_single_int_SPECint_2006': peak_single_int_SPECint_2006,
                    'peak_single_fp_410_bwaves': peak_single_fp_410_bwaves,
                    'peak_single_fp_416_gamess': peak_single_fp_416_gamess,
                    'peak_single_fp_433_milc': peak_single_fp_433_milc,
                    'peak_single_fp_434_zeusmp': peak_single_fp_434_zeusmp,
                    'peak_single_fp_435_gromacs': peak_single_fp_435_gromacs,
                    'peak_single_fp_436_cactusADM': peak_single_fp_436_cactusADM,
                    'peak_single_fp_437_leslie3d': peak_single_fp_437_leslie3d,
                    'peak_single_fp_444_namd': peak_single_fp_444_namd,
                    'peak_single_fp_447_dealII': peak_single_fp_447_dealII,
                    'peak_single_fp_450_soplex': peak_single_fp_450_soplex,
                    'peak_single_fp_453_povray': peak_single_fp_453_povray,
                    'peak_single_fp_454_calculix': peak_single_fp_454_calculix,
                    'peak_single_fp_459_GemsFDTD': peak_single_fp_459_GemsFDTD,
                    'peak_single_fp_465_tonto': peak_single_fp_465_tonto,
                    'peak_single_fp_470_lbm': peak_single_fp_470_lbm,
                    'peak_single_fp_481_wrf': peak_single_fp_481_wrf,
                    'peak_single_fp_482_sphinx3': peak_single_fp_482_sphinx3,
                    'peak_single_fp_SPECfp_2006': peak_single_fp_SPECfp_2006,
                    'peak_multi_int_400_perlbench': peak_multi_int_400_perlbench,
                    'peak_multi_int_401_bzip2': peak_multi_int_401_bzip2,
                    'peak_multi_int_403_gcc': peak_multi_int_403_gcc,
                    'peak_multi_int_429_mcf': peak_multi_int_429_mcf,
                    'peak_multi_int_445_gobmk': peak_multi_int_445_gobmk,
                    'peak_multi_int_456_hmmer': peak_multi_int_456_hmmer,
                    'peak_multi_int_458_sjeng': peak_multi_int_458_sjeng,
                    'peak_multi_int_462_libquantum': peak_multi_int_462_libquantum,
                    'peak_multi_int_464_h264ref': peak_multi_int_464_h264ref,
                    'peak_multi_int_471_omnetpp': peak_multi_int_471_omnetpp,
                    'peak_multi_int_473_astar': peak_multi_int_473_astar,
                    'peak_multi_int_483_xalancbmk': peak_multi_int_483_xalancbmk,
                    'peak_multi_int_SPECint_2006': peak_multi_int_SPECint_2006,
                    'peak_multi_fp_410_bwaves': peak_multi_fp_410_bwaves,
                    'peak_multi_fp_416_gamess': peak_multi_fp_416_gamess,
                    'peak_multi_fp_433_milc': peak_multi_fp_433_milc,
                    'peak_multi_fp_434_zeusmp': peak_multi_fp_434_zeusmp,
                    'peak_multi_fp_435_gromacs': peak_multi_fp_435_gromacs,
                    'peak_multi_fp_436_cactusADM': peak_multi_fp_436_cactusADM,
                    'peak_multi_fp_437_leslie3d': peak_multi_fp_437_leslie3d,
                    'peak_multi_fp_444_namd': peak_multi_fp_444_namd,
                    'peak_multi_fp_447_dealII': peak_multi_fp_447_dealII,
                    'peak_multi_fp_450_soplex': peak_multi_fp_450_soplex,
                    'peak_multi_fp_453_povray': peak_multi_fp_453_povray,
                    'peak_multi_fp_454_calculix': peak_multi_fp_454_calculix,
                    'peak_multi_fp_459_GemsFDTD': peak_multi_fp_459_GemsFDTD,
                    'peak_multi_fp_465_tonto': peak_multi_fp_465_tonto,
                    'peak_multi_fp_470_lbm': peak_multi_fp_470_lbm,
                    'peak_multi_fp_481_wrf': peak_multi_fp_481_wrf,
                    'peak_multi_fp_482_sphinx3': peak_multi_fp_482_sphinx3,
                    'peak_multi_fp_SPECfp_2006': peak_multi_fp_SPECfp_2006,
                    }
        return new_data

    def do_base_data(self,data):
        datas = [
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '400.perlbench', 'column5': data['base_single_int_400_perlbench']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '401.bzip2', 'column5': data['base_single_int_401_bzip2']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '403.gcc', 'column5': data['base_single_int_403_gcc']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '429.mcf', 'column5': data['base_single_int_429_mcf']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '445.gobmk', 'column5': data['base_single_int_445_gobmk']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '456.hmmer', 'column5': data['base_single_int_456_hmmer']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '458.sjeng', 'column5': data['base_single_int_458_sjeng']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '462.libquantum', 'column5': data['base_single_int_462_libquantum']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '464.h264ref', 'column5': data['base_single_int_464_h264ref']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '471.omnetpp', 'column5': data['base_single_int_471_omnetpp']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '473.astar', 'column5': data['base_single_int_473_astar']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '483.xalancbmk', 'column5': data['base_single_int_483_xalancbmk']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'SPECint_2006', 'column5': data['base_single_int_SPECint_2006']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '410.bwaves', 'column5': data['base_single_fp_410_bwaves']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '416.gamess', 'column5': data['base_single_fp_416_gamess']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '433.milc', 'column5': data['base_single_fp_433_milc']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '434.zeusmp', 'column5': data['base_single_fp_434_zeusmp']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '435.gromacs', 'column5': data['base_single_fp_435_gromacs']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '436.cactusADM', 'column5': data['base_single_fp_436_cactusADM']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '437.leslie3d', 'column5': data['base_single_fp_437_leslie3d']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '444.namd', 'column5': data['base_single_fp_444_namd']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '447.dealII', 'column5': data['base_single_fp_447_dealII']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '450.soplex', 'column5': data['base_single_fp_450_soplex']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '453.povray', 'column5': data['base_single_fp_453_povray']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '454.calculix', 'column5': data['base_single_fp_454_calculix']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '459.GemsFDTD', 'column5': data['base_single_fp_459_GemsFDTD']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '465.tonto', 'column5': data['base_single_fp_465_tonto']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '470.lbm', 'column5': data['base_single_fp_470_lbm']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '481.wrf', 'column5': data['base_single_fp_481_wrf']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '482.sphinx3', 'column5': data['base_single_fp_482_sphinx3']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'SPECfp_2006', 'column5': data['base_single_fp_SPECfp_2006']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '400.perlbench', 'column5': data['base_multi_int_400_perlbench']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '401.bzip2', 'column5': data['base_multi_int_401_bzip2']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '403.gcc', 'column5': data['base_multi_int_403_gcc']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '429.mcf', 'column5': data['base_multi_int_429_mcf']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '445.gobmk', 'column5': data['base_multi_int_445_gobmk']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '456.hmmer', 'column5': data['base_multi_int_456_hmmer']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '458.sjeng', 'column5': data['base_multi_int_458_sjeng']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '462.libquantum', 'column5': data['base_multi_int_462_libquantum']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '464.h264ref', 'column5': data['base_multi_int_464_h264ref']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '471.omnetpp', 'column5': data['base_multi_int_471_omnetpp']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '473.astar', 'column5': data['base_multi_int_473_astar']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '483.xalancbmk', 'column5': data['base_multi_int_483_xalancbmk']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'SPECint_2006', 'column5': data['base_multi_int_SPECint_2006']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '410.bwaves', 'column5': data['base_multi_fp_410_bwaves']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '416.gamess', 'column5': data['base_multi_fp_416_gamess']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '433.milc', 'column5': data['base_multi_fp_433_milc']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '434.zeusmp', 'column5': data['base_multi_fp_434_zeusmp']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '435.gromacs', 'column5': data['base_multi_fp_435_gromacs']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '436.cactusADM', 'column5': data['base_multi_fp_436_cactusADM']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '437.leslie3d', 'column5': data['base_multi_fp_437_leslie3d']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '444.namd', 'column5': data['base_multi_fp_444_namd']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '447.dealII', 'column5': data['base_multi_fp_447_dealII']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '450.soplex', 'column5': data['base_multi_fp_450_soplex']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '453.povray', 'column5': data['base_multi_fp_453_povray']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '454.calculix', 'column5': data['base_multi_fp_454_calculix']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '459.GemsFDTD', 'column5': data['base_multi_fp_459_GemsFDTD']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '465.tonto', 'column5': data['base_multi_fp_465_tonto']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '470.lbm', 'column5': data['base_multi_fp_470_lbm']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '481.wrf', 'column5': data['base_multi_fp_481_wrf']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '482.sphinx3', 'column5': data['base_multi_fp_482_sphinx3']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'SPECfp_2006', 'column5': data['base_multi_fp_SPECfp_2006']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '400.perlbench', 'column5': data['peak_single_int_400_perlbench']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '401.bzip2', 'column5': data['peak_single_int_401_bzip2']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '403.gcc', 'column5': data['peak_single_int_403_gcc']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '429.mcf', 'column5': data['peak_single_int_429_mcf']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '445.gobmk', 'column5': data['peak_single_int_445_gobmk']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '456.hmmer', 'column5': data['peak_single_int_456_hmmer']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '458.sjeng', 'column5': data['peak_single_int_458_sjeng']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '462.libquantum', 'column5': data['peak_single_int_462_libquantum']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '464.h264ref', 'column5': data['peak_single_int_464_h264ref']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '471.omnetpp', 'column5': data['peak_single_int_471_omnetpp']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '473.astar', 'column5': data['peak_single_int_473_astar']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '483.xalancbmk', 'column5': data['peak_single_int_483_xalancbmk']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'SPECint_2006', 'column5': data['peak_single_int_SPECint_2006']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '410.bwaves', 'column5': data['peak_single_fp_410_bwaves']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '416.gamess', 'column5': data['peak_single_fp_416_gamess']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '433.milc', 'column5': data['peak_single_fp_433_milc']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '434.zeusmp', 'column5': data['peak_single_fp_434_zeusmp']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '435.gromacs', 'column5': data['peak_single_fp_435_gromacs']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '436.cactusADM', 'column5': data['peak_single_fp_436_cactusADM']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '437.leslie3d', 'column5': data['peak_single_fp_437_leslie3d']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '444.namd', 'column5': data['peak_single_fp_444_namd']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '447.dealII', 'column5': data['peak_single_fp_447_dealII']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '450.soplex', 'column5': data['peak_single_fp_450_soplex']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '453.povray', 'column5': data['peak_single_fp_453_povray']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '454.calculix', 'column5': data['peak_single_fp_454_calculix']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '459.GemsFDTD', 'column5': data['peak_single_fp_459_GemsFDTD']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '465.tonto', 'column5': data['peak_single_fp_465_tonto']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '470.lbm', 'column5': data['peak_single_fp_470_lbm']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '481.wrf', 'column5': data['peak_single_fp_481_wrf']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '482.sphinx3', 'column5': data['peak_single_fp_482_sphinx3']},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'SPECfp_2006', 'column5': data['peak_single_fp_SPECfp_2006']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '400.perlbench', 'column5': data['peak_multi_int_400_perlbench']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '401.bzip2', 'column5': data['peak_multi_int_401_bzip2']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '403.gcc', 'column5': data['peak_multi_int_403_gcc']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '429.mcf', 'column5': data['peak_multi_int_429_mcf']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '445.gobmk', 'column5': data['peak_multi_int_445_gobmk']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '456.hmmer', 'column5': data['peak_multi_int_456_hmmer']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '458.sjeng', 'column5': data['peak_multi_int_458_sjeng']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '462.libquantum', 'column5': data['peak_multi_int_462_libquantum']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '464.h264ref', 'column5': data['peak_multi_int_464_h264ref']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '471.omnetpp', 'column5': data['peak_multi_int_471_omnetpp']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '473.astar', 'column5': data['peak_multi_int_473_astar']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '483.xalancbmk', 'column5': data['peak_multi_int_483_xalancbmk']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'SPECint_2006', 'column5': data['peak_multi_int_SPECint_2006']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '410.bwaves', 'column5': data['peak_multi_fp_410_bwaves']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '416.gamess', 'column5': data['peak_multi_fp_416_gamess']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '433.milc', 'column5': data['peak_multi_fp_433_milc']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '434.zeusmp', 'column5': data['peak_multi_fp_434_zeusmp']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '435.gromacs', 'column5': data['peak_multi_fp_435_gromacs']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '436.cactusADM', 'column5': data['peak_multi_fp_436_cactusADM']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '437.leslie3d', 'column5': data['peak_multi_fp_437_leslie3d']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '444.namd', 'column5': data['peak_multi_fp_444_namd']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '447.dealII', 'column5': data['peak_multi_fp_447_dealII']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '450.soplex', 'column5': data['peak_multi_fp_450_soplex']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '453.povray', 'column5': data['peak_multi_fp_453_povray']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '454.calculix', 'column5': data['peak_multi_fp_454_calculix']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '459.GemsFDTD', 'column5': data['peak_multi_fp_459_GemsFDTD']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '465.tonto', 'column5': data['peak_multi_fp_465_tonto']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '470.lbm', 'column5': data['peak_multi_fp_470_lbm']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '481.wrf', 'column5': data['peak_multi_fp_481_wrf']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '482.sphinx3', 'column5': data['peak_multi_fp_482_sphinx3']},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'SPECfp_2006', 'column5': data['peak_multi_fp_SPECfp_2006']},
        ]
        return datas

    def list(self, request, *args, **kwargs):
        """
        返回列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        env_id = request.GET.get('env_id')
        comparsionIds = request.GET.get('comparsionIds')
        comparsionIds = comparsionIds.split(',')
        base_queryset = Cpu2006.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        json_datas = self.get_data(base_serializer)
        base_datas = self.do_base_data(json_datas)
        others = [{'column1': 'Cpu2006', 'column2': '', 'column3': '','column4': '','column5': 'Cpu2006#1'},
                  {'column1': '执行命令', 'column2': '', 'column3': '','column4': '','column5': base_serializer.data[0]['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': '','column4': '','column5': base_serializer.data[0]['modify_parameters']}]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 6
                comparsion_queryset = Cpu2006.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_serializer)

                others[0]['column' + str(new_index)] = 'Cpu2006#' + str(index + 2)
                others[1]['column' + str(new_index)] = comparsion_serializer.data[0]['execute_cmd']
                others[2]['column' + str(new_index)] = comparsion_serializer.data[0]['modify_parameters']

                others[0]['column' + str(new_index + 1)] = ''
                others[1]['column' + str(new_index + 1)] = ''
                others[2]['column' + str(new_index + 1)] = ''

                base_datas[0]['column' + str(new_index)] = comparsion_datas['base_single_int_400_perlbench']
                base_datas[1]['column' + str(new_index)] = comparsion_datas['base_single_int_401_bzip2']
                base_datas[2]['column' + str(new_index)] = comparsion_datas['base_single_int_403_gcc']
                base_datas[3]['column' + str(new_index)] = comparsion_datas['base_single_int_429_mcf']
                base_datas[4]['column' + str(new_index)] = comparsion_datas['base_single_int_445_gobmk']
                base_datas[5]['column' + str(new_index)] = comparsion_datas['base_single_int_456_hmmer']
                base_datas[6]['column' + str(new_index)] = comparsion_datas['base_single_int_458_sjeng']
                base_datas[7]['column' + str(new_index)] = comparsion_datas['base_single_int_462_libquantum']
                base_datas[8]['column' + str(new_index)] = comparsion_datas['base_single_int_464_h264ref']
                base_datas[9]['column' + str(new_index)] = comparsion_datas['base_single_int_471_omnetpp']
                base_datas[10]['column' + str(new_index)] = comparsion_datas['base_single_int_473_astar']
                base_datas[11]['column' + str(new_index)] = comparsion_datas['base_single_int_483_xalancbmk']
                base_datas[12]['column' + str(new_index)] = comparsion_datas['base_single_int_SPECint_2006']
                base_datas[13]['column' + str(new_index)] = comparsion_datas['base_single_fp_410_bwaves']
                base_datas[14]['column' + str(new_index)] = comparsion_datas['base_single_fp_416_gamess']
                base_datas[15]['column' + str(new_index)] = comparsion_datas['base_single_fp_433_milc']
                base_datas[16]['column' + str(new_index)] = comparsion_datas['base_single_fp_434_zeusmp']
                base_datas[17]['column' + str(new_index)] = comparsion_datas['base_single_fp_435_gromacs']
                base_datas[18]['column' + str(new_index)] = comparsion_datas['base_single_fp_436_cactusADM']
                base_datas[19]['column' + str(new_index)] = comparsion_datas['base_single_fp_437_leslie3d']
                base_datas[20]['column' + str(new_index)] = comparsion_datas['base_single_fp_444_namd']
                base_datas[21]['column' + str(new_index)] = comparsion_datas['base_single_fp_447_dealII']
                base_datas[22]['column' + str(new_index)] = comparsion_datas['base_single_fp_450_soplex']
                base_datas[23]['column' + str(new_index)] = comparsion_datas['base_single_fp_453_povray']
                base_datas[24]['column' + str(new_index)] = comparsion_datas['base_single_fp_454_calculix']
                base_datas[25]['column' + str(new_index)] = comparsion_datas['base_single_fp_459_GemsFDTD']
                base_datas[26]['column' + str(new_index)] = comparsion_datas['base_single_fp_465_tonto']
                base_datas[27]['column' + str(new_index)] = comparsion_datas['base_single_fp_470_lbm']
                base_datas[28]['column' + str(new_index)] = comparsion_datas['base_single_fp_481_wrf']
                base_datas[29]['column' + str(new_index)] = comparsion_datas['base_single_fp_482_sphinx3']
                base_datas[30]['column' + str(new_index)] = comparsion_datas['base_single_fp_SPECfp_2006']
                base_datas[31]['column' + str(new_index)] = comparsion_datas['base_multi_int_400_perlbench']
                base_datas[32]['column' + str(new_index)] = comparsion_datas['base_multi_int_401_bzip2']
                base_datas[33]['column' + str(new_index)] = comparsion_datas['base_multi_int_403_gcc']
                base_datas[34]['column' + str(new_index)] = comparsion_datas['base_multi_int_429_mcf']
                base_datas[35]['column' + str(new_index)] = comparsion_datas['base_multi_int_445_gobmk']
                base_datas[36]['column' + str(new_index)] = comparsion_datas['base_multi_int_456_hmmer']
                base_datas[37]['column' + str(new_index)] = comparsion_datas['base_multi_int_458_sjeng']
                base_datas[38]['column' + str(new_index)] = comparsion_datas['base_multi_int_462_libquantum']
                base_datas[39]['column' + str(new_index)] = comparsion_datas['base_multi_int_464_h264ref']
                base_datas[40]['column' + str(new_index)] = comparsion_datas['base_multi_int_471_omnetpp']
                base_datas[41]['column' + str(new_index)] = comparsion_datas['base_multi_int_473_astar']
                base_datas[42]['column' + str(new_index)] = comparsion_datas['base_multi_int_483_xalancbmk']
                base_datas[43]['column' + str(new_index)] = comparsion_datas['base_multi_int_SPECint_2006']
                base_datas[44]['column' + str(new_index)] = comparsion_datas['base_multi_fp_410_bwaves']
                base_datas[45]['column' + str(new_index)] = comparsion_datas['base_multi_fp_416_gamess']
                base_datas[46]['column' + str(new_index)] = comparsion_datas['base_multi_fp_433_milc']
                base_datas[47]['column' + str(new_index)] = comparsion_datas['base_multi_fp_434_zeusmp']
                base_datas[48]['column' + str(new_index)] = comparsion_datas['base_multi_fp_435_gromacs']
                base_datas[49]['column' + str(new_index)] = comparsion_datas['base_multi_fp_436_cactusADM']
                base_datas[50]['column' + str(new_index)] = comparsion_datas['base_multi_fp_437_leslie3d']
                base_datas[51]['column' + str(new_index)] = comparsion_datas['base_multi_fp_444_namd']
                base_datas[52]['column' + str(new_index)] = comparsion_datas['base_multi_fp_447_dealII']
                base_datas[53]['column' + str(new_index)] = comparsion_datas['base_multi_fp_450_soplex']
                base_datas[54]['column' + str(new_index)] = comparsion_datas['base_multi_fp_453_povray']
                base_datas[55]['column' + str(new_index)] = comparsion_datas['base_multi_fp_454_calculix']
                base_datas[56]['column' + str(new_index)] = comparsion_datas['base_multi_fp_459_GemsFDTD']
                base_datas[57]['column' + str(new_index)] = comparsion_datas['base_multi_fp_465_tonto']
                base_datas[58]['column' + str(new_index)] = comparsion_datas['base_multi_fp_470_lbm']
                base_datas[59]['column' + str(new_index)] = comparsion_datas['base_multi_fp_481_wrf']
                base_datas[60]['column' + str(new_index)] = comparsion_datas['base_multi_fp_482_sphinx3']
                base_datas[61]['column' + str(new_index)] = comparsion_datas['base_multi_fp_SPECfp_2006']
                base_datas[62]['column' + str(new_index)] = comparsion_datas['peak_single_int_400_perlbench']
                base_datas[63]['column' + str(new_index)] = comparsion_datas['peak_single_int_401_bzip2']
                base_datas[64]['column' + str(new_index)] = comparsion_datas['peak_single_int_403_gcc']
                base_datas[65]['column' + str(new_index)] = comparsion_datas['peak_single_int_429_mcf']
                base_datas[66]['column' + str(new_index)] = comparsion_datas['peak_single_int_445_gobmk']
                base_datas[67]['column' + str(new_index)] = comparsion_datas['peak_single_int_456_hmmer']
                base_datas[68]['column' + str(new_index)] = comparsion_datas['peak_single_int_458_sjeng']
                base_datas[69]['column' + str(new_index)] = comparsion_datas['peak_single_int_462_libquantum']
                base_datas[70]['column' + str(new_index)] = comparsion_datas['peak_single_int_464_h264ref']
                base_datas[71]['column' + str(new_index)] = comparsion_datas['peak_single_int_471_omnetpp']
                base_datas[72]['column' + str(new_index)] = comparsion_datas['peak_single_int_473_astar']
                base_datas[73]['column' + str(new_index)] = comparsion_datas['peak_single_int_483_xalancbmk']
                base_datas[74]['column' + str(new_index)] = comparsion_datas['peak_single_int_SPECint_2006']
                base_datas[75]['column' + str(new_index)] = comparsion_datas['peak_single_fp_410_bwaves']
                base_datas[76]['column' + str(new_index)] = comparsion_datas['peak_single_fp_416_gamess']
                base_datas[77]['column' + str(new_index)] = comparsion_datas['peak_single_fp_433_milc']
                base_datas[78]['column' + str(new_index)] = comparsion_datas['peak_single_fp_434_zeusmp']
                base_datas[79]['column' + str(new_index)] = comparsion_datas['peak_single_fp_435_gromacs']
                base_datas[80]['column' + str(new_index)] = comparsion_datas['peak_single_fp_436_cactusADM']
                base_datas[81]['column' + str(new_index)] = comparsion_datas['peak_single_fp_437_leslie3d']
                base_datas[82]['column' + str(new_index)] = comparsion_datas['peak_single_fp_444_namd']
                base_datas[83]['column' + str(new_index)] = comparsion_datas['peak_single_fp_447_dealII']
                base_datas[84]['column' + str(new_index)] = comparsion_datas['peak_single_fp_450_soplex']
                base_datas[85]['column' + str(new_index)] = comparsion_datas['peak_single_fp_453_povray']
                base_datas[86]['column' + str(new_index)] = comparsion_datas['peak_single_fp_454_calculix']
                base_datas[87]['column' + str(new_index)] = comparsion_datas['peak_single_fp_459_GemsFDTD']
                base_datas[88]['column' + str(new_index)] = comparsion_datas['peak_single_fp_465_tonto']
                base_datas[89]['column' + str(new_index)] = comparsion_datas['peak_single_fp_470_lbm']
                base_datas[90]['column' + str(new_index)] = comparsion_datas['peak_single_fp_481_wrf']
                base_datas[91]['column' + str(new_index)] = comparsion_datas['peak_single_fp_482_sphinx3']
                base_datas[92]['column' + str(new_index)] = comparsion_datas['peak_single_fp_SPECfp_2006']
                base_datas[93]['column' + str(new_index)] = comparsion_datas['peak_multi_int_400_perlbench']
                base_datas[94]['column' + str(new_index)] = comparsion_datas['peak_multi_int_401_bzip2']
                base_datas[95]['column' + str(new_index)] = comparsion_datas['peak_multi_int_403_gcc']
                base_datas[96]['column' + str(new_index)] = comparsion_datas['peak_multi_int_429_mcf']
                base_datas[97]['column' + str(new_index)] = comparsion_datas['peak_multi_int_445_gobmk']
                base_datas[98]['column' + str(new_index)] = comparsion_datas['peak_multi_int_456_hmmer']
                base_datas[99]['column' + str(new_index)] = comparsion_datas['peak_multi_int_458_sjeng']
                base_datas[100]['column' + str(new_index)] = comparsion_datas['peak_multi_int_462_libquantum']
                base_datas[101]['column' + str(new_index)] = comparsion_datas['peak_multi_int_464_h264ref']
                base_datas[102]['column' + str(new_index)] = comparsion_datas['peak_multi_int_471_omnetpp']
                base_datas[103]['column' + str(new_index)] = comparsion_datas['peak_multi_int_473_astar']
                base_datas[104]['column' + str(new_index)] = comparsion_datas['peak_multi_int_483_xalancbmk']
                base_datas[105]['column' + str(new_index)] = comparsion_datas['peak_multi_int_SPECint_2006']
                base_datas[106]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_410_bwaves']
                base_datas[107]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_416_gamess']
                base_datas[108]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_433_milc']
                base_datas[109]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_434_zeusmp']
                base_datas[110]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_435_gromacs']
                base_datas[111]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_436_cactusADM']
                base_datas[112]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_437_leslie3d']
                base_datas[113]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_444_namd']
                base_datas[114]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_447_dealII']
                base_datas[115]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_450_soplex']
                base_datas[116]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_453_povray']
                base_datas[117]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_454_calculix']
                base_datas[118]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_459_GemsFDTD']
                base_datas[119]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_465_tonto']
                base_datas[120]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_470_lbm']
                base_datas[121]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_481_wrf']
                base_datas[122]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_482_sphinx3']
                base_datas[123]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_SPECfp_2006']
                # 在datas中增加计算数据
                base_datas[0]['column' + str(new_index + 1)] =  "%.2f%%" % ((base_datas[0]['column'+str(new_index)] - base_datas[0]['column5'])/base_datas[0]['column5'] * 100)
                base_datas[1]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[1]['column'+str(new_index)] - base_datas[1]['column5'])/base_datas[1]['column5'] * 100)
                base_datas[2]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[2]['column'+str(new_index)] - base_datas[2]['column5'])/base_datas[2]['column5'] * 100)
                base_datas[3]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[3]['column'+str(new_index)] - base_datas[3]['column5'])/base_datas[3]['column5'] * 100)
                base_datas[4]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[4]['column'+str(new_index)] - base_datas[4]['column5'])/base_datas[4]['column5'] * 100)
                base_datas[5]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[5]['column'+str(new_index)] - base_datas[5]['column5'])/base_datas[5]['column5'] * 100)
                base_datas[6]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[6]['column'+str(new_index)] - base_datas[6]['column5'])/base_datas[6]['column5'] * 100)
                base_datas[7]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[7]['column'+str(new_index)] - base_datas[7]['column5'])/base_datas[7]['column5'] * 100)
                base_datas[8]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[8]['column'+str(new_index)] - base_datas[8]['column5'])/base_datas[8]['column5'] * 100)
                base_datas[9]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[9]['column'+str(new_index)] - base_datas[9]['column5'])/base_datas[9]['column5'] * 100)
                base_datas[10]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[10]['column'+str(new_index)] - base_datas[10]['column5'])/base_datas[10]['column5'] * 100)
                base_datas[11]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[11]['column'+str(new_index)] - base_datas[11]['column5'])/base_datas[11]['column5'] * 100)
                base_datas[12]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[12]['column'+str(new_index)] - base_datas[12]['column5'])/base_datas[12]['column5'] * 100)
                base_datas[13]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[13]['column'+str(new_index)] - base_datas[13]['column5'])/base_datas[13]['column5'] * 100)
                base_datas[14]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[14]['column'+str(new_index)] - base_datas[14]['column5'])/base_datas[14]['column5'] * 100)
                base_datas[15]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[15]['column'+str(new_index)] - base_datas[15]['column5'])/base_datas[15]['column5'] * 100)
                base_datas[16]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[16]['column'+str(new_index)] - base_datas[16]['column5'])/base_datas[16]['column5'] * 100)
                base_datas[17]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[17]['column'+str(new_index)] - base_datas[17]['column5'])/base_datas[17]['column5'] * 100)
                base_datas[18]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[18]['column'+str(new_index)] - base_datas[18]['column5'])/base_datas[18]['column5'] * 100)
                base_datas[19]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[19]['column'+str(new_index)] - base_datas[19]['column5'])/base_datas[19]['column5'] * 100)
                base_datas[20]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[20]['column'+str(new_index)] - base_datas[20]['column5'])/base_datas[20]['column5'] * 100)
                base_datas[21]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[21]['column'+str(new_index)] - base_datas[21]['column5'])/base_datas[21]['column5'] * 100)
                base_datas[22]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[22]['column'+str(new_index)] - base_datas[22]['column5'])/base_datas[22]['column5'] * 100)
                base_datas[23]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[23]['column'+str(new_index)] - base_datas[23]['column5'])/base_datas[23]['column5'] * 100)
                base_datas[24]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[24]['column'+str(new_index)] - base_datas[24]['column5'])/base_datas[24]['column5'] * 100)
                base_datas[25]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[25]['column'+str(new_index)] - base_datas[25]['column5'])/base_datas[25]['column5'] * 100)
                base_datas[26]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[26]['column'+str(new_index)] - base_datas[26]['column5'])/base_datas[26]['column5'] * 100)
                base_datas[27]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[27]['column'+str(new_index)] - base_datas[27]['column5'])/base_datas[27]['column5'] * 100)
                base_datas[28]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[28]['column'+str(new_index)] - base_datas[28]['column5'])/base_datas[28]['column5'] * 100)
                base_datas[29]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[29]['column'+str(new_index)] - base_datas[29]['column5'])/base_datas[29]['column5'] * 100)
                base_datas[30]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[30]['column'+str(new_index)] - base_datas[30]['column5'])/base_datas[30]['column5'] * 100)
                base_datas[31]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[31]['column'+str(new_index)] - base_datas[31]['column5'])/base_datas[31]['column5'] * 100)
                base_datas[32]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[32]['column'+str(new_index)] - base_datas[32]['column5'])/base_datas[32]['column5'] * 100)
                base_datas[33]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[33]['column'+str(new_index)] - base_datas[33]['column5'])/base_datas[33]['column5'] * 100)
                base_datas[34]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[34]['column'+str(new_index)] - base_datas[34]['column5'])/base_datas[34]['column5'] * 100)
                base_datas[35]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[35]['column'+str(new_index)] - base_datas[35]['column5'])/base_datas[35]['column5'] * 100)
                base_datas[36]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[36]['column'+str(new_index)] - base_datas[36]['column5'])/base_datas[36]['column5'] * 100)
                base_datas[37]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[37]['column'+str(new_index)] - base_datas[37]['column5'])/base_datas[37]['column5'] * 100)
                base_datas[38]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[38]['column'+str(new_index)] - base_datas[38]['column5'])/base_datas[38]['column5'] * 100)
                base_datas[39]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[39]['column'+str(new_index)] - base_datas[39]['column5'])/base_datas[39]['column5'] * 100)
                base_datas[40]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[40]['column'+str(new_index)] - base_datas[40]['column5'])/base_datas[40]['column5'] * 100)
                base_datas[41]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[41]['column'+str(new_index)] - base_datas[41]['column5'])/base_datas[41]['column5'] * 100)
                base_datas[42]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[42]['column'+str(new_index)] - base_datas[42]['column5'])/base_datas[42]['column5'] * 100)
                base_datas[43]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[43]['column'+str(new_index)] - base_datas[43]['column5'])/base_datas[43]['column5'] * 100)
                base_datas[44]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[44]['column'+str(new_index)] - base_datas[44]['column5'])/base_datas[44]['column5'] * 100)
                base_datas[45]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[45]['column'+str(new_index)] - base_datas[45]['column5'])/base_datas[45]['column5'] * 100)
                base_datas[46]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[46]['column'+str(new_index)] - base_datas[46]['column5'])/base_datas[46]['column5'] * 100)
                base_datas[47]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[47]['column'+str(new_index)] - base_datas[47]['column5'])/base_datas[47]['column5'] * 100)
                base_datas[48]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[48]['column'+str(new_index)] - base_datas[48]['column5'])/base_datas[48]['column5'] * 100)
                base_datas[49]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[49]['column'+str(new_index)] - base_datas[49]['column5'])/base_datas[49]['column5'] * 100)
                base_datas[50]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[50]['column'+str(new_index)] - base_datas[50]['column5'])/base_datas[50]['column5'] * 100)
                base_datas[51]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[51]['column'+str(new_index)] - base_datas[51]['column5'])/base_datas[51]['column5'] * 100)
                base_datas[52]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[52]['column'+str(new_index)] - base_datas[52]['column5'])/base_datas[52]['column5'] * 100)
                base_datas[53]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[53]['column'+str(new_index)] - base_datas[53]['column5'])/base_datas[53]['column5'] * 100)
                base_datas[54]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[54]['column'+str(new_index)] - base_datas[54]['column5'])/base_datas[54]['column5'] * 100)
                base_datas[55]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[55]['column'+str(new_index)] - base_datas[55]['column5'])/base_datas[55]['column5'] * 100)
                base_datas[56]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[56]['column'+str(new_index)] - base_datas[56]['column5'])/base_datas[56]['column5'] * 100)
                base_datas[57]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[57]['column'+str(new_index)] - base_datas[57]['column5'])/base_datas[57]['column5'] * 100)
                base_datas[58]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[58]['column'+str(new_index)] - base_datas[58]['column5'])/base_datas[58]['column5'] * 100)
                base_datas[59]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[59]['column'+str(new_index)] - base_datas[59]['column5'])/base_datas[59]['column5'] * 100)
                base_datas[60]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[60]['column'+str(new_index)] - base_datas[60]['column5'])/base_datas[60]['column5'] * 100)
                base_datas[61]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[61]['column'+str(new_index)] - base_datas[61]['column5'])/base_datas[61]['column5'] * 100)
                base_datas[62]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[62]['column'+str(new_index)] - base_datas[62]['column5'])/base_datas[62]['column5'] * 100)
                base_datas[63]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[63]['column'+str(new_index)] - base_datas[63]['column5'])/base_datas[63]['column5'] * 100)
                base_datas[64]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[64]['column'+str(new_index)] - base_datas[64]['column5'])/base_datas[64]['column5'] * 100)
                base_datas[65]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[65]['column'+str(new_index)] - base_datas[65]['column5'])/base_datas[65]['column5'] * 100)
                base_datas[66]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[66]['column'+str(new_index)] - base_datas[66]['column5'])/base_datas[66]['column5'] * 100)
                base_datas[67]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[67]['column'+str(new_index)] - base_datas[67]['column5'])/base_datas[67]['column5'] * 100)
                base_datas[68]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[68]['column'+str(new_index)] - base_datas[68]['column5'])/base_datas[68]['column5'] * 100)
                base_datas[69]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[69]['column'+str(new_index)] - base_datas[69]['column5'])/base_datas[69]['column5'] * 100)
                base_datas[70]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[70]['column'+str(new_index)] - base_datas[70]['column5'])/base_datas[70]['column5'] * 100)
                base_datas[71]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[71]['column'+str(new_index)] - base_datas[71]['column5'])/base_datas[71]['column5'] * 100)
                base_datas[72]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[72]['column'+str(new_index)] - base_datas[72]['column5'])/base_datas[72]['column5'] * 100)
                base_datas[73]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[73]['column'+str(new_index)] - base_datas[73]['column5'])/base_datas[73]['column5'] * 100)
                base_datas[74]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[74]['column'+str(new_index)] - base_datas[74]['column5'])/base_datas[74]['column5'] * 100)
                base_datas[75]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[75]['column'+str(new_index)] - base_datas[75]['column5'])/base_datas[75]['column5'] * 100)
                base_datas[76]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[76]['column'+str(new_index)] - base_datas[76]['column5'])/base_datas[76]['column5'] * 100)
                base_datas[77]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[77]['column'+str(new_index)] - base_datas[77]['column5'])/base_datas[77]['column5'] * 100)
                base_datas[78]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[78]['column'+str(new_index)] - base_datas[78]['column5'])/base_datas[78]['column5'] * 100)
                base_datas[79]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[79]['column'+str(new_index)] - base_datas[79]['column5'])/base_datas[79]['column5'] * 100)
                base_datas[80]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[80]['column'+str(new_index)] - base_datas[80]['column5'])/base_datas[80]['column5'] * 100)
                base_datas[81]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[81]['column'+str(new_index)] - base_datas[81]['column5'])/base_datas[81]['column5'] * 100)
                base_datas[82]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[82]['column'+str(new_index)] - base_datas[82]['column5'])/base_datas[82]['column5'] * 100)
                base_datas[83]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[83]['column'+str(new_index)] - base_datas[83]['column5'])/base_datas[83]['column5'] * 100)
                base_datas[84]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[84]['column'+str(new_index)] - base_datas[84]['column5'])/base_datas[84]['column5'] * 100)
                base_datas[85]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[85]['column'+str(new_index)] - base_datas[85]['column5'])/base_datas[85]['column5'] * 100)
                base_datas[86]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[86]['column'+str(new_index)] - base_datas[86]['column5'])/base_datas[86]['column5'] * 100)
                base_datas[87]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[87]['column'+str(new_index)] - base_datas[87]['column5'])/base_datas[87]['column5'] * 100)
                base_datas[88]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[88]['column'+str(new_index)] - base_datas[88]['column5'])/base_datas[88]['column5'] * 100)
                base_datas[89]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[89]['column'+str(new_index)] - base_datas[89]['column5'])/base_datas[89]['column5'] * 100)
                base_datas[90]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[90]['column'+str(new_index)] - base_datas[90]['column5'])/base_datas[90]['column5'] * 100)
                base_datas[91]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[91]['column'+str(new_index)] - base_datas[91]['column5'])/base_datas[91]['column5'] * 100)
                base_datas[92]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[92]['column'+str(new_index)] - base_datas[92]['column5'])/base_datas[92]['column5'] * 100)
                base_datas[93]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[93]['column'+str(new_index)] - base_datas[93]['column5'])/base_datas[93]['column5'] * 100)
                base_datas[94]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[94]['column'+str(new_index)] - base_datas[94]['column5'])/base_datas[94]['column5'] * 100)
                base_datas[95]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[95]['column'+str(new_index)] - base_datas[95]['column5'])/base_datas[95]['column5'] * 100)
                base_datas[96]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[96]['column'+str(new_index)] - base_datas[96]['column5'])/base_datas[96]['column5'] * 100)
                base_datas[97]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[97]['column'+str(new_index)] - base_datas[97]['column5'])/base_datas[97]['column5'] * 100)
                base_datas[98]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[98]['column'+str(new_index)] - base_datas[98]['column5'])/base_datas[98]['column5'] * 100)
                base_datas[99]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[99]['column'+str(new_index)] - base_datas[99]['column5'])/base_datas[99]['column5'] * 100)
                base_datas[100]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[100]['column'+str(new_index)] - base_datas[100]['column5'])/base_datas[100]['column5'] * 100)
                base_datas[101]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[101]['column'+str(new_index)] - base_datas[101]['column5'])/base_datas[101]['column5'] * 100)
                base_datas[102]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[102]['column'+str(new_index)] - base_datas[102]['column5'])/base_datas[102]['column5'] * 100)
                base_datas[103]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[103]['column'+str(new_index)] - base_datas[103]['column5'])/base_datas[103]['column5'] * 100)
                base_datas[104]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[104]['column'+str(new_index)] - base_datas[104]['column5'])/base_datas[104]['column5'] * 100)
                base_datas[105]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[105]['column'+str(new_index)] - base_datas[105]['column5'])/base_datas[105]['column5'] * 100)
                base_datas[106]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[106]['column'+str(new_index)] - base_datas[106]['column5'])/base_datas[106]['column5'] * 100)
                base_datas[107]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[107]['column'+str(new_index)] - base_datas[107]['column5'])/base_datas[107]['column5'] * 100)
                base_datas[108]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[108]['column'+str(new_index)] - base_datas[108]['column5'])/base_datas[108]['column5'] * 100)
                base_datas[109]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[109]['column'+str(new_index)] - base_datas[109]['column5'])/base_datas[109]['column5'] * 100)
                base_datas[110]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[110]['column'+str(new_index)] - base_datas[110]['column5'])/base_datas[110]['column5'] * 100)
                base_datas[111]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[111]['column'+str(new_index)] - base_datas[111]['column5'])/base_datas[111]['column5'] * 100)
                base_datas[112]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[112]['column'+str(new_index)] - base_datas[112]['column5'])/base_datas[112]['column5'] * 100)
                base_datas[113]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[113]['column'+str(new_index)] - base_datas[113]['column5'])/base_datas[113]['column5'] * 100)
                base_datas[114]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[114]['column'+str(new_index)] - base_datas[114]['column5'])/base_datas[114]['column5'] * 100)
                base_datas[115]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[115]['column'+str(new_index)] - base_datas[115]['column5'])/base_datas[115]['column5'] * 100)
                base_datas[116]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[116]['column'+str(new_index)] - base_datas[116]['column5'])/base_datas[116]['column5'] * 100)
                base_datas[117]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[117]['column'+str(new_index)] - base_datas[117]['column5'])/base_datas[117]['column5'] * 100)
                base_datas[118]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[118]['column'+str(new_index)] - base_datas[118]['column5'])/base_datas[118]['column5'] * 100)
                base_datas[119]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[119]['column'+str(new_index)] - base_datas[119]['column5'])/base_datas[119]['column5'] * 100)
                base_datas[120]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[120]['column'+str(new_index)] - base_datas[120]['column5'])/base_datas[120]['column5'] * 100)
                base_datas[121]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[121]['column'+str(new_index)] - base_datas[121]['column5'])/base_datas[121]['column5'] * 100)
                base_datas[122]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[122]['column'+str(new_index)] - base_datas[122]['column5'])/base_datas[122]['column5'] * 100)
                base_datas[123]['column' + str(new_index + 1)] = "%.2f%%" % ((base_datas[123]['column'+str(new_index)] - base_datas[123]['column5'])/base_datas[123]['column5'] * 100)
        cpu2006_data = {'others': others, 'data': base_datas}
        return json_response(cpu2006_data, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_cpu2006_errors = []
        error_message = []
        for k, cpu2006_json in request.__dict__['data_cpu2006'].items():
            if k.lower().startswith('cpu2006'):
                constants.CPU2006_BOOL = True
                for key, value in cpu2006_json['items'].items():
                    data_cpu2006 = {}
                    data_cpu2006['env_id'] = request.__dict__['data_cpu2006']['env_id']
                    data_cpu2006['thread'] = key.split("_")[0]
                    data_cpu2006['thread'] = key.split("_")[0]
                    if key.split("_")[1] == "fp":
                        for key1 in value:
                            data_cpu2006['execute_cmd'] = "xx"
                            data_cpu2006['modify_parameters'] = "xx"
                            data_cpu2006['dtype'] = "fp"
                            data_cpu2006['tuneType'] = key1
                            data_cpu2006['fp_410_bwaves'] = value[key1]['410.bwaves']
                            data_cpu2006['fp_416_gamess'] = value[key1]['416.gamess']
                            data_cpu2006['fp_433_milc'] = value[key1]['433.milc']
                            data_cpu2006['fp_434_zeusmp'] = value[key1]['434.zeusmp']
                            data_cpu2006['fp_435_gromacs'] = value[key1]['435.gromacs']
                            data_cpu2006['fp_436_cactusADM'] = value[key1]['436.cactusADM']
                            data_cpu2006['fp_437_leslie3d'] = value[key1]['437.leslie3d']
                            data_cpu2006['fp_444_namd'] = value[key1]['444.namd']
                            data_cpu2006['fp_447_dealII'] = value[key1]['447.dealII']
                            data_cpu2006['fp_450_soplex'] = value[key1]['450.soplex']
                            data_cpu2006['fp_453_povray'] = value[key1]['453.povray']
                            data_cpu2006['fp_454_calculix'] = value[key1]['454.calculix']
                            data_cpu2006['fp_459_GemsFDTD'] = value[key1]['459.GemsFDTD']
                            data_cpu2006['fp_465_tonto'] = value[key1]['465.tonto']
                            data_cpu2006['fp_470_lbm'] = value[key1]['470.lbm']
                            data_cpu2006['fp_481_wrf'] = value[key1]['481.wrf']
                            data_cpu2006['fp_482_sphinx3'] = value[key1]['482.sphinx3']
                            data_cpu2006['fp_SPECfp_2006'] = value[key1]['SPECfp_2006']
                            data_cpu2006['test_time'] = return_time(cpu2006_json['time'])
                            serializer_cpu2006 = Cpu2006Serializer(data=data_cpu2006)
                            if serializer_cpu2006.is_valid():
                                self.perform_create(serializer_cpu2006)
                            serializer_cpu2006_errors.append(serializer_cpu2006.errors)
                            error_message.append(get_error_message(serializer_cpu2006))
                    elif key.split("_")[1] == "int":
                        for key1 in value:
                            data_cpu2006['execute_cmd'] = "xx"
                            data_cpu2006['modify_parameters'] = "xx"
                            data_cpu2006['dtype'] = "int"
                            data_cpu2006['tuneType'] = key1
                            data_cpu2006['int_400_perlbench'] = value[key1]['400.perlbench']
                            data_cpu2006['int_401_bzip2'] = value[key1]['401.bzip2']
                            data_cpu2006['int_403_gcc'] = value[key1]['403.gcc']
                            data_cpu2006['int_429_mcf'] = value[key1]['429.mcf']
                            data_cpu2006['int_445_gobmk'] = value[key1]['445.gobmk']
                            data_cpu2006['int_456_hmmer'] = value[key1]['456.hmmer']
                            data_cpu2006['int_458_sjeng'] = value[key1]['458.sjeng']
                            data_cpu2006['int_462_libquantum'] = value[key1]['462.libquantum']
                            data_cpu2006['int_464_h264ref'] = value[key1]['464.h264ref']
                            data_cpu2006['int_471_omnetpp'] = value[key1]['471.omnetpp']
                            data_cpu2006['int_473_astar'] = value[key1]['473.astar']
                            data_cpu2006['int_483_xalancbmk'] = value[key1]['483.xalancbmk']
                            data_cpu2006['int_SPECint_2006'] = value[key1]['SPECint_2006']
                            data_cpu2006['test_time'] = return_time(cpu2006_json['time'])
                            serializer_cpu2006 = Cpu2006Serializer(data=data_cpu2006)
                            if serializer_cpu2006.is_valid():
                                self.perform_create(serializer_cpu2006)
                            serializer_cpu2006_errors.append(serializer_cpu2006.errors)
                            error_message.append(get_error_message(serializer_cpu2006))

        return json_response(serializer_cpu2006_errors, status.HTTP_400_BAD_REQUEST,
                             error_message)
