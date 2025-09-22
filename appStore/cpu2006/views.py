"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 11:15:07 2024 +0800
"""
import numpy as np
# Create your views here.
from rest_framework import status

from appStore.cpu2006.models import Cpu2006
from appStore.cpu2006.serializers import Cpu2006Serializer
from appStore.utils.common import json_response, get_error_message
from appStore.utils.customer_view import CusModelViewSet


class Cpu2006ViewSet(CusModelViewSet):
    """
    Cpu2006数据管理
    """
    queryset = Cpu2006.objects.all().order_by('id')
    serializer_class = Cpu2006Serializer

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        serializer = self.get_serializer(serializer_, many=True)
        # thread dtype tuneType
        # 先判断数据的TuneType确定是base还是peak
        # 在判断数据的thread确定是单线程还是多线程
        # 在判断tuneType确定是int还是fp
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            # 基准数据和对比数据的全部数据
            datas[0]['column' + str(column_index)] = 'Cpu2006#' + str(title_index)
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            # 初始化所有数据为None
            for i in range(3, 127):
                datas[i]['column' + str(column_index)] = None
            for data in serializer.data:
                # 判断数据的TuneType确定是base还是peak
                if data['tuneType'] == 'base':
                    if data['thread'] == '单线程':
                        if data['dtype'] == 'int':
                            datas[3]['column' + str(column_index)] = data['int_400_perlbench']
                            datas[4]['column' + str(column_index)] = data['int_401_bzip2']
                            datas[5]['column' + str(column_index)] = data['int_403_gcc']
                            datas[6]['column' + str(column_index)] = data['int_429_mcf']
                            datas[7]['column' + str(column_index)] = data['int_445_gobmk']
                            datas[8]['column' + str(column_index)] = data['int_456_hmmer']
                            datas[9]['column' + str(column_index)] = data['int_458_sjeng']
                            datas[10]['column' + str(column_index)] = data['int_462_libquantum']
                            datas[11]['column' + str(column_index)] = data['int_464_h264ref']
                            datas[12]['column' + str(column_index)] = data['int_471_omnetpp']
                            datas[13]['column' + str(column_index)] = data['int_473_astar']
                            datas[14]['column' + str(column_index)] = data['int_483_xalancbmk']
                            datas[15]['column' + str(column_index)] = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            datas[16]['column' + str(column_index)] = data['fp_410_bwaves']
                            datas[17]['column' + str(column_index)] = data['fp_416_gamess']
                            datas[18]['column' + str(column_index)] = data['fp_433_milc']
                            datas[19]['column' + str(column_index)] = data['fp_434_zeusmp']
                            datas[20]['column' + str(column_index)] = data['fp_435_gromacs']
                            datas[21]['column' + str(column_index)] = data['fp_436_cactusADM']
                            datas[22]['column' + str(column_index)] = data['fp_437_leslie3d']
                            datas[23]['column' + str(column_index)] = data['fp_444_namd']
                            datas[24]['column' + str(column_index)] = data['fp_447_dealII']
                            datas[25]['column' + str(column_index)] = data['fp_450_soplex']
                            datas[26]['column' + str(column_index)] = data['fp_453_povray']
                            datas[27]['column' + str(column_index)] = data['fp_454_calculix']
                            datas[28]['column' + str(column_index)] = data['fp_459_GemsFDTD']
                            datas[29]['column' + str(column_index)] = data['fp_465_tonto']
                            datas[30]['column' + str(column_index)] = data['fp_470_lbm']
                            datas[31]['column' + str(column_index)] = data['fp_481_wrf']
                            datas[32]['column' + str(column_index)] = data['fp_482_sphinx3']
                            datas[33]['column' + str(column_index)] = data['fp_SPECfp_2006']
                    elif data['thread'] == '多线程':
                        if data['dtype'] == 'int':
                            datas[34]['column' + str(column_index)] = data['int_400_perlbench']
                            datas[35]['column' + str(column_index)] = data['int_401_bzip2']
                            datas[36]['column' + str(column_index)] = data['int_403_gcc']
                            datas[37]['column' + str(column_index)] = data['int_429_mcf']
                            datas[38]['column' + str(column_index)] = data['int_445_gobmk']
                            datas[39]['column' + str(column_index)] = data['int_456_hmmer']
                            datas[40]['column' + str(column_index)] = data['int_458_sjeng']
                            datas[41]['column' + str(column_index)] = data['int_462_libquantum']
                            datas[42]['column' + str(column_index)] = data['int_464_h264ref']
                            datas[43]['column' + str(column_index)] = data['int_471_omnetpp']
                            datas[44]['column' + str(column_index)] = data['int_473_astar']
                            datas[45]['column' + str(column_index)] = data['int_483_xalancbmk']
                            datas[46]['column' + str(column_index)] = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            datas[47]['column' + str(column_index)] = data['fp_410_bwaves']
                            datas[48]['column' + str(column_index)] = data['fp_416_gamess']
                            datas[49]['column' + str(column_index)] = data['fp_433_milc']
                            datas[50]['column' + str(column_index)] = data['fp_434_zeusmp']
                            datas[51]['column' + str(column_index)] = data['fp_435_gromacs']
                            datas[52]['column' + str(column_index)] = data['fp_436_cactusADM']
                            datas[53]['column' + str(column_index)] = data['fp_437_leslie3d']
                            datas[54]['column' + str(column_index)] = data['fp_444_namd']
                            datas[55]['column' + str(column_index)] = data['fp_447_dealII']
                            datas[56]['column' + str(column_index)] = data['fp_450_soplex']
                            datas[57]['column' + str(column_index)] = data['fp_453_povray']
                            datas[58]['column' + str(column_index)] = data['fp_454_calculix']
                            datas[59]['column' + str(column_index)] = data['fp_459_GemsFDTD']
                            datas[60]['column' + str(column_index)] = data['fp_465_tonto']
                            datas[61]['column' + str(column_index)] = data['fp_470_lbm']
                            datas[62]['column' + str(column_index)] = data['fp_481_wrf']
                            datas[63]['column' + str(column_index)] = data['fp_482_sphinx3']
                            datas[64]['column' + str(column_index)] = data['fp_SPECfp_2006']
                elif data['tuneType'] == 'peak':
                    if data['thread'] == '单线程':
                        if data['dtype'] == 'int':
                            datas[65]['column' + str(column_index)] = data['int_400_perlbench']
                            datas[66]['column' + str(column_index)] = data['int_401_bzip2']
                            datas[67]['column' + str(column_index)] = data['int_403_gcc']
                            datas[68]['column' + str(column_index)] = data['int_429_mcf']
                            datas[69]['column' + str(column_index)] = data['int_445_gobmk']
                            datas[70]['column' + str(column_index)] = data['int_456_hmmer']
                            datas[71]['column' + str(column_index)] = data['int_458_sjeng']
                            datas[72]['column' + str(column_index)] = data['int_462_libquantum']
                            datas[73]['column' + str(column_index)] = data['int_464_h264ref']
                            datas[74]['column' + str(column_index)] = data['int_471_omnetpp']
                            datas[75]['column' + str(column_index)] = data['int_473_astar']
                            datas[76]['column' + str(column_index)] = data['int_483_xalancbmk']
                            datas[77]['column' + str(column_index)] = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            datas[78]['column' + str(column_index)] = data['fp_410_bwaves']
                            datas[79]['column' + str(column_index)] = data['fp_416_gamess']
                            datas[80]['column' + str(column_index)] = data['fp_433_milc']
                            datas[81]['column' + str(column_index)] = data['fp_434_zeusmp']
                            datas[82]['column' + str(column_index)] = data['fp_435_gromacs']
                            datas[83]['column' + str(column_index)] = data['fp_436_cactusADM']
                            datas[84]['column' + str(column_index)] = data['fp_437_leslie3d']
                            datas[85]['column' + str(column_index)] = data['fp_444_namd']
                            datas[86]['column' + str(column_index)] = data['fp_447_dealII']
                            datas[87]['column' + str(column_index)] = data['fp_450_soplex']
                            datas[88]['column' + str(column_index)] = data['fp_453_povray']
                            datas[89]['column' + str(column_index)] = data['fp_454_calculix']
                            datas[90]['column' + str(column_index)] = data['fp_459_GemsFDTD']
                            datas[91]['column' + str(column_index)] = data['fp_465_tonto']
                            datas[92]['column' + str(column_index)] = data['fp_470_lbm']
                            datas[93]['column' + str(column_index)] = data['fp_481_wrf']
                            datas[94]['column' + str(column_index)] = data['fp_482_sphinx3']
                            datas[95]['column' + str(column_index)] = data['fp_SPECfp_2006']
                    elif data['thread'] == '多线程':
                        if data['dtype'] == 'int':
                            datas[96]['column' + str(column_index)] = data['int_400_perlbench']
                            datas[97]['column' + str(column_index)] = data['int_401_bzip2']
                            datas[98]['column' + str(column_index)] = data['int_403_gcc']
                            datas[99]['column' + str(column_index)] = data['int_429_mcf']
                            datas[100]['column' + str(column_index)] = data['int_445_gobmk']
                            datas[101]['column' + str(column_index)] = data['int_456_hmmer']
                            datas[102]['column' + str(column_index)] = data['int_458_sjeng']
                            datas[103]['column' + str(column_index)] = data['int_462_libquantum']
                            datas[104]['column' + str(column_index)] = data['int_464_h264ref']
                            datas[105]['column' + str(column_index)] = data['int_471_omnetpp']
                            datas[106]['column' + str(column_index)] = data['int_473_astar']
                            datas[107]['column' + str(column_index)] = data['int_483_xalancbmk']
                            datas[108]['column' + str(column_index)] = data['int_SPECint_2006']
                        elif data['dtype'] == 'fp':
                            datas[109]['column' + str(column_index)] = data['fp_410_bwaves']
                            datas[110]['column' + str(column_index)] = data['fp_416_gamess']
                            datas[111]['column' + str(column_index)] = data['fp_433_milc']
                            datas[112]['column' + str(column_index)] = data['fp_434_zeusmp']
                            datas[113]['column' + str(column_index)] = data['fp_435_gromacs']
                            datas[114]['column' + str(column_index)] = data['fp_436_cactusADM']
                            datas[115]['column' + str(column_index)] = data['fp_437_leslie3d']
                            datas[116]['column' + str(column_index)] = data['fp_444_namd']
                            datas[117]['column' + str(column_index)] = data['fp_447_dealII']
                            datas[118]['column' + str(column_index)] = data['fp_450_soplex']
                            datas[119]['column' + str(column_index)] = data['fp_453_povray']
                            datas[120]['column' + str(column_index)] = data['fp_454_calculix']
                            datas[121]['column' + str(column_index)] = data['fp_459_GemsFDTD']
                            datas[122]['column' + str(column_index)] = data['fp_465_tonto']
                            datas[123]['column' + str(column_index)] = data['fp_470_lbm']
                            datas[124]['column' + str(column_index)] = data['fp_481_wrf']
                            datas[125]['column' + str(column_index)] = data['fp_482_sphinx3']
                            datas[126]['column' + str(column_index)] = data['fp_SPECfp_2006']
            column_index += 1
            title_index += 1
            # 基准数据和对比数据的平均数据
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for i in range(127):
                if i > 2:
                    datas[i]['column' + str(column_index)] = datas[i]['column' + str(column_index - 1)]
            column_index += 1
        else:
            # 计算平均值
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
            average_base_single_int_400_perlbench = np.mean(base_single_int_400_perlbench_list).round(2) if not np.isnan(np.mean(base_single_int_400_perlbench_list)) else None
            average_base_single_int_401_bzip2 = np.mean(base_single_int_401_bzip2_list).round(2) if not np.isnan(np.mean(base_single_int_401_bzip2_list)) else None
            average_base_single_int_403_gcc = np.mean(base_single_int_403_gcc_list).round(2) if not np.isnan(np.mean(base_single_int_403_gcc_list)) else None
            average_base_single_int_429_mcf = np.mean(base_single_int_429_mcf_list).round(2) if not np.isnan(np.mean(base_single_int_429_mcf_list)) else None
            average_base_single_int_445_gobmk = np.mean(base_single_int_445_gobmk_list).round(2) if not np.isnan(np.mean(base_single_int_445_gobmk_list)) else None
            average_base_single_int_456_hmmer = np.mean(base_single_int_456_hmmer_list).round(2) if not np.isnan(np.mean(base_single_int_456_hmmer_list)) else None
            average_base_single_int_458_sjeng = np.mean(base_single_int_458_sjeng_list).round(2) if not np.isnan(np.mean(base_single_int_458_sjeng_list)) else None
            average_base_single_int_462_libquantum = np.mean(base_single_int_462_libquantum_list).round(2) if not np.isnan(np.mean(base_single_int_462_libquantum_list)) else None
            average_base_single_int_464_h264ref = np.mean(base_single_int_464_h264ref_list).round(2) if not np.isnan(np.mean(base_single_int_464_h264ref_list)) else None
            average_base_single_int_471_omnetpp = np.mean(base_single_int_471_omnetpp_list).round(2) if not np.isnan(np.mean(base_single_int_471_omnetpp_list)) else None
            average_base_single_int_473_astar = np.mean(base_single_int_473_astar_list).round(2) if not np.isnan(np.mean(base_single_int_473_astar_list)) else None
            average_base_single_int_483_xalancbmk = np.mean(base_single_int_483_xalancbmk_list).round(2) if not np.isnan(np.mean(base_single_int_483_xalancbmk_list)) else None
            average_base_single_int_SPECint_2006 = np.mean(base_single_int_SPECint_2006_list).round(2) if not np.isnan(np.mean(base_single_int_SPECint_2006_list)) else None
            average_base_single_fp_410_bwaves = np.mean(base_single_fp_410_bwaves_list).round(2) if not np.isnan(np.mean(base_single_fp_410_bwaves_list)) else None
            average_base_single_fp_416_gamess = np.mean(base_single_fp_416_gamess_list).round(2) if not np.isnan(np.mean(base_single_fp_416_gamess_list)) else None
            average_base_single_fp_433_milc = np.mean(base_single_fp_433_milc_list).round(2) if not np.isnan(np.mean(base_single_fp_433_milc_list)) else None
            average_base_single_fp_434_zeusmp = np.mean(base_single_fp_434_zeusmp_list).round(2) if not np.isnan(np.mean(base_single_fp_434_zeusmp_list)) else None
            average_base_single_fp_435_gromacs = np.mean(base_single_fp_435_gromacs_list).round(2) if not np.isnan(np.mean(base_single_fp_435_gromacs_list)) else None
            average_base_single_fp_436_cactusADM = np.mean(base_single_fp_436_cactusADM_list).round(2) if not np.isnan(np.mean(base_single_fp_436_cactusADM_list)) else None
            average_base_single_fp_437_leslie3d = np.mean(base_single_fp_437_leslie3d_list).round(2) if not np.isnan(np.mean(base_single_fp_437_leslie3d_list)) else None
            average_base_single_fp_444_namd = np.mean(base_single_fp_444_namd_list).round(2) if not np.isnan(np.mean(base_single_fp_444_namd_list)) else None
            average_base_single_fp_447_dealII = np.mean(base_single_fp_447_dealII_list).round(2) if not np.isnan(np.mean(base_single_fp_447_dealII_list)) else None
            average_base_single_fp_450_soplex = np.mean(base_single_fp_450_soplex_list).round(2) if not np.isnan(np.mean(base_single_fp_450_soplex_list)) else None
            average_base_single_fp_453_povray = np.mean(base_single_fp_453_povray_list).round(2) if not np.isnan(np.mean(base_single_fp_453_povray_list)) else None
            average_base_single_fp_454_calculix = np.mean(base_single_fp_454_calculix_list).round(2) if not np.isnan(np.mean(base_single_fp_454_calculix_list)) else None
            average_base_single_fp_459_GemsFDTD = np.mean(base_single_fp_459_GemsFDTD_list).round(2) if not np.isnan(np.mean(base_single_fp_459_GemsFDTD_list)) else None
            average_base_single_fp_465_tonto = np.mean(base_single_fp_465_tonto_list).round(2) if not np.isnan(np.mean(base_single_fp_465_tonto_list)) else None
            average_base_single_fp_470_lbm = np.mean(base_single_fp_470_lbm_list).round(2) if not np.isnan(np.mean(base_single_fp_470_lbm_list)) else None
            average_base_single_fp_481_wrf = np.mean(base_single_fp_481_wrf_list).round(2) if not np.isnan(np.mean(base_single_fp_481_wrf_list)) else None
            average_base_single_fp_482_sphinx3 = np.mean(base_single_fp_482_sphinx3_list).round(2) if not np.isnan(np.mean(base_single_fp_482_sphinx3_list)) else None
            average_base_single_fp_SPECfp_2006 = np.mean(base_single_fp_SPECfp_2006_list).round(2) if not np.isnan(np.mean(base_single_fp_SPECfp_2006_list)) else None
            average_base_multi_int_400_perlbench = np.mean(base_multi_int_400_perlbench_list).round(2) if not np.isnan(np.mean(base_multi_int_400_perlbench_list)) else None
            average_base_multi_int_401_bzip2 = np.mean(base_multi_int_401_bzip2_list).round(2) if not np.isnan(np.mean(base_multi_int_401_bzip2_list)) else None
            average_base_multi_int_403_gcc = np.mean(base_multi_int_403_gcc_list).round(2) if not np.isnan(np.mean(base_multi_int_403_gcc_list)) else None
            average_base_multi_int_429_mcf = np.mean(base_multi_int_429_mcf_list).round(2) if not np.isnan(np.mean(base_multi_int_429_mcf_list)) else None
            average_base_multi_int_445_gobmk = np.mean(base_multi_int_445_gobmk_list).round(2) if not np.isnan(np.mean(base_multi_int_445_gobmk_list)) else None
            average_base_multi_int_456_hmmer = np.mean(base_multi_int_456_hmmer_list).round(2) if not np.isnan(np.mean(base_multi_int_456_hmmer_list)) else None
            average_base_multi_int_458_sjeng = np.mean(base_multi_int_458_sjeng_list).round(2) if not np.isnan(np.mean(base_multi_int_458_sjeng_list)) else None
            average_base_multi_int_462_libquantum = np.mean(base_multi_int_462_libquantum_list).round(2) if not np.isnan(np.mean(base_multi_int_462_libquantum_list)) else None
            average_base_multi_int_464_h264ref = np.mean(base_multi_int_464_h264ref_list).round(2) if not np.isnan(np.mean(base_multi_int_464_h264ref_list)) else None
            average_base_multi_int_471_omnetpp = np.mean(base_multi_int_471_omnetpp_list).round(2) if not np.isnan(np.mean(base_multi_int_471_omnetpp_list)) else None
            average_base_multi_int_473_astar = np.mean(base_multi_int_473_astar_list).round(2) if not np.isnan(np.mean(base_multi_int_473_astar_list)) else None
            average_base_multi_int_483_xalancbmk = np.mean(base_multi_int_483_xalancbmk_list).round(2) if not np.isnan(np.mean(base_multi_int_483_xalancbmk_list)) else None
            average_base_multi_int_SPECint_2006 = np.mean(base_multi_int_SPECint_2006_list).round(2) if not np.isnan(np.mean(base_multi_int_SPECint_2006_list)) else None
            average_base_multi_fp_410_bwaves = np.mean(base_multi_fp_410_bwaves_list).round(2) if not np.isnan(np.mean(base_multi_fp_410_bwaves_list)) else None
            average_base_multi_fp_416_gamess = np.mean(base_multi_fp_416_gamess_list).round(2) if not np.isnan(np.mean(base_multi_fp_416_gamess_list)) else None
            average_base_multi_fp_433_milc = np.mean(base_multi_fp_433_milc_list).round(2) if not np.isnan(np.mean(base_multi_fp_433_milc_list)) else None
            average_base_multi_fp_434_zeusmp = np.mean(base_multi_fp_434_zeusmp_list).round(2) if not np.isnan(np.mean(base_multi_fp_434_zeusmp_list)) else None
            average_base_multi_fp_435_gromacs = np.mean(base_multi_fp_435_gromacs_list).round(2) if not np.isnan(np.mean(base_multi_fp_435_gromacs_list)) else None
            average_base_multi_fp_436_cactusADM = np.mean(base_multi_fp_436_cactusADM_list).round(2) if not np.isnan(np.mean(base_multi_fp_436_cactusADM_list)) else None
            average_base_multi_fp_437_leslie3d = np.mean(base_multi_fp_437_leslie3d_list).round(2) if not np.isnan(np.mean(base_multi_fp_437_leslie3d_list)) else None
            average_base_multi_fp_444_namd = np.mean(base_multi_fp_444_namd_list).round(2) if not np.isnan(np.mean(base_multi_fp_444_namd_list)) else None
            average_base_multi_fp_447_dealII = np.mean(base_multi_fp_447_dealII_list).round(2) if not np.isnan(np.mean(base_multi_fp_447_dealII_list)) else None
            average_base_multi_fp_450_soplex = np.mean(base_multi_fp_450_soplex_list).round(2) if not np.isnan(np.mean(base_multi_fp_450_soplex_list)) else None
            average_base_multi_fp_453_povray = np.mean(base_multi_fp_453_povray_list).round(2) if not np.isnan(np.mean(base_multi_fp_453_povray_list)) else None
            average_base_multi_fp_454_calculix = np.mean(base_multi_fp_454_calculix_list).round(2) if not np.isnan(np.mean(base_multi_fp_454_calculix_list)) else None
            average_base_multi_fp_459_GemsFDTD = np.mean(base_multi_fp_459_GemsFDTD_list).round(2) if not np.isnan(np.mean(base_multi_fp_459_GemsFDTD_list)) else None
            average_base_multi_fp_465_tonto = np.mean(base_multi_fp_465_tonto_list).round(2) if not np.isnan(np.mean(base_multi_fp_465_tonto_list)) else None
            average_base_multi_fp_470_lbm = np.mean(base_multi_fp_470_lbm_list).round(2) if not np.isnan(np.mean(base_multi_fp_470_lbm_list)) else None
            average_base_multi_fp_481_wrf = np.mean(base_multi_fp_481_wrf_list).round(2) if not np.isnan(np.mean(base_multi_fp_481_wrf_list)) else None
            average_base_multi_fp_482_sphinx3 = np.mean(base_multi_fp_482_sphinx3_list).round(2) if not np.isnan(np.mean(base_multi_fp_482_sphinx3_list)) else None
            average_base_multi_fp_SPECfp_2006 = np.mean(base_multi_fp_SPECfp_2006_list).round(2) if not np.isnan(np.mean(base_multi_fp_SPECfp_2006_list)) else None
            average_peak_single_int_400_perlbench = np.mean(peak_single_int_400_perlbench_list).round(2) if not np.isnan(np.mean(peak_single_int_400_perlbench_list)) else None
            average_peak_single_int_401_bzip2 = np.mean(peak_single_int_401_bzip2_list).round(2) if not np.isnan(np.mean(peak_single_int_401_bzip2_list)) else None
            average_peak_single_int_403_gcc = np.mean(peak_single_int_403_gcc_list).round(2) if not np.isnan(np.mean(peak_single_int_403_gcc_list)) else None
            average_peak_single_int_429_mcf = np.mean(peak_single_int_429_mcf_list).round(2) if not np.isnan(np.mean(peak_single_int_429_mcf_list)) else None
            average_peak_single_int_445_gobmk = np.mean(peak_single_int_445_gobmk_list).round(2) if not np.isnan(np.mean(peak_single_int_445_gobmk_list)) else None
            average_peak_single_int_456_hmmer = np.mean(peak_single_int_456_hmmer_list).round(2) if not np.isnan(np.mean(peak_single_int_456_hmmer_list)) else None
            average_peak_single_int_458_sjeng = np.mean(peak_single_int_458_sjeng_list).round(2) if not np.isnan(np.mean(peak_single_int_458_sjeng_list)) else None
            average_peak_single_int_462_libquantum = np.mean(peak_single_int_462_libquantum_list).round(2) if not np.isnan(np.mean(peak_single_int_462_libquantum_list)) else None
            average_peak_single_int_464_h264ref = np.mean(peak_single_int_464_h264ref_list).round(2) if not np.isnan(np.mean(peak_single_int_464_h264ref_list)) else None
            average_peak_single_int_471_omnetpp = np.mean(peak_single_int_471_omnetpp_list).round(2) if not np.isnan(np.mean(peak_single_int_471_omnetpp_list)) else None
            average_peak_single_int_473_astar = np.mean(peak_single_int_473_astar_list).round(2) if not np.isnan(np.mean(peak_single_int_473_astar_list)) else None
            average_peak_single_int_483_xalancbmk = np.mean(peak_single_int_483_xalancbmk_list).round(2) if not np.isnan(np.mean(peak_single_int_483_xalancbmk_list)) else None
            average_peak_single_int_SPECint_2006 = np.mean(peak_single_int_SPECint_2006_list).round(2) if not np.isnan(np.mean(peak_single_int_SPECint_2006_list)) else None
            average_peak_single_fp_410_bwaves = np.mean(peak_single_fp_410_bwaves_list).round(2) if not np.isnan(np.mean(peak_single_fp_410_bwaves_list)) else None
            average_peak_single_fp_416_gamess = np.mean(peak_single_fp_416_gamess_list).round(2) if not np.isnan(np.mean(peak_single_fp_416_gamess_list)) else None
            average_peak_single_fp_433_milc = np.mean(peak_single_fp_433_milc_list).round(2) if not np.isnan(np.mean(peak_single_fp_433_milc_list)) else None
            average_peak_single_fp_434_zeusmp = np.mean(peak_single_fp_434_zeusmp_list).round(2) if not np.isnan(np.mean(peak_single_fp_434_zeusmp_list)) else None
            average_peak_single_fp_435_gromacs = np.mean(peak_single_fp_435_gromacs_list).round(2) if not np.isnan(np.mean(peak_single_fp_435_gromacs_list)) else None
            average_peak_single_fp_436_cactusADM = np.mean(peak_single_fp_436_cactusADM_list).round(2) if not np.isnan(np.mean(peak_single_fp_436_cactusADM_list)) else None
            average_peak_single_fp_437_leslie3d = np.mean(peak_single_fp_437_leslie3d_list).round(2) if not np.isnan(np.mean(peak_single_fp_437_leslie3d_list)) else None
            average_peak_single_fp_444_namd = np.mean(peak_single_fp_444_namd_list).round(2) if not np.isnan(np.mean(peak_single_fp_444_namd_list)) else None
            average_peak_single_fp_447_dealII = np.mean(peak_single_fp_447_dealII_list).round(2) if not np.isnan(np.mean(peak_single_fp_447_dealII_list)) else None
            average_peak_single_fp_450_soplex = np.mean(peak_single_fp_450_soplex_list).round(2) if not np.isnan(np.mean(peak_single_fp_450_soplex_list)) else None
            average_peak_single_fp_453_povray = np.mean(peak_single_fp_453_povray_list).round(2) if not np.isnan(np.mean(peak_single_fp_453_povray_list)) else None
            average_peak_single_fp_454_calculix = np.mean(peak_single_fp_454_calculix_list).round(2) if not np.isnan(np.mean(peak_single_fp_454_calculix_list)) else None
            average_peak_single_fp_459_GemsFDTD = np.mean(peak_single_fp_459_GemsFDTD_list).round(2) if not np.isnan(np.mean(peak_single_fp_459_GemsFDTD_list)) else None
            average_peak_single_fp_465_tonto = np.mean(peak_single_fp_465_tonto_list).round(2) if not np.isnan(np.mean(peak_single_fp_465_tonto_list)) else None
            average_peak_single_fp_470_lbm = np.mean(peak_single_fp_470_lbm_list).round(2) if not np.isnan(np.mean(peak_single_fp_470_lbm_list)) else None
            average_peak_single_fp_481_wrf = np.mean(peak_single_fp_481_wrf_list).round(2) if not np.isnan(np.mean(peak_single_fp_481_wrf_list)) else None
            average_peak_single_fp_482_sphinx3 = np.mean(peak_single_fp_482_sphinx3_list).round(2) if not np.isnan(np.mean(peak_single_fp_482_sphinx3_list)) else None
            average_peak_single_fp_SPECfp_2006 = np.mean(peak_single_fp_SPECfp_2006_list).round(2) if not np.isnan(np.mean(peak_single_fp_SPECfp_2006_list)) else None
            average_peak_multi_int_400_perlbench = np.mean(peak_multi_int_400_perlbench_list).round(2) if not np.isnan(np.mean(peak_multi_int_400_perlbench_list)) else None
            average_peak_multi_int_401_bzip2 = np.mean(peak_multi_int_401_bzip2_list).round(2) if not np.isnan(np.mean(peak_multi_int_401_bzip2_list)) else None
            average_peak_multi_int_403_gcc = np.mean(peak_multi_int_403_gcc_list).round(2) if not np.isnan(np.mean(peak_multi_int_403_gcc_list)) else None
            average_peak_multi_int_429_mcf = np.mean(peak_multi_int_429_mcf_list).round(2) if not np.isnan(np.mean(peak_multi_int_429_mcf_list)) else None
            average_peak_multi_int_445_gobmk = np.mean(peak_multi_int_445_gobmk_list).round(2) if not np.isnan(np.mean(peak_multi_int_445_gobmk_list)) else None
            average_peak_multi_int_456_hmmer = np.mean(peak_multi_int_456_hmmer_list).round(2) if not np.isnan(np.mean(peak_multi_int_456_hmmer_list)) else None
            average_peak_multi_int_458_sjeng = np.mean(peak_multi_int_458_sjeng_list).round(2) if not np.isnan(np.mean(peak_multi_int_458_sjeng_list)) else None
            average_peak_multi_int_462_libquantum = np.mean(peak_multi_int_462_libquantum_list).round(2) if not np.isnan(np.mean(peak_multi_int_462_libquantum_list)) else None
            average_peak_multi_int_464_h264ref = np.mean(peak_multi_int_464_h264ref_list).round(2) if not np.isnan(np.mean(peak_multi_int_464_h264ref_list)) else None
            average_peak_multi_int_471_omnetpp = np.mean(peak_multi_int_471_omnetpp_list).round(2) if not np.isnan(np.mean(peak_multi_int_471_omnetpp_list)) else None
            average_peak_multi_int_473_astar = np.mean(peak_multi_int_473_astar_list).round(2) if not np.isnan(np.mean(peak_multi_int_473_astar_list)) else None
            average_peak_multi_int_483_xalancbmk = np.mean(peak_multi_int_483_xalancbmk_list).round(2) if not np.isnan(np.mean(peak_multi_int_483_xalancbmk_list)) else None
            average_peak_multi_int_SPECint_2006 = np.mean(peak_multi_int_SPECint_2006_list).round(2) if not np.isnan(np.mean(peak_multi_int_SPECint_2006_list)) else None
            average_peak_multi_fp_410_bwaves = np.mean(peak_multi_fp_410_bwaves_list).round(2) if not np.isnan(np.mean(peak_multi_fp_410_bwaves_list)) else None
            average_peak_multi_fp_416_gamess = np.mean(peak_multi_fp_416_gamess_list).round(2) if not np.isnan(np.mean(peak_multi_fp_416_gamess_list)) else None
            average_peak_multi_fp_433_milc = np.mean(peak_multi_fp_433_milc_list).round(2) if not np.isnan(np.mean(peak_multi_fp_433_milc_list)) else None
            average_peak_multi_fp_434_zeusmp = np.mean(peak_multi_fp_434_zeusmp_list).round(2) if not np.isnan(np.mean(peak_multi_fp_434_zeusmp_list)) else None
            average_peak_multi_fp_435_gromacs = np.mean(peak_multi_fp_435_gromacs_list).round(2) if not np.isnan(np.mean(peak_multi_fp_435_gromacs_list)) else None
            average_peak_multi_fp_436_cactusADM = np.mean(peak_multi_fp_436_cactusADM_list).round(2) if not np.isnan(np.mean(peak_multi_fp_436_cactusADM_list)) else None
            average_peak_multi_fp_437_leslie3d = np.mean(peak_multi_fp_437_leslie3d_list).round(2) if not np.isnan(np.mean(peak_multi_fp_437_leslie3d_list)) else None
            average_peak_multi_fp_444_namd = np.mean(peak_multi_fp_444_namd_list).round(2) if not np.isnan(np.mean(peak_multi_fp_444_namd_list)) else None
            average_peak_multi_fp_447_dealII = np.mean(peak_multi_fp_447_dealII_list).round(2) if not np.isnan(np.mean(peak_multi_fp_447_dealII_list)) else None
            average_peak_multi_fp_450_soplex = np.mean(peak_multi_fp_450_soplex_list).round(2) if not np.isnan(np.mean(peak_multi_fp_450_soplex_list)) else None
            average_peak_multi_fp_453_povray = np.mean(peak_multi_fp_453_povray_list).round(2) if not np.isnan(np.mean(peak_multi_fp_453_povray_list)) else None
            average_peak_multi_fp_454_calculix = np.mean(peak_multi_fp_454_calculix_list).round(2) if not np.isnan(np.mean(peak_multi_fp_454_calculix_list)) else None
            average_peak_multi_fp_459_GemsFDTD = np.mean(peak_multi_fp_459_GemsFDTD_list).round(2) if not np.isnan(np.mean(peak_multi_fp_459_GemsFDTD_list)) else None
            average_peak_multi_fp_465_tonto = np.mean(peak_multi_fp_465_tonto_list).round(2) if not np.isnan(np.mean(peak_multi_fp_465_tonto_list)) else None
            average_peak_multi_fp_470_lbm = np.mean(peak_multi_fp_470_lbm_list).round(2) if not np.isnan(np.mean(peak_multi_fp_470_lbm_list)) else None
            average_peak_multi_fp_481_wrf = np.mean(peak_multi_fp_481_wrf_list).round(2) if not np.isnan(np.mean(peak_multi_fp_481_wrf_list)) else None
            average_peak_multi_fp_482_sphinx3 = np.mean(peak_multi_fp_482_sphinx3_list).round(2) if not np.isnan(np.mean(peak_multi_fp_482_sphinx3_list)) else None
            average_peak_multi_fp_SPECfp_2006 = np.mean(peak_multi_fp_SPECfp_2006_list).round(2) if not np.isnan(np.mean(peak_multi_fp_SPECfp_2006_list)) else None

            # 查到mark-name相同的数据拼接为一组：serializer.data
            for mark_name in groups:
                temp_datas = serializer_.filter(mark_name=mark_name)
                datas[0]['column' + str(column_index)] = 'Cpu2006#' + str(title_index)
                datas[1]['column' + str(column_index)] = temp_datas[0].execute_cmd
                datas[2]['column' + str(column_index)] = temp_datas[0].modify_parameters
                # 基准数据和对比数据的全部数据
                # 初始化所有数据为None
                for i in range(3, 127):
                    datas[i]['column' + str(column_index)] = None
                for data in temp_datas:
                    # 判断数据的TuneType确定是base还是peak
                    if data.tuneType == 'base':
                        if data.thread == '单线程':
                            if data.dtype == 'int':
                                datas[3]['column' + str(column_index)] = data.int_400_perlbench
                                datas[4]['column' + str(column_index)] = data.int_401_bzip2
                                datas[5]['column' + str(column_index)] = data.int_403_gcc
                                datas[6]['column' + str(column_index)] = data.int_429_mcf
                                datas[7]['column' + str(column_index)] = data.int_445_gobmk
                                datas[8]['column' + str(column_index)] = data.int_456_hmmer
                                datas[9]['column' + str(column_index)] = data.int_458_sjeng
                                datas[10]['column' + str(column_index)] = data.int_462_libquantum
                                datas[11]['column' + str(column_index)] = data.int_464_h264ref
                                datas[12]['column' + str(column_index)] = data.int_471_omnetpp
                                datas[13]['column' + str(column_index)] = data.int_473_astar
                                datas[14]['column' + str(column_index)] = data.int_483_xalancbmk
                                datas[15]['column' + str(column_index)] = data.int_SPECint_2006
                            elif data.dtype == 'fp':
                                datas[16]['column' + str(column_index)] = data.fp_410_bwaves
                                datas[17]['column' + str(column_index)] = data.fp_416_gamess
                                datas[18]['column' + str(column_index)] = data.fp_433_milc
                                datas[19]['column' + str(column_index)] = data.fp_434_zeusmp
                                datas[20]['column' + str(column_index)] = data.fp_435_gromacs
                                datas[21]['column' + str(column_index)] = data.fp_436_cactusADM
                                datas[22]['column' + str(column_index)] = data.fp_437_leslie3d
                                datas[23]['column' + str(column_index)] = data.fp_444_namd
                                datas[24]['column' + str(column_index)] = data.fp_447_dealII
                                datas[25]['column' + str(column_index)] = data.fp_450_soplex
                                datas[26]['column' + str(column_index)] = data.fp_453_povray
                                datas[27]['column' + str(column_index)] = data.fp_454_calculix
                                datas[28]['column' + str(column_index)] = data.fp_459_GemsFDTD
                                datas[29]['column' + str(column_index)] = data.fp_465_tonto
                                datas[30]['column' + str(column_index)] = data.fp_470_lbm
                                datas[31]['column' + str(column_index)] = data.fp_481_wrf
                                datas[32]['column' + str(column_index)] = data.fp_482_sphinx3
                                datas[33]['column' + str(column_index)] = data.fp_SPECfp_2006
                        elif data.thread == '多线程':
                            if data.dtype == 'int':
                                datas[34]['column' + str(column_index)] = data.int_400_perlbench
                                datas[35]['column' + str(column_index)] = data.int_401_bzip2
                                datas[36]['column' + str(column_index)] = data.int_403_gcc
                                datas[37]['column' + str(column_index)] = data.int_429_mcf
                                datas[38]['column' + str(column_index)] = data.int_445_gobmk
                                datas[39]['column' + str(column_index)] = data.int_456_hmmer
                                datas[40]['column' + str(column_index)] = data.int_458_sjeng
                                datas[41]['column' + str(column_index)] = data.int_462_libquantum
                                datas[42]['column' + str(column_index)] = data.int_464_h264ref
                                datas[43]['column' + str(column_index)] = data.int_471_omnetpp
                                datas[44]['column' + str(column_index)] = data.int_473_astar
                                datas[45]['column' + str(column_index)] = data.int_483_xalancbmk
                                datas[46]['column' + str(column_index)] = data.int_SPECint_2006
                            elif data.dtype == 'fp':
                                datas[47]['column' + str(column_index)] = data.fp_410_bwaves
                                datas[48]['column' + str(column_index)] = data.fp_416_gamess
                                datas[49]['column' + str(column_index)] = data.fp_433_milc
                                datas[50]['column' + str(column_index)] = data.fp_434_zeusmp
                                datas[51]['column' + str(column_index)] = data.fp_435_gromacs
                                datas[52]['column' + str(column_index)] = data.fp_436_cactusADM
                                datas[53]['column' + str(column_index)] = data.fp_437_leslie3d
                                datas[54]['column' + str(column_index)] = data.fp_444_namd
                                datas[55]['column' + str(column_index)] = data.fp_447_dealII
                                datas[56]['column' + str(column_index)] = data.fp_450_soplex
                                datas[57]['column' + str(column_index)] = data.fp_453_povray
                                datas[58]['column' + str(column_index)] = data.fp_454_calculix
                                datas[59]['column' + str(column_index)] = data.fp_459_GemsFDTD
                                datas[60]['column' + str(column_index)] = data.fp_465_tonto
                                datas[61]['column' + str(column_index)] = data.fp_470_lbm
                                datas[62]['column' + str(column_index)] = data.fp_481_wrf
                                datas[63]['column' + str(column_index)] = data.fp_482_sphinx3
                                datas[64]['column' + str(column_index)] = data.fp_SPECfp_2006
                    elif data.tuneType == 'peak':
                        if data.thread == '单线程':
                            if data.dtype == 'int':
                                datas[65]['column' + str(column_index)] = data.int_400_perlbench
                                datas[66]['column' + str(column_index)] = data.int_401_bzip2
                                datas[67]['column' + str(column_index)] = data.int_403_gcc
                                datas[68]['column' + str(column_index)] = data.int_429_mcf
                                datas[69]['column' + str(column_index)] = data.int_445_gobmk
                                datas[70]['column' + str(column_index)] = data.int_456_hmmer
                                datas[71]['column' + str(column_index)] = data.int_458_sjeng
                                datas[72]['column' + str(column_index)] = data.int_462_libquantum
                                datas[73]['column' + str(column_index)] = data.int_464_h264ref
                                datas[74]['column' + str(column_index)] = data.int_471_omnetpp
                                datas[75]['column' + str(column_index)] = data.int_473_astar
                                datas[76]['column' + str(column_index)] = data.int_483_xalancbmk
                                datas[77]['column' + str(column_index)] = data.int_SPECint_2006
                            elif data.dtype == 'fp':
                                datas[78]['column' + str(column_index)] = data.fp_410_bwaves
                                datas[79]['column' + str(column_index)] = data.fp_416_gamess
                                datas[80]['column' + str(column_index)] = data.fp_433_milc
                                datas[81]['column' + str(column_index)] = data.fp_434_zeusmp
                                datas[82]['column' + str(column_index)] = data.fp_435_gromacs
                                datas[83]['column' + str(column_index)] = data.fp_436_cactusADM
                                datas[84]['column' + str(column_index)] = data.fp_437_leslie3d
                                datas[85]['column' + str(column_index)] = data.fp_444_namd
                                datas[86]['column' + str(column_index)] = data.fp_447_dealII
                                datas[87]['column' + str(column_index)] = data.fp_450_soplex
                                datas[88]['column' + str(column_index)] = data.fp_453_povray
                                datas[89]['column' + str(column_index)] = data.fp_454_calculix
                                datas[90]['column' + str(column_index)] = data.fp_459_GemsFDTD
                                datas[91]['column' + str(column_index)] = data.fp_465_tonto
                                datas[92]['column' + str(column_index)] = data.fp_470_lbm
                                datas[93]['column' + str(column_index)] = data.fp_481_wrf
                                datas[94]['column' + str(column_index)] = data.fp_482_sphinx3
                                datas[95]['column' + str(column_index)] = data.fp_SPECfp_2006
                        elif data.thread == '多线程':
                            if data.dtype == 'int':
                                datas[96]['column' + str(column_index)] = data.int_400_perlbench
                                datas[97]['column' + str(column_index)] = data.int_401_bzip2
                                datas[98]['column' + str(column_index)] = data.int_403_gcc
                                datas[99]['column' + str(column_index)] = data.int_429_mcf
                                datas[100]['column' + str(column_index)] = data.int_445_gobmk
                                datas[101]['column' + str(column_index)] = data.int_456_hmmer
                                datas[102]['column' + str(column_index)] = data.int_458_sjeng
                                datas[103]['column' + str(column_index)] = data.int_462_libquantum
                                datas[104]['column' + str(column_index)] = data.int_464_h264ref
                                datas[105]['column' + str(column_index)] = data.int_471_omnetpp
                                datas[106]['column' + str(column_index)] = data.int_473_astar
                                datas[107]['column' + str(column_index)] = data.int_483_xalancbmk
                                datas[108]['column' + str(column_index)] = data.int_SPECint_2006
                            elif data.dtype == 'fp':
                                datas[109]['column' + str(column_index)] = data.fp_410_bwaves
                                datas[110]['column' + str(column_index)] = data.fp_416_gamess
                                datas[111]['column' + str(column_index)] = data.fp_433_milc
                                datas[112]['column' + str(column_index)] = data.fp_434_zeusmp
                                datas[113]['column' + str(column_index)] = data.fp_435_gromacs
                                datas[114]['column' + str(column_index)] = data.fp_436_cactusADM
                                datas[115]['column' + str(column_index)] = data.fp_437_leslie3d
                                datas[116]['column' + str(column_index)] = data.fp_444_namd
                                datas[117]['column' + str(column_index)] = data.fp_447_dealII
                                datas[118]['column' + str(column_index)] = data.fp_450_soplex
                                datas[119]['column' + str(column_index)] = data.fp_453_povray
                                datas[120]['column' + str(column_index)] = data.fp_454_calculix
                                datas[121]['column' + str(column_index)] = data.fp_459_GemsFDTD
                                datas[122]['column' + str(column_index)] = data.fp_465_tonto
                                datas[123]['column' + str(column_index)] = data.fp_470_lbm
                                datas[124]['column' + str(column_index)] = data.fp_481_wrf
                                datas[125]['column' + str(column_index)] = data.fp_482_sphinx3
                                datas[126]['column' + str(column_index)] = data.fp_SPECfp_2006
                column_index += 1
                title_index += 1
            # 基准数据和对比数据的平均数据
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = average_base_single_int_400_perlbench
            datas[4]['column' + str(column_index)] = average_base_single_int_401_bzip2
            datas[5]['column' + str(column_index)] = average_base_single_int_403_gcc
            datas[6]['column' + str(column_index)] = average_base_single_int_429_mcf
            datas[7]['column' + str(column_index)] = average_base_single_int_445_gobmk
            datas[8]['column' + str(column_index)] = average_base_single_int_456_hmmer
            datas[9]['column' + str(column_index)] = average_base_single_int_458_sjeng
            datas[10]['column' + str(column_index)] = average_base_single_int_462_libquantum
            datas[11]['column' + str(column_index)] = average_base_single_int_464_h264ref
            datas[12]['column' + str(column_index)] = average_base_single_int_471_omnetpp
            datas[13]['column' + str(column_index)] = average_base_single_int_473_astar
            datas[14]['column' + str(column_index)] = average_base_single_int_483_xalancbmk
            datas[15]['column' + str(column_index)] = average_base_single_int_SPECint_2006
            datas[16]['column' + str(column_index)] = average_base_single_fp_410_bwaves
            datas[17]['column' + str(column_index)] = average_base_single_fp_416_gamess
            datas[18]['column' + str(column_index)] = average_base_single_fp_433_milc
            datas[19]['column' + str(column_index)] = average_base_single_fp_434_zeusmp
            datas[20]['column' + str(column_index)] = average_base_single_fp_435_gromacs
            datas[21]['column' + str(column_index)] = average_base_single_fp_436_cactusADM
            datas[22]['column' + str(column_index)] = average_base_single_fp_437_leslie3d
            datas[23]['column' + str(column_index)] = average_base_single_fp_444_namd
            datas[24]['column' + str(column_index)] = average_base_single_fp_447_dealII
            datas[25]['column' + str(column_index)] = average_base_single_fp_450_soplex
            datas[26]['column' + str(column_index)] = average_base_single_fp_453_povray
            datas[27]['column' + str(column_index)] = average_base_single_fp_454_calculix
            datas[28]['column' + str(column_index)] = average_base_single_fp_459_GemsFDTD
            datas[29]['column' + str(column_index)] = average_base_single_fp_465_tonto
            datas[30]['column' + str(column_index)] = average_base_single_fp_470_lbm
            datas[31]['column' + str(column_index)] = average_base_single_fp_481_wrf
            datas[32]['column' + str(column_index)] = average_base_single_fp_482_sphinx3
            datas[33]['column' + str(column_index)] = average_base_single_fp_SPECfp_2006
            datas[34]['column' + str(column_index)] = average_base_multi_int_400_perlbench
            datas[35]['column' + str(column_index)] = average_base_multi_int_401_bzip2
            datas[36]['column' + str(column_index)] = average_base_multi_int_403_gcc
            datas[37]['column' + str(column_index)] = average_base_multi_int_429_mcf
            datas[38]['column' + str(column_index)] = average_base_multi_int_445_gobmk
            datas[39]['column' + str(column_index)] = average_base_multi_int_456_hmmer
            datas[40]['column' + str(column_index)] = average_base_multi_int_458_sjeng
            datas[41]['column' + str(column_index)] = average_base_multi_int_462_libquantum
            datas[42]['column' + str(column_index)] = average_base_multi_int_464_h264ref
            datas[43]['column' + str(column_index)] = average_base_multi_int_471_omnetpp
            datas[44]['column' + str(column_index)] = average_base_multi_int_473_astar
            datas[45]['column' + str(column_index)] = average_base_multi_int_483_xalancbmk
            datas[46]['column' + str(column_index)] = average_base_multi_int_SPECint_2006
            datas[47]['column' + str(column_index)] = average_base_multi_fp_410_bwaves
            datas[48]['column' + str(column_index)] = average_base_multi_fp_416_gamess
            datas[49]['column' + str(column_index)] = average_base_multi_fp_433_milc
            datas[50]['column' + str(column_index)] = average_base_multi_fp_434_zeusmp
            datas[51]['column' + str(column_index)] = average_base_multi_fp_435_gromacs
            datas[52]['column' + str(column_index)] = average_base_multi_fp_436_cactusADM
            datas[53]['column' + str(column_index)] = average_base_multi_fp_437_leslie3d
            datas[54]['column' + str(column_index)] = average_base_multi_fp_444_namd
            datas[55]['column' + str(column_index)] = average_base_multi_fp_447_dealII
            datas[56]['column' + str(column_index)] = average_base_multi_fp_450_soplex
            datas[57]['column' + str(column_index)] = average_base_multi_fp_453_povray
            datas[58]['column' + str(column_index)] = average_base_multi_fp_454_calculix
            datas[59]['column' + str(column_index)] = average_base_multi_fp_459_GemsFDTD
            datas[60]['column' + str(column_index)] = average_base_multi_fp_465_tonto
            datas[61]['column' + str(column_index)] = average_base_multi_fp_470_lbm
            datas[62]['column' + str(column_index)] = average_base_multi_fp_481_wrf
            datas[63]['column' + str(column_index)] = average_base_multi_fp_482_sphinx3
            datas[64]['column' + str(column_index)] = average_base_multi_fp_SPECfp_2006
            datas[65]['column' + str(column_index)] = average_peak_single_int_400_perlbench
            datas[66]['column' + str(column_index)] = average_peak_single_int_401_bzip2
            datas[67]['column' + str(column_index)] = average_peak_single_int_403_gcc
            datas[68]['column' + str(column_index)] = average_peak_single_int_429_mcf
            datas[69]['column' + str(column_index)] = average_peak_single_int_445_gobmk
            datas[70]['column' + str(column_index)] = average_peak_single_int_456_hmmer
            datas[71]['column' + str(column_index)] = average_peak_single_int_458_sjeng
            datas[72]['column' + str(column_index)] = average_peak_single_int_462_libquantum
            datas[73]['column' + str(column_index)] = average_peak_single_int_464_h264ref
            datas[74]['column' + str(column_index)] = average_peak_single_int_471_omnetpp
            datas[75]['column' + str(column_index)] = average_peak_single_int_473_astar
            datas[76]['column' + str(column_index)] = average_peak_single_int_483_xalancbmk
            datas[77]['column' + str(column_index)] = average_peak_single_int_SPECint_2006
            datas[78]['column' + str(column_index)] = average_peak_single_fp_410_bwaves
            datas[79]['column' + str(column_index)] = average_peak_single_fp_416_gamess
            datas[80]['column' + str(column_index)] = average_peak_single_fp_433_milc
            datas[81]['column' + str(column_index)] = average_peak_single_fp_434_zeusmp
            datas[82]['column' + str(column_index)] = average_peak_single_fp_435_gromacs
            datas[83]['column' + str(column_index)] = average_peak_single_fp_436_cactusADM
            datas[84]['column' + str(column_index)] = average_peak_single_fp_437_leslie3d
            datas[85]['column' + str(column_index)] = average_peak_single_fp_444_namd
            datas[86]['column' + str(column_index)] = average_peak_single_fp_447_dealII
            datas[87]['column' + str(column_index)] = average_peak_single_fp_450_soplex
            datas[88]['column' + str(column_index)] = average_peak_single_fp_453_povray
            datas[89]['column' + str(column_index)] = average_peak_single_fp_454_calculix
            datas[90]['column' + str(column_index)] = average_peak_single_fp_459_GemsFDTD
            datas[91]['column' + str(column_index)] = average_peak_single_fp_465_tonto
            datas[92]['column' + str(column_index)] = average_peak_single_fp_470_lbm
            datas[93]['column' + str(column_index)] = average_peak_single_fp_481_wrf
            datas[94]['column' + str(column_index)] = average_peak_single_fp_482_sphinx3
            datas[95]['column' + str(column_index)] = average_peak_single_fp_SPECfp_2006
            datas[96]['column' + str(column_index)] = average_peak_multi_int_400_perlbench
            datas[97]['column' + str(column_index)] = average_peak_multi_int_401_bzip2
            datas[98]['column' + str(column_index)] = average_peak_multi_int_403_gcc
            datas[99]['column' + str(column_index)] = average_peak_multi_int_429_mcf
            datas[100]['column' + str(column_index)] = average_peak_multi_int_445_gobmk
            datas[101]['column' + str(column_index)] = average_peak_multi_int_456_hmmer
            datas[102]['column' + str(column_index)] = average_peak_multi_int_458_sjeng
            datas[103]['column' + str(column_index)] = average_peak_multi_int_462_libquantum
            datas[104]['column' + str(column_index)] = average_peak_multi_int_464_h264ref
            datas[105]['column' + str(column_index)] = average_peak_multi_int_471_omnetpp
            datas[106]['column' + str(column_index)] = average_peak_multi_int_473_astar
            datas[107]['column' + str(column_index)] = average_peak_multi_int_483_xalancbmk
            datas[108]['column' + str(column_index)] = average_peak_multi_int_SPECint_2006
            datas[109]['column' + str(column_index)] = average_peak_multi_fp_410_bwaves
            datas[110]['column' + str(column_index)] = average_peak_multi_fp_416_gamess
            datas[111]['column' + str(column_index)] = average_peak_multi_fp_433_milc
            datas[112]['column' + str(column_index)] = average_peak_multi_fp_434_zeusmp
            datas[113]['column' + str(column_index)] = average_peak_multi_fp_435_gromacs
            datas[114]['column' + str(column_index)] = average_peak_multi_fp_436_cactusADM
            datas[115]['column' + str(column_index)] = average_peak_multi_fp_437_leslie3d
            datas[116]['column' + str(column_index)] = average_peak_multi_fp_444_namd
            datas[117]['column' + str(column_index)] = average_peak_multi_fp_447_dealII
            datas[118]['column' + str(column_index)] = average_peak_multi_fp_450_soplex
            datas[119]['column' + str(column_index)] = average_peak_multi_fp_453_povray
            datas[120]['column' + str(column_index)] = average_peak_multi_fp_454_calculix
            datas[121]['column' + str(column_index)] = average_peak_multi_fp_459_GemsFDTD
            datas[122]['column' + str(column_index)] = average_peak_multi_fp_465_tonto
            datas[123]['column' + str(column_index)] = average_peak_multi_fp_470_lbm
            datas[124]['column' + str(column_index)] = average_peak_multi_fp_481_wrf
            datas[125]['column' + str(column_index)] = average_peak_multi_fp_482_sphinx3
            datas[126]['column' + str(column_index)] = average_peak_multi_fp_SPECfp_2006
            column_index += 1
        if not base_column_index:
            # 记录基准数据
            base_column_index = column_index - 1
        else:
            # 对比数据的对比值
            datas[0]['column' + str(column_index)] = '对比值'
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for i in range(127):
                    if i > 2:
                        datas[i]['column' + str(column_index)] = \
                            "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i]['column' + str(base_column_index)]) / datas[i]['column' + str(base_column_index)] * 100) if datas[i]['column' + str(column_index - 1)] is not None and datas[i]['column' + str(base_column_index)] is not None else None
            column_index += 1
        return datas, title_index, column_index, base_column_index

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
        datas = [{'column1': 'Cpu2006', 'column2': '', 'column3': '', 'column4': ''},
                 {'column1': '执行命令', 'column2': '', 'column3': '', 'column4': ''},
                 {'column1': '修改参数', 'column2': '', 'column3': '', 'column4': ''},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '400.perlbench'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '401.bzip2'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '403.gcc'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '429.mcf'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '445.gobmk'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '456.hmmer'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '458.sjeng'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '462.libquantum'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '464.h264ref'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '471.omnetpp'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '473.astar'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': '483.xalancbmk'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'SPECint_2006'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '410.bwaves'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '416.gamess'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '433.milc'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '434.zeusmp'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '435.gromacs'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '436.cactusADM'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '437.leslie3d'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '444.namd'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '447.dealII'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '450.soplex'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '453.povray'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '454.calculix'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '459.GemsFDTD'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '465.tonto'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '470.lbm'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '481.wrf'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': '482.sphinx3'},
                 {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'SPECfp_2006'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '400.perlbench'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '401.bzip2'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '403.gcc'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '429.mcf'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '445.gobmk'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '456.hmmer'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '458.sjeng'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '462.libquantum'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '464.h264ref'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '471.omnetpp'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '473.astar'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': '483.xalancbmk'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'SPECint_2006'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '410.bwaves'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '416.gamess'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '433.milc'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '434.zeusmp'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '435.gromacs'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '436.cactusADM'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '437.leslie3d'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '444.namd'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '447.dealII'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '450.soplex'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '453.povray'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '454.calculix'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '459.GemsFDTD'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '465.tonto'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '470.lbm'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '481.wrf'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': '482.sphinx3'},
                 {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'SPECfp_2006'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '400.perlbench'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '401.bzip2'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '403.gcc'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '429.mcf'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '445.gobmk'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '456.hmmer'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '458.sjeng'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '462.libquantum'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '464.h264ref'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '471.omnetpp'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '473.astar'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': '483.xalancbmk'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'SPECint_2006'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '410.bwaves'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '416.gamess'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '433.milc'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '434.zeusmp'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '435.gromacs'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '436.cactusADM'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '437.leslie3d'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '444.namd'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '447.dealII'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '450.soplex'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '453.povray'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '454.calculix'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '459.GemsFDTD'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '465.tonto'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '470.lbm'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '481.wrf'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': '482.sphinx3'},
                 {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'SPECfp_2006'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '400.perlbench'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '401.bzip2'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '403.gcc'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '429.mcf'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '445.gobmk'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '456.hmmer'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '458.sjeng'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '462.libquantum'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '464.h264ref'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '471.omnetpp'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '473.astar'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': '483.xalancbmk'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'SPECint_2006'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '410.bwaves'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '416.gamess'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '433.milc'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '434.zeusmp'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '435.gromacs'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '436.cactusADM'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '437.leslie3d'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '444.namd'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '447.dealII'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '450.soplex'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '453.povray'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '454.calculix'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '459.GemsFDTD'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '465.tonto'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '470.lbm'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '481.wrf'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': '482.sphinx3'},
                 {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'SPECfp_2006'},
                 ]
        title_index = 1
        column_index = 5
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)

        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Cpu2006.objects.filter(env_id=comparativeId).all()
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas, title_index, column_index, base_column_index)
        return json_response(datas, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_cpu2006_errors = []
        error_message = []
        for k, cpu2006_json in request.__dict__['data_cpu2006'].items():
            if k.lower().startswith('cpu2006'):
                for key, value in cpu2006_json['items'].items():
                    data_cpu2006 = {}
                    data_cpu2006['env_id'] = request.__dict__['data_cpu2006']['env_id']
                    data_cpu2006['thread'] = key.split("_")[0]
                    data_cpu2006['mark_name'] = k[-3:]
                    if key.split("_")[1] == "fp":
                        for key1 in value:
                            data_cpu2006['execute_cmd'] = cpu2006_json.get('execute_cmd')
                            data_cpu2006['modify_parameters'] = str(cpu2006_json.get('modify_parameters'))[1:-2] if cpu2006_json.get('modify_parameters') else None
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
                            data_cpu2006 = {key: value if not isinstance(value, str) or value != '' else None for
                                            key, value in data_cpu2006.items()}
                            serializer_cpu2006 = Cpu2006Serializer(data=data_cpu2006)
                            if serializer_cpu2006.is_valid():
                                self.perform_create(serializer_cpu2006)
                            else:
                                serializer_cpu2006_errors.append(serializer_cpu2006.errors)
                                error_message.append(get_error_message(serializer_cpu2006))
                    elif key.split("_")[1] == "int":
                        for key1 in value:
                            data_cpu2006['execute_cmd'] = cpu2006_json.get('execute_cmd')
                            data_cpu2006['modify_parameters'] = str(cpu2006_json.get('modify_parameters'))[1:-2] if cpu2006_json.get('modify_parameters') else None
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
                            data_cpu2006 = {key: value if not isinstance(value, str) or value != '' else None for
                                            key, value in data_cpu2006.items()}
                            serializer_cpu2006 = Cpu2006Serializer(data=data_cpu2006)
                            if serializer_cpu2006.is_valid():
                                self.perform_create(serializer_cpu2006)
                            else:
                                serializer_cpu2006_errors.append(serializer_cpu2006.errors)
                                error_message.append(get_error_message(serializer_cpu2006))
        if serializer_cpu2006_errors:
            print(serializer_cpu2006_errors, "cpu2006")
            return json_response(serializer_cpu2006_errors, status.HTTP_400_BAD_REQUEST,
                             error_message)
        else:
            return
