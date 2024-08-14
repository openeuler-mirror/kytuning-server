import math
import numpy as np

# Create your views here.
from rest_framework import status

from appStore.cpu2017.models import Cpu2017
from appStore.cpu2017.serializers import Cpu2017Serializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class Cpu2017ViewSet(CusModelViewSet):
    """
    Cpu2017数据管理
    """
    queryset = Cpu2017.objects.all().order_by('id')
    serializer_class = Cpu2017Serializer

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        # 初始化数据为空 否则如果下面只获取的单线程或者多线程另外一组获取不到可能会报错
        serializer = self.get_serializer(serializer_, many=True)

        # thread dtype tuneType
        # 先判断数据的TuneType确定是base还是peak
        # 在判断数据的thread确定是单线程还是多线程
        # 在判断tuneType确定是int还是fp
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            # 基准数据和对比数据的全部数据
            datas[0]['column' + str(column_index)] = 'Cpu2017#' + str(title_index)
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            # 初始化所有数据为空
            for i in range(5, 103):
                datas[i]['column' + str(column_index)] = None
            for data in serializer.data:
                # 判断数据的TuneType确定是base还是peak
                if data['tuneType'] == 'base':
                    if data['thread'] == '单线程':
                        if data['dtype'] == 'int':
                            datas[3]['column' + str(column_index)] = data['int_500_perlbench_r']
                            datas[4]['column' + str(column_index)] = data['int_502_gcc_r']
                            datas[5]['column' + str(column_index)] = data['int_505_mcf_r']
                            datas[6]['column' + str(column_index)] = data['int_520_omnetpp_r']
                            datas[7]['column' + str(column_index)] = data['int_523_xalancbmk_r']
                            datas[8]['column' + str(column_index)] = data['int_525_x264_r']
                            datas[9]['column' + str(column_index)] = data['int_531_deepsjeng_r']
                            datas[10]['column' + str(column_index)] = data['int_541_leela_r']
                            datas[11]['column' + str(column_index)] = data['int_548_exchange2_r']
                            datas[12]['column' + str(column_index)] = data['int_557_xz_r']
                            datas[13]['column' + str(column_index)] = data['int_SPECrate2017_int']
                        elif data['dtype'] == 'fp':
                            datas[14]['column' + str(column_index)] = data['fp_503_bwaves_r']
                            datas[15]['column' + str(column_index)] = data['fp_507_cactuBSSN_r']
                            datas[16]['column' + str(column_index)] = data['fp_508_namd_r']
                            datas[17]['column' + str(column_index)] = data['fp_510_parest_r']
                            datas[18]['column' + str(column_index)] = data['fp_511_povray_r']
                            datas[19]['column' + str(column_index)] = data['fp_519_lbm_r']
                            datas[20]['column' + str(column_index)] = data['fp_521_wrf_r']
                            datas[21]['column' + str(column_index)] = data['fp_526_blender_r']
                            datas[22]['column' + str(column_index)] = data['fp_527_cam4_r']
                            datas[23]['column' + str(column_index)] = data['fp_538_imagick_r']
                            datas[24]['column' + str(column_index)] = data['fp_544_nab_r']
                            datas[25]['column' + str(column_index)] = data['fp_549_fotonik3d_r']
                            datas[26]['column' + str(column_index)] = data['fp_554_roms_r']
                            datas[27]['column' + str(column_index)] = data['fp_PECrate2017_fp']
                    elif data['thread'] == '多线程':
                        if data['dtype'] == 'int':
                            datas[28]['column' + str(column_index)] = data['int_500_perlbench_r']
                            datas[29]['column' + str(column_index)] = data['int_502_gcc_r']
                            datas[30]['column' + str(column_index)] = data['int_505_mcf_r']
                            datas[31]['column' + str(column_index)] = data['int_520_omnetpp_r']
                            datas[32]['column' + str(column_index)] = data['int_523_xalancbmk_r']
                            datas[33]['column' + str(column_index)] = data['int_525_x264_r']
                            datas[34]['column' + str(column_index)] = data['int_531_deepsjeng_r']
                            datas[35]['column' + str(column_index)] = data['int_541_leela_r']
                            datas[36]['column' + str(column_index)] = data['int_548_exchange2_r']
                            datas[37]['column' + str(column_index)] = data['int_557_xz_r']
                            datas[38]['column' + str(column_index)] = data['int_SPECrate2017_int']
                        elif data['dtype'] == 'fp':
                            datas[39]['column' + str(column_index)] = data['fp_503_bwaves_r']
                            datas[40]['column' + str(column_index)] = data['fp_507_cactuBSSN_r']
                            datas[41]['column' + str(column_index)] = data['fp_508_namd_r']
                            datas[42]['column' + str(column_index)] = data['fp_510_parest_r']
                            datas[43]['column' + str(column_index)] = data['fp_511_povray_r']
                            datas[44]['column' + str(column_index)] = data['fp_519_lbm_r']
                            datas[45]['column' + str(column_index)] = data['fp_521_wrf_r']
                            datas[46]['column' + str(column_index)] = data['fp_526_blender_r']
                            datas[47]['column' + str(column_index)] = data['fp_527_cam4_r']
                            datas[48]['column' + str(column_index)] = data['fp_538_imagick_r']
                            datas[49]['column' + str(column_index)] = data['fp_544_nab_r']
                            datas[50]['column' + str(column_index)] = data['fp_549_fotonik3d_r']
                            datas[51]['column' + str(column_index)] = data['fp_554_roms_r']
                            datas[52]['column' + str(column_index)] = data['fp_PECrate2017_fp']
                elif data['tuneType'] == 'peak':
                    if data['thread'] == '单线程':
                        if data['dtype'] == 'int':
                            datas[53]['column' + str(column_index)] = data['int_500_perlbench_r']
                            datas[54]['column' + str(column_index)] = data['int_502_gcc_r']
                            datas[55]['column' + str(column_index)] = data['int_505_mcf_r']
                            datas[56]['column' + str(column_index)] = data['int_520_omnetpp_r']
                            datas[57]['column' + str(column_index)] = data['int_523_xalancbmk_r']
                            datas[58]['column' + str(column_index)] = data['int_525_x264_r']
                            datas[59]['column' + str(column_index)] = data['int_531_deepsjeng_r']
                            datas[60]['column' + str(column_index)] = data['int_541_leela_r']
                            datas[61]['column' + str(column_index)] = data['int_548_exchange2_r']
                            datas[62]['column' + str(column_index)] = data['int_557_xz_r']
                            datas[63]['column' + str(column_index)] = data['int_SPECrate2017_int']
                        elif data['dtype'] == 'fp':
                            datas[64]['column' + str(column_index)] = data['fp_503_bwaves_r']
                            datas[65]['column' + str(column_index)] = data['fp_507_cactuBSSN_r']
                            datas[66]['column' + str(column_index)] = data['fp_508_namd_r']
                            datas[67]['column' + str(column_index)] = data['fp_510_parest_r']
                            datas[68]['column' + str(column_index)] = data['fp_511_povray_r']
                            datas[69]['column' + str(column_index)] = data['fp_519_lbm_r']
                            datas[70]['column' + str(column_index)] = data['fp_521_wrf_r']
                            datas[71]['column' + str(column_index)] = data['fp_526_blender_r']
                            datas[72]['column' + str(column_index)] = data['fp_527_cam4_r']
                            datas[73]['column' + str(column_index)] = data['fp_538_imagick_r']
                            datas[74]['column' + str(column_index)] = data['fp_544_nab_r']
                            datas[75]['column' + str(column_index)] = data['fp_549_fotonik3d_r']
                            datas[76]['column' + str(column_index)] = data['fp_554_roms_r']
                            datas[77]['column' + str(column_index)] = data['fp_PECrate2017_fp']
                    elif data['thread'] == '多线程':
                        if data['dtype'] == 'int':
                            datas[78]['column' + str(column_index)] = data['int_500_perlbench_r']
                            datas[79]['column' + str(column_index)] = data['int_502_gcc_r']
                            datas[80]['column' + str(column_index)] = data['int_505_mcf_r']
                            datas[81]['column' + str(column_index)] = data['int_520_omnetpp_r']
                            datas[82]['column' + str(column_index)] = data['int_523_xalancbmk_r']
                            datas[83]['column' + str(column_index)] = data['int_525_x264_r']
                            datas[84]['column' + str(column_index)] = data['int_531_deepsjeng_r']
                            datas[85]['column' + str(column_index)] = data['int_541_leela_r']
                            datas[86]['column' + str(column_index)] = data['int_548_exchange2_r']
                            datas[87]['column' + str(column_index)] = data['int_557_xz_r']
                            datas[88]['column' + str(column_index)] = data['int_SPECrate2017_int']
                        elif data['dtype'] == 'fp':
                            datas[89]['column' + str(column_index)] = data['fp_503_bwaves_r']
                            datas[90]['column' + str(column_index)] = data['fp_507_cactuBSSN_r']
                            datas[91]['column' + str(column_index)] = data['fp_508_namd_r']
                            datas[92]['column' + str(column_index)] = data['fp_510_parest_r']
                            datas[93]['column' + str(column_index)] = data['fp_511_povray_r']
                            datas[94]['column' + str(column_index)] = data['fp_519_lbm_r']
                            datas[95]['column' + str(column_index)] = data['fp_521_wrf_r']
                            datas[96]['column' + str(column_index)] = data['fp_526_blender_r']
                            datas[97]['column' + str(column_index)] = data['fp_527_cam4_r']
                            datas[98]['column' + str(column_index)] = data['fp_538_imagick_r']
                            datas[99]['column' + str(column_index)] = data['fp_544_nab_r']
                            datas[100]['column' + str(column_index)] = data['fp_549_fotonik3d_r']
                            datas[101]['column' + str(column_index)] = data['fp_554_roms_r']
                            datas[102]['column' + str(column_index)] = data['fp_PECrate2017_fp']
            column_index += 1
            title_index += 1
            # 基准数据和对比数据的平均数据
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for i in range(103):
                if i > 2:
                    datas[i]['column' + str(column_index)] = datas[i]['column' + str(column_index - 1)]
            column_index += 1
            if not base_column_index:
                # 记录基准数据
                base_column_index = column_index - 1
            else:
               # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(103):
                    if i > 2:
                        datas[i]['column' + str(column_index)] = \
                            "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i]['column' + str(base_column_index)]) / datas[i]['column' + str(base_column_index)] * 100) if datas[i]['column' + str(column_index - 1)] is not None and datas[i]['column' + str(base_column_index)] is not None else None
                column_index += 1
        else:
            # 计算平均值
            base_single_data_ = serializer_.filter(tuneType='base').filter(thread='单线程')
            base_multi_data_ = serializer_.filter(tuneType='base').filter(thread='多线程')
            peak_single_data_ = serializer_.filter(tuneType='peak').filter(thread='单线程')
            peak_multi_data_ = serializer_.filter(tuneType='peak').filter(thread='多线程')
            # 将每个字典转换为NumPy数组
            base_single_int_rate_500_perlbench_r_list = [d.int_500_perlbench_r for d in base_single_data_ if d.int_500_perlbench_r is not None]
            base_single_int_rate_502_gcc_r_list = [d.int_502_gcc_r for d in base_single_data_ if d.int_502_gcc_r is not None]
            base_single_int_rate_505_mcf_r_list = [d.int_505_mcf_r for d in base_single_data_ if d.int_505_mcf_r is not None]
            base_single_int_rate_520_omnetpp_r_list = [d.int_520_omnetpp_r for d in base_single_data_ if d.int_520_omnetpp_r is not None]
            base_single_int_rate_523_xalancbmk_r_list = [d.int_523_xalancbmk_r for d in base_single_data_ if d.int_523_xalancbmk_r is not None]
            base_single_int_rate_525_x264_r_list = [d.int_525_x264_r for d in base_single_data_ if d.int_525_x264_r is not None]
            base_single_int_rate_531_deepsjeng_r_list = [d.int_531_deepsjeng_r for d in base_single_data_ if d.int_531_deepsjeng_r is not None]
            base_single_int_rate_541_leela_r_list = [d.int_541_leela_r for d in base_single_data_ if d.int_541_leela_r is not None]
            base_single_int_rate_548_exchange2_r_list = [d.int_548_exchange2_r for d in base_single_data_ if d.int_548_exchange2_r is not None]
            base_single_int_rate_557_xz_r_list = [d.int_557_xz_r for d in base_single_data_ if d.int_557_xz_r is not None]
            base_single_int_rate_SPECrate2017_int_list = [d.int_SPECrate2017_int for d in base_single_data_ if d.int_SPECrate2017_int is not None]
            base_single_fp_rate_503_bwaves_r_list = [d.fp_503_bwaves_r for d in base_single_data_ if d.fp_503_bwaves_r is not None]
            base_single_fp_rate_507_cactuBSSN_r_list = [d.fp_507_cactuBSSN_r for d in base_single_data_ if d.fp_507_cactuBSSN_r is not None]
            base_single_fp_rate_508_namd_r_list = [d.fp_508_namd_r for d in base_single_data_ if d.fp_508_namd_r is not None]
            base_single_fp_rate_510_parest_r_list = [d.fp_510_parest_r for d in base_single_data_ if d.fp_510_parest_r is not None]
            base_single_fp_rate_511_povray_r_list = [d.fp_511_povray_r for d in base_single_data_ if d.fp_511_povray_r is not None]
            base_single_fp_rate_519_lbm_r_list = [d.fp_519_lbm_r for d in base_single_data_ if d.fp_519_lbm_r is not None]
            base_single_fp_rate_521_wrf_r_list = [d.fp_521_wrf_r for d in base_single_data_ if d.fp_521_wrf_r is not None]
            base_single_fp_rate_526_blender_r_list = [d.fp_526_blender_r for d in base_single_data_ if d.fp_526_blender_r is not None]
            base_single_fp_rate_527_cam4_r_list = [d.fp_527_cam4_r for d in base_single_data_ if d.fp_527_cam4_r is not None]
            base_single_fp_rate_538_imagick_r_list = [d.fp_538_imagick_r for d in base_single_data_ if d.fp_538_imagick_r is not None]
            base_single_fp_rate_544_nab_r_list = [d.fp_544_nab_r for d in base_single_data_ if d.fp_544_nab_r is not None]
            base_single_fp_rate_549_fotonik3d_r_list = [d.fp_549_fotonik3d_r for d in base_single_data_ if d.fp_549_fotonik3d_r is not None]
            base_single_fp_rate_554_roms_r_list = [d.fp_554_roms_r for d in base_single_data_ if d.fp_554_roms_r is not None]
            base_single_fp_rate_PECrate2017_fp_list = [d.fp_PECrate2017_fp for d in base_single_data_ if d.fp_PECrate2017_fp is not None]
            base_multi_int_rate_500_perlbench_r_list = [d.int_500_perlbench_r for d in base_multi_data_ if d.int_500_perlbench_r is not None]
            base_multi_int_rate_502_gcc_r_list = [d.int_502_gcc_r for d in base_multi_data_ if d.int_502_gcc_r is not None]
            base_multi_int_rate_505_mcf_r_list = [d.int_505_mcf_r for d in base_multi_data_ if d.int_505_mcf_r is not None]
            base_multi_int_rate_520_omnetpp_r_list = [d.int_520_omnetpp_r for d in base_multi_data_ if d.int_520_omnetpp_r is not None]
            base_multi_int_rate_523_xalancbmk_r_list = [d.int_523_xalancbmk_r for d in base_multi_data_ if d.int_523_xalancbmk_r is not None]
            base_multi_int_rate_525_x264_r_list = [d.int_525_x264_r for d in base_multi_data_ if d.int_525_x264_r is not None]
            base_multi_int_rate_531_deepsjeng_r_list = [d.int_531_deepsjeng_r for d in base_multi_data_ if d.int_531_deepsjeng_r is not None]
            base_multi_int_rate_541_leela_r_list = [d.int_541_leela_r for d in base_multi_data_ if d.int_541_leela_r is not None]
            base_multi_int_rate_548_exchange2_r_list = [d.int_548_exchange2_r for d in base_multi_data_ if d.int_548_exchange2_r is not None]
            base_multi_int_rate_557_xz_r_list = [d.int_557_xz_r for d in base_multi_data_ if d.int_557_xz_r is not None]
            base_multi_int_rate_SPECrate2017_int_list = [d.int_SPECrate2017_int for d in base_multi_data_ if d.int_SPECrate2017_int is not None]
            base_multi_fp_rate_503_bwaves_r_list = [d.fp_503_bwaves_r for d in base_multi_data_ if d.fp_503_bwaves_r is not None]
            base_multi_fp_rate_507_cactuBSSN_r_list = [d.fp_507_cactuBSSN_r for d in base_multi_data_ if d.fp_507_cactuBSSN_r is not None]
            base_multi_fp_rate_508_namd_r_list = [d.fp_508_namd_r for d in base_multi_data_ if d.fp_508_namd_r is not None]
            base_multi_fp_rate_510_parest_r_list = [d.fp_510_parest_r for d in base_multi_data_ if d.fp_510_parest_r is not None]
            base_multi_fp_rate_511_povray_r_list = [d.fp_511_povray_r for d in base_multi_data_ if d.fp_511_povray_r is not None]
            base_multi_fp_rate_519_lbm_r_list = [d.fp_519_lbm_r for d in base_multi_data_ if d.fp_519_lbm_r is not None]
            base_multi_fp_rate_521_wrf_r_list = [d.fp_521_wrf_r for d in base_multi_data_ if d.fp_521_wrf_r is not None]
            base_multi_fp_rate_526_blender_r_list = [d.fp_526_blender_r for d in base_multi_data_ if d.fp_526_blender_r is not None]
            base_multi_fp_rate_527_cam4_r_list = [d.fp_527_cam4_r for d in base_multi_data_ if d.fp_527_cam4_r is not None]
            base_multi_fp_rate_538_imagick_r_list = [d.fp_538_imagick_r for d in base_multi_data_ if d.fp_538_imagick_r is not None]
            base_multi_fp_rate_544_nab_r_list = [d.fp_544_nab_r for d in base_multi_data_ if d.fp_544_nab_r is not None]
            base_multi_fp_rate_549_fotonik3d_r_list = [d.fp_549_fotonik3d_r for d in base_multi_data_ if d.fp_549_fotonik3d_r is not None]
            base_multi_fp_rate_554_roms_r_list = [d.fp_554_roms_r for d in base_multi_data_ if d.fp_554_roms_r is not None]
            base_multi_fp_rate_PECrate2017_fp_list = [d.fp_PECrate2017_fp for d in base_multi_data_ if d.fp_PECrate2017_fp is not None]
            peak_single_int_rate_500_perlbench_r_list = [d.int_500_perlbench_r for d in peak_single_data_ if d.int_500_perlbench_r is not None]
            peak_single_int_rate_502_gcc_r_list = [d.int_502_gcc_r for d in peak_single_data_ if d.int_502_gcc_r is not None]
            peak_single_int_rate_505_mcf_r_list = [d.int_505_mcf_r for d in peak_single_data_ if d.int_505_mcf_r is not None]
            peak_single_int_rate_520_omnetpp_r_list = [d.int_520_omnetpp_r for d in peak_single_data_ if d.int_520_omnetpp_r is not None]
            peak_single_int_rate_523_xalancbmk_r_list = [d.int_523_xalancbmk_r for d in peak_single_data_ if d.int_523_xalancbmk_r is not None]
            peak_single_int_rate_525_x264_r_list = [d.int_525_x264_r for d in peak_single_data_ if d.int_525_x264_r is not None]
            peak_single_int_rate_531_deepsjeng_r_list = [d.int_531_deepsjeng_r for d in peak_single_data_ if d.int_531_deepsjeng_r is not None]
            peak_single_int_rate_541_leela_r_list = [d.int_541_leela_r for d in peak_single_data_ if d.int_541_leela_r is not None]
            peak_single_int_rate_548_exchange2_r_list = [d.int_548_exchange2_r for d in peak_single_data_ if d.int_548_exchange2_r is not None]
            peak_single_int_rate_557_xz_r_list = [d.int_557_xz_r for d in peak_single_data_ if d.int_557_xz_r is not None]
            peak_single_int_rate_SPECrate2017_int_list = [d.int_SPECrate2017_int for d in peak_single_data_ if d.int_SPECrate2017_int is not None]
            peak_single_fp_rate_503_bwaves_r_list = [d.fp_503_bwaves_r for d in peak_single_data_ if d.fp_503_bwaves_r is not None]
            peak_single_fp_rate_507_cactuBSSN_r_list = [d.fp_507_cactuBSSN_r for d in peak_single_data_ if d.fp_507_cactuBSSN_r is not None]
            peak_single_fp_rate_508_namd_r_list = [d.fp_508_namd_r for d in peak_single_data_ if d.fp_508_namd_r is not None]
            peak_single_fp_rate_510_parest_r_list = [d.fp_510_parest_r for d in peak_single_data_ if d.fp_510_parest_r is not None]
            peak_single_fp_rate_511_povray_r_list = [d.fp_511_povray_r for d in peak_single_data_ if d.fp_511_povray_r is not None]
            peak_single_fp_rate_519_lbm_r_list = [d.fp_519_lbm_r for d in peak_single_data_ if d.fp_519_lbm_r is not None]
            peak_single_fp_rate_521_wrf_r_list = [d.fp_521_wrf_r for d in peak_single_data_ if d.fp_521_wrf_r is not None]
            peak_single_fp_rate_526_blender_r_list = [d.fp_526_blender_r for d in peak_single_data_ if d.fp_526_blender_r is not None]
            peak_single_fp_rate_527_cam4_r_list = [d.fp_527_cam4_r for d in peak_single_data_ if d.fp_527_cam4_r is not None]
            peak_single_fp_rate_538_imagick_r_list = [d.fp_538_imagick_r for d in peak_single_data_ if d.fp_538_imagick_r is not None]
            peak_single_fp_rate_544_nab_r_list = [d.fp_544_nab_r for d in peak_single_data_ if d.fp_544_nab_r is not None]
            peak_single_fp_rate_549_fotonik3d_r_list = [d.fp_549_fotonik3d_r for d in peak_single_data_ if d.fp_549_fotonik3d_r is not None]
            peak_single_fp_rate_554_roms_r_list = [d.fp_554_roms_r for d in peak_single_data_ if d.fp_554_roms_r is not None]
            peak_single_fp_rate_PECrate2017_fp_list = [d.fp_PECrate2017_fp for d in peak_single_data_ if d.fp_PECrate2017_fp is not None]
            peak_multi_int_rate_500_perlbench_r_list = [d.int_500_perlbench_r for d in peak_multi_data_ if d.int_500_perlbench_r is not None]
            peak_multi_int_rate_502_gcc_r_list = [d.int_502_gcc_r for d in peak_multi_data_ if d.int_502_gcc_r is not None]
            peak_multi_int_rate_505_mcf_r_list = [d.int_505_mcf_r for d in peak_multi_data_ if d.int_505_mcf_r is not None]
            peak_multi_int_rate_520_omnetpp_r_list = [d.int_520_omnetpp_r for d in peak_multi_data_ if d.int_520_omnetpp_r is not None]
            peak_multi_int_rate_523_xalancbmk_r_list = [d.int_523_xalancbmk_r for d in peak_multi_data_ if d.int_523_xalancbmk_r is not None]
            peak_multi_int_rate_525_x264_r_list = [d.int_525_x264_r for d in peak_multi_data_ if d.int_525_x264_r is not None]
            peak_multi_int_rate_531_deepsjeng_r_list = [d.int_531_deepsjeng_r for d in peak_multi_data_ if d.int_531_deepsjeng_r is not None]
            peak_multi_int_rate_541_leela_r_list = [d.int_541_leela_r for d in peak_multi_data_ if d.int_541_leela_r is not None]
            peak_multi_int_rate_548_exchange2_r_list = [d.int_548_exchange2_r for d in peak_multi_data_ if d.int_548_exchange2_r is not None]
            peak_multi_int_rate_557_xz_r_list = [d.int_557_xz_r for d in peak_multi_data_ if d.int_557_xz_r is not None]
            peak_multi_int_rate_SPECrate2017_int_list = [d.int_SPECrate2017_int for d in peak_multi_data_ if d.int_SPECrate2017_int is not None]
            peak_multi_fp_rate_503_bwaves_r_list = [d.fp_503_bwaves_r for d in peak_multi_data_ if d.fp_503_bwaves_r is not None]
            peak_multi_fp_rate_507_cactuBSSN_r_list = [d.fp_507_cactuBSSN_r for d in peak_multi_data_ if d.fp_507_cactuBSSN_r is not None]
            peak_multi_fp_rate_508_namd_r_list = [d.fp_508_namd_r for d in peak_multi_data_ if d.fp_508_namd_r is not None]
            peak_multi_fp_rate_510_parest_r_list = [d.fp_510_parest_r for d in peak_multi_data_ if d.fp_510_parest_r is not None]
            peak_multi_fp_rate_511_povray_r_list = [d.fp_511_povray_r for d in peak_multi_data_ if d.fp_511_povray_r is not None]
            peak_multi_fp_rate_519_lbm_r_list = [d.fp_519_lbm_r for d in peak_multi_data_ if d.fp_519_lbm_r is not None]
            peak_multi_fp_rate_521_wrf_r_list = [d.fp_521_wrf_r for d in peak_multi_data_ if d.fp_521_wrf_r is not None]
            peak_multi_fp_rate_526_blender_r_list = [d.fp_526_blender_r for d in peak_multi_data_ if d.fp_526_blender_r is not None]
            peak_multi_fp_rate_527_cam4_r_list = [d.fp_527_cam4_r for d in peak_multi_data_ if d.fp_527_cam4_r is not None]
            peak_multi_fp_rate_538_imagick_r_list = [d.fp_538_imagick_r for d in peak_multi_data_ if d.fp_538_imagick_r is not None]
            peak_multi_fp_rate_544_nab_r_list = [d.fp_544_nab_r for d in peak_multi_data_ if d.fp_544_nab_r is not None]
            peak_multi_fp_rate_549_fotonik3d_r_list = [d.fp_549_fotonik3d_r for d in peak_multi_data_ if d.fp_549_fotonik3d_r is not None]
            peak_multi_fp_rate_554_roms_r_list = [d.fp_554_roms_r for d in peak_multi_data_ if d.fp_554_roms_r is not None]
            peak_multi_fp_rate_PECrate2017_fp_list = [d.fp_PECrate2017_fp for d in peak_multi_data_ if d.fp_PECrate2017_fp is not None]

            # 计算每个数组的平均值
            average_base_single_int_rate_500_perlbench_r = np.mean(base_single_int_rate_500_perlbench_r_list).round(2) if not base_single_int_rate_500_perlbench_r_list else None
            average_base_single_int_rate_502_gcc_r = np.mean(base_single_int_rate_502_gcc_r_list).round(2) if not base_single_int_rate_502_gcc_r_list else None
            average_base_single_int_rate_505_mcf_r = np.mean(base_single_int_rate_505_mcf_r_list).round(2) if not base_single_int_rate_505_mcf_r_list else None
            average_base_single_int_rate_520_omnetpp_r = np.mean(base_single_int_rate_520_omnetpp_r_list).round(2) if not base_single_int_rate_520_omnetpp_r_list else None
            average_base_single_int_rate_523_xalancbmk_r = np.mean(base_single_int_rate_523_xalancbmk_r_list).round(2) if not base_single_int_rate_523_xalancbmk_r_list else None
            average_base_single_int_rate_525_x264_r = np.mean(base_single_int_rate_525_x264_r_list).round(2) if not base_single_int_rate_525_x264_r_list else None
            average_base_single_int_rate_531_deepsjeng_r = np.mean(base_single_int_rate_531_deepsjeng_r_list).round(2) if not base_single_int_rate_531_deepsjeng_r_list else None
            average_base_single_int_rate_541_leela_r = np.mean(base_single_int_rate_541_leela_r_list).round(2) if not base_single_int_rate_541_leela_r_list else None
            average_base_single_int_rate_548_exchange2_r = np.mean(base_single_int_rate_548_exchange2_r_list).round(2) if not base_single_int_rate_548_exchange2_r_list else None
            average_base_single_int_rate_557_xz_r = np.mean(base_single_int_rate_557_xz_r_list).round(2) if not base_single_int_rate_557_xz_r_list else None
            average_base_single_int_rate_SPECrate2017_int = np.mean(base_single_int_rate_SPECrate2017_int_list).round(2) if not base_single_int_rate_SPECrate2017_int_list else None
            average_base_single_fp_rate_503_bwaves_r = np.mean(base_single_fp_rate_503_bwaves_r_list).round(2) if not base_single_fp_rate_503_bwaves_r_list else None
            average_base_single_fp_rate_507_cactuBSSN_r = np.mean(base_single_fp_rate_507_cactuBSSN_r_list).round(2) if not base_single_fp_rate_507_cactuBSSN_r_list else None
            average_base_single_fp_rate_508_namd_r = np.mean(base_single_fp_rate_508_namd_r_list).round(2) if not base_single_fp_rate_508_namd_r_list else None
            average_base_single_fp_rate_510_parest_r = np.mean(base_single_fp_rate_510_parest_r_list).round(2) if not base_single_fp_rate_510_parest_r_list else None
            average_base_single_fp_rate_511_povray_r = np.mean(base_single_fp_rate_511_povray_r_list).round(2) if not base_single_fp_rate_511_povray_r_list else None
            average_base_single_fp_rate_519_lbm_r = np.mean(base_single_fp_rate_519_lbm_r_list).round(2) if not base_single_fp_rate_519_lbm_r_list else None
            average_base_single_fp_rate_521_wrf_r = np.mean(base_single_fp_rate_521_wrf_r_list).round(2) if not base_single_fp_rate_521_wrf_r_list else None
            average_base_single_fp_rate_526_blender_r = np.mean(base_single_fp_rate_526_blender_r_list).round(2) if not base_single_fp_rate_526_blender_r_list else None
            average_base_single_fp_rate_527_cam4_r = np.mean(base_single_fp_rate_527_cam4_r_list).round(2) if not base_single_fp_rate_527_cam4_r_list else None
            average_base_single_fp_rate_538_imagick_r = np.mean(base_single_fp_rate_538_imagick_r_list).round(2) if not base_single_fp_rate_538_imagick_r_list else None
            average_base_single_fp_rate_544_nab_r = np.mean(base_single_fp_rate_544_nab_r_list).round(2) if not base_single_fp_rate_544_nab_r_list else None
            average_base_single_fp_rate_549_fotonik3d_r = np.mean(base_single_fp_rate_549_fotonik3d_r_list).round(2) if not base_single_fp_rate_549_fotonik3d_r_list else None
            average_base_single_fp_rate_554_roms_r = np.mean(base_single_fp_rate_554_roms_r_list).round(2) if not base_single_fp_rate_554_roms_r_list else None
            average_base_single_fp_rate_PECrate2017_fp = np.mean(base_single_fp_rate_PECrate2017_fp_list).round(2) if not base_single_fp_rate_PECrate2017_fp_list else None
            average_base_multi_int_rate_500_perlbench_r = np.mean(base_multi_int_rate_500_perlbench_r_list).round(2) if not base_multi_int_rate_500_perlbench_r_list else None
            average_base_multi_int_rate_502_gcc_r = np.mean(base_multi_int_rate_502_gcc_r_list).round(2) if not base_multi_int_rate_502_gcc_r_list else None
            average_base_multi_int_rate_505_mcf_r = np.mean(base_multi_int_rate_505_mcf_r_list).round(2) if not base_multi_int_rate_505_mcf_r_list else None
            average_base_multi_int_rate_520_omnetpp_r = np.mean(base_multi_int_rate_520_omnetpp_r_list).round(2) if not base_multi_int_rate_520_omnetpp_r_list else None
            average_base_multi_int_rate_523_xalancbmk_r = np.mean(base_multi_int_rate_523_xalancbmk_r_list).round(2) if not base_multi_int_rate_523_xalancbmk_r_list else None
            average_base_multi_int_rate_525_x264_r = np.mean(base_multi_int_rate_525_x264_r_list).round(2) if not base_multi_int_rate_525_x264_r_list else None
            average_base_multi_int_rate_531_deepsjeng_r = np.mean(base_multi_int_rate_531_deepsjeng_r_list).round(2) if not base_multi_int_rate_531_deepsjeng_r_list else None
            average_base_multi_int_rate_541_leela_r = np.mean(base_multi_int_rate_541_leela_r_list).round(2) if not base_multi_int_rate_541_leela_r_list else None
            average_base_multi_int_rate_548_exchange2_r = np.mean(base_multi_int_rate_548_exchange2_r_list).round(2) if not base_multi_int_rate_548_exchange2_r_list else None
            average_base_multi_int_rate_557_xz_r = np.mean(base_multi_int_rate_557_xz_r_list).round(2) if not base_multi_int_rate_557_xz_r_list else None
            average_base_multi_int_rate_SPECrate2017_int = np.mean(base_multi_int_rate_SPECrate2017_int_list).round(2) if not base_multi_int_rate_SPECrate2017_int_list else None
            average_base_multi_fp_rate_503_bwaves_r = np.mean(base_multi_fp_rate_503_bwaves_r_list).round(2) if not base_multi_fp_rate_503_bwaves_r_list else None
            average_base_multi_fp_rate_507_cactuBSSN_r = np.mean(base_multi_fp_rate_507_cactuBSSN_r_list).round(2) if not base_multi_fp_rate_507_cactuBSSN_r_list else None
            average_base_multi_fp_rate_508_namd_r = np.mean(base_multi_fp_rate_508_namd_r_list).round(2) if not base_multi_fp_rate_508_namd_r_list else None
            average_base_multi_fp_rate_510_parest_r = np.mean(base_multi_fp_rate_510_parest_r_list).round(2) if not base_multi_fp_rate_510_parest_r_list else None
            average_base_multi_fp_rate_511_povray_r = np.mean(base_multi_fp_rate_511_povray_r_list).round(2) if not base_multi_fp_rate_511_povray_r_list else None
            average_base_multi_fp_rate_519_lbm_r = np.mean(base_multi_fp_rate_519_lbm_r_list).round(2) if not base_multi_fp_rate_519_lbm_r_list else None
            average_base_multi_fp_rate_521_wrf_r = np.mean(base_multi_fp_rate_521_wrf_r_list).round(2) if not base_multi_fp_rate_521_wrf_r_list else None
            average_base_multi_fp_rate_526_blender_r = np.mean(base_multi_fp_rate_526_blender_r_list).round(2) if not base_multi_fp_rate_526_blender_r_list else None
            average_base_multi_fp_rate_527_cam4_r = np.mean(base_multi_fp_rate_527_cam4_r_list).round(2) if not base_multi_fp_rate_527_cam4_r_list else None
            average_base_multi_fp_rate_538_imagick_r = np.mean(base_multi_fp_rate_538_imagick_r_list).round(2) if not base_multi_fp_rate_538_imagick_r_list else None
            average_base_multi_fp_rate_544_nab_r = np.mean(base_multi_fp_rate_544_nab_r_list).round(2) if not base_multi_fp_rate_544_nab_r_list else None
            average_base_multi_fp_rate_549_fotonik3d_r = np.mean(base_multi_fp_rate_549_fotonik3d_r_list).round(2) if not base_multi_fp_rate_549_fotonik3d_r_list else None
            average_base_multi_fp_rate_554_roms_r = np.mean(base_multi_fp_rate_554_roms_r_list).round(2) if not base_multi_fp_rate_554_roms_r_list else None
            average_base_multi_fp_rate_PECrate2017_fp = np.mean(base_multi_fp_rate_PECrate2017_fp_list).round(2) if not base_multi_fp_rate_PECrate2017_fp_list else None
            average_peak_single_int_rate_500_perlbench_r = np.mean(peak_single_int_rate_500_perlbench_r_list).round(2) if not peak_single_int_rate_500_perlbench_r_list else None
            average_peak_single_int_rate_502_gcc_r = np.mean(peak_single_int_rate_502_gcc_r_list).round(2) if not peak_single_int_rate_502_gcc_r_list else None
            average_peak_single_int_rate_505_mcf_r = np.mean(peak_single_int_rate_505_mcf_r_list).round(2) if not peak_single_int_rate_505_mcf_r_list else None
            average_peak_single_int_rate_520_omnetpp_r = np.mean(peak_single_int_rate_520_omnetpp_r_list).round(2) if not peak_single_int_rate_520_omnetpp_r_list else None
            average_peak_single_int_rate_523_xalancbmk_r = np.mean(peak_single_int_rate_523_xalancbmk_r_list).round(2) if not peak_single_int_rate_523_xalancbmk_r_list else None
            average_peak_single_int_rate_525_x264_r = np.mean(peak_single_int_rate_525_x264_r_list).round(2) if not peak_single_int_rate_525_x264_r_list else None
            average_peak_single_int_rate_531_deepsjeng_r = np.mean(peak_single_int_rate_531_deepsjeng_r_list).round(2) if not peak_single_int_rate_531_deepsjeng_r_list else None
            average_peak_single_int_rate_541_leela_r = np.mean(peak_single_int_rate_541_leela_r_list).round(2) if not peak_single_int_rate_541_leela_r_list else None
            average_peak_single_int_rate_548_exchange2_r = np.mean(peak_single_int_rate_548_exchange2_r_list).round(2) if not peak_single_int_rate_548_exchange2_r_list else None
            average_peak_single_int_rate_557_xz_r = np.mean(peak_single_int_rate_557_xz_r_list).round(2) if not peak_single_int_rate_557_xz_r_list else None
            average_peak_single_int_rate_SPECrate2017_int = np.mean(peak_single_int_rate_SPECrate2017_int_list).round(2) if not peak_single_int_rate_SPECrate2017_int_list else None
            average_peak_single_fp_rate_503_bwaves_r = np.mean(peak_single_fp_rate_503_bwaves_r_list).round(2) if not peak_single_fp_rate_503_bwaves_r_list else None
            average_peak_single_fp_rate_507_cactuBSSN_r = np.mean(peak_single_fp_rate_507_cactuBSSN_r_list).round(2) if not peak_single_fp_rate_507_cactuBSSN_r_list else None
            average_peak_single_fp_rate_508_namd_r = np.mean(peak_single_fp_rate_508_namd_r_list).round(2) if not peak_single_fp_rate_508_namd_r_list else None
            average_peak_single_fp_rate_510_parest_r = np.mean(peak_single_fp_rate_510_parest_r_list).round(2) if not peak_single_fp_rate_510_parest_r_list else None
            average_peak_single_fp_rate_511_povray_r = np.mean(peak_single_fp_rate_511_povray_r_list).round(2) if not peak_single_fp_rate_511_povray_r_list else None
            average_peak_single_fp_rate_519_lbm_r = np.mean(peak_single_fp_rate_519_lbm_r_list).round(2) if not peak_single_fp_rate_519_lbm_r_list else None
            average_peak_single_fp_rate_521_wrf_r = np.mean(peak_single_fp_rate_521_wrf_r_list).round(2) if not peak_single_fp_rate_521_wrf_r_list else None
            average_peak_single_fp_rate_526_blender_r = np.mean(peak_single_fp_rate_526_blender_r_list).round(2) if not peak_single_fp_rate_526_blender_r_list else None
            average_peak_single_fp_rate_527_cam4_r = np.mean(peak_single_fp_rate_527_cam4_r_list).round(2) if not peak_single_fp_rate_527_cam4_r_list else None
            average_peak_single_fp_rate_538_imagick_r = np.mean(peak_single_fp_rate_538_imagick_r_list).round(2) if not peak_single_fp_rate_538_imagick_r_list else None
            average_peak_single_fp_rate_544_nab_r = np.mean(peak_single_fp_rate_544_nab_r_list).round(2) if not peak_single_fp_rate_544_nab_r_list else None
            average_peak_single_fp_rate_549_fotonik3d_r = np.mean(peak_single_fp_rate_549_fotonik3d_r_list).round(2) if not peak_single_fp_rate_549_fotonik3d_r_list else None
            average_peak_single_fp_rate_554_roms_r = np.mean(peak_single_fp_rate_554_roms_r_list).round(2) if not peak_single_fp_rate_554_roms_r_list else None
            average_peak_single_fp_rate_PECrate2017_fp = np.mean(peak_single_fp_rate_PECrate2017_fp_list).round(2) if not peak_single_fp_rate_PECrate2017_fp_list else None
            average_peak_multi_int_rate_500_perlbench_r = np.mean(peak_multi_int_rate_500_perlbench_r_list).round(2) if not peak_multi_int_rate_500_perlbench_r_list else None
            average_peak_multi_int_rate_502_gcc_r = np.mean(peak_multi_int_rate_502_gcc_r_list).round(2) if not peak_multi_int_rate_502_gcc_r_list else None
            average_peak_multi_int_rate_505_mcf_r = np.mean(peak_multi_int_rate_505_mcf_r_list).round(2) if not peak_multi_int_rate_505_mcf_r_list else None
            average_peak_multi_int_rate_520_omnetpp_r = np.mean(peak_multi_int_rate_520_omnetpp_r_list).round(2) if not peak_multi_int_rate_520_omnetpp_r_list else None
            average_peak_multi_int_rate_523_xalancbmk_r = np.mean(peak_multi_int_rate_523_xalancbmk_r_list).round(2) if not peak_multi_int_rate_523_xalancbmk_r_list else None
            average_peak_multi_int_rate_525_x264_r = np.mean(peak_multi_int_rate_525_x264_r_list).round(2) if not peak_multi_int_rate_525_x264_r_list else None
            average_peak_multi_int_rate_531_deepsjeng_r = np.mean(peak_multi_int_rate_531_deepsjeng_r_list).round(2) if not peak_multi_int_rate_531_deepsjeng_r_list else None
            average_peak_multi_int_rate_541_leela_r = np.mean(peak_multi_int_rate_541_leela_r_list).round(2) if not peak_multi_int_rate_541_leela_r_list else None
            average_peak_multi_int_rate_548_exchange2_r = np.mean(peak_multi_int_rate_548_exchange2_r_list).round(2) if not peak_multi_int_rate_548_exchange2_r_list else None
            average_peak_multi_int_rate_557_xz_r = np.mean(peak_multi_int_rate_557_xz_r_list).round(2) if not peak_multi_int_rate_557_xz_r_list else None
            average_peak_multi_int_rate_SPECrate2017_int = np.mean(peak_multi_int_rate_SPECrate2017_int_list).round(2) if not peak_multi_int_rate_SPECrate2017_int_list else None
            average_peak_multi_fp_rate_503_bwaves_r = np.mean(peak_multi_fp_rate_503_bwaves_r_list).round(2) if not peak_multi_fp_rate_503_bwaves_r_list else None
            average_peak_multi_fp_rate_507_cactuBSSN_r = np.mean(peak_multi_fp_rate_507_cactuBSSN_r_list).round(2) if not peak_multi_fp_rate_507_cactuBSSN_r_list else None
            average_peak_multi_fp_rate_508_namd_r = np.mean(peak_multi_fp_rate_508_namd_r_list).round(2) if not peak_multi_fp_rate_508_namd_r_list else None
            average_peak_multi_fp_rate_510_parest_r = np.mean(peak_multi_fp_rate_510_parest_r_list).round(2) if not peak_multi_fp_rate_510_parest_r_list else None
            average_peak_multi_fp_rate_511_povray_r = np.mean(peak_multi_fp_rate_511_povray_r_list).round(2) if not peak_multi_fp_rate_511_povray_r_list else None
            average_peak_multi_fp_rate_519_lbm_r = np.mean(peak_multi_fp_rate_519_lbm_r_list).round(2) if not peak_multi_fp_rate_519_lbm_r_list else None
            average_peak_multi_fp_rate_521_wrf_r = np.mean(peak_multi_fp_rate_521_wrf_r_list).round(2) if not peak_multi_fp_rate_521_wrf_r_list else None
            average_peak_multi_fp_rate_526_blender_r = np.mean(peak_multi_fp_rate_526_blender_r_list).round(2) if not peak_multi_fp_rate_526_blender_r_list else None
            average_peak_multi_fp_rate_527_cam4_r = np.mean(peak_multi_fp_rate_527_cam4_r_list).round(2) if not peak_multi_fp_rate_527_cam4_r_list else None
            average_peak_multi_fp_rate_538_imagick_r = np.mean(peak_multi_fp_rate_538_imagick_r_list).round(2) if not peak_multi_fp_rate_538_imagick_r_list else None
            average_peak_multi_fp_rate_544_nab_r = np.mean(peak_multi_fp_rate_544_nab_r_list).round(2) if not peak_multi_fp_rate_544_nab_r_list else None
            average_peak_multi_fp_rate_549_fotonik3d_r = np.mean(peak_multi_fp_rate_549_fotonik3d_r_list).round(2) if not peak_multi_fp_rate_549_fotonik3d_r_list else None
            average_peak_multi_fp_rate_554_roms_r = np.mean(peak_multi_fp_rate_554_roms_r_list).round(2) if not peak_multi_fp_rate_554_roms_r_list else None
            average_peak_multi_fp_rate_PECrate2017_fp = np.mean(peak_multi_fp_rate_PECrate2017_fp_list).round(2) if not peak_multi_fp_rate_PECrate2017_fp_list else None

            # 查到mark-name相同的数据拼接为一组：serializer.data
            for mark_name in groups:
                temp_datas = serializer_.filter(mark_name=mark_name)
                datas[0]['column' + str(column_index)] = 'Cpu2017#' + str(title_index)
                datas[1]['column' + str(column_index)] = temp_datas[0].execute_cmd
                datas[2]['column' + str(column_index)] = temp_datas[0].modify_parameters
                # 基准数据和对比数据的全部数据
                for data in temp_datas:
                    if data.tuneType == 'base':
                        if data.thread == '单线程':
                            if data.dtype == 'int':
                                datas[3]['column' + str(column_index)] = data.int_500_perlbench_r
                                datas[4]['column' + str(column_index)] = data.int_502_gcc_r
                                datas[5]['column' + str(column_index)] = data.int_505_mcf_r
                                datas[6]['column' + str(column_index)] = data.int_520_omnetpp_r
                                datas[7]['column' + str(column_index)] = data.int_523_xalancbmk_r
                                datas[8]['column' + str(column_index)] = data.int_525_x264_r
                                datas[9]['column' + str(column_index)] = data.int_531_deepsjeng_r
                                datas[10]['column' + str(column_index)] = data.int_541_leela_r
                                datas[11]['column' + str(column_index)] = data.int_548_exchange2_r
                                datas[12]['column' + str(column_index)] = data.int_557_xz_r
                                datas[13]['column' + str(column_index)] = data.int_SPECrate2017_int
                            elif data.dtype == 'fp':
                                datas[14]['column' + str(column_index)] = data.fp_503_bwaves_r
                                datas[15]['column' + str(column_index)] = data.fp_507_cactuBSSN_r
                                datas[16]['column' + str(column_index)] = data.fp_508_namd_r
                                datas[17]['column' + str(column_index)] = data.fp_510_parest_r
                                datas[18]['column' + str(column_index)] = data.fp_511_povray_r
                                datas[19]['column' + str(column_index)] = data.fp_519_lbm_r
                                datas[20]['column' + str(column_index)] = data.fp_521_wrf_r
                                datas[21]['column' + str(column_index)] = data.fp_526_blender_r
                                datas[22]['column' + str(column_index)] = data.fp_527_cam4_r
                                datas[23]['column' + str(column_index)] = data.fp_538_imagick_r
                                datas[24]['column' + str(column_index)] = data.fp_544_nab_r
                                datas[25]['column' + str(column_index)] = data.fp_549_fotonik3d_r
                                datas[26]['column' + str(column_index)] = data.fp_554_roms_r
                                datas[27]['column' + str(column_index)] = data.fp_PECrate2017_fp
                        elif data.thread == '多线程':
                            if data.dtype == 'int':
                                datas[28]['column' + str(column_index)] = data.int_500_perlbench_r
                                datas[29]['column' + str(column_index)] = data.int_502_gcc_r
                                datas[30]['column' + str(column_index)] = data.int_505_mcf_r
                                datas[31]['column' + str(column_index)] = data.int_520_omnetpp_r
                                datas[32]['column' + str(column_index)] = data.int_523_xalancbmk_r
                                datas[33]['column' + str(column_index)] = data.int_525_x264_r
                                datas[34]['column' + str(column_index)] = data.int_531_deepsjeng_r
                                datas[35]['column' + str(column_index)] = data.int_541_leela_r
                                datas[36]['column' + str(column_index)] = data.int_548_exchange2_r
                                datas[37]['column' + str(column_index)] = data.int_557_xz_r
                                datas[38]['column' + str(column_index)] = data.int_SPECrate2017_int
                            elif data.dtype == 'fp':
                                datas[39]['column' + str(column_index)] = data.fp_503_bwaves_r
                                datas[40]['column' + str(column_index)] = data.fp_507_cactuBSSN_r
                                datas[41]['column' + str(column_index)] = data.fp_508_namd_r
                                datas[42]['column' + str(column_index)] = data.fp_510_parest_r
                                datas[43]['column' + str(column_index)] = data.fp_511_povray_r
                                datas[44]['column' + str(column_index)] = data.fp_519_lbm_r
                                datas[45]['column' + str(column_index)] = data.fp_521_wrf_r
                                datas[46]['column' + str(column_index)] = data.fp_526_blender_r
                                datas[47]['column' + str(column_index)] = data.fp_527_cam4_r
                                datas[48]['column' + str(column_index)] = data.fp_538_imagick_r
                                datas[49]['column' + str(column_index)] = data.fp_544_nab_r
                                datas[50]['column' + str(column_index)] = data.fp_549_fotonik3d_r
                                datas[51]['column' + str(column_index)] = data.fp_554_roms_r
                                datas[52]['column' + str(column_index)] = data.fp_PECrate2017_fp
                    elif data.tuneType == 'peak':
                        if data.thread == '单线程':
                            if data.dtype == 'int':
                                datas[53]['column' + str(column_index)] = data.int_500_perlbench_r
                                datas[54]['column' + str(column_index)] = data.int_502_gcc_r
                                datas[55]['column' + str(column_index)] = data.int_505_mcf_r
                                datas[56]['column' + str(column_index)] = data.int_520_omnetpp_r
                                datas[57]['column' + str(column_index)] = data.int_523_xalancbmk_r
                                datas[58]['column' + str(column_index)] = data.int_525_x264_r
                                datas[59]['column' + str(column_index)] = data.int_531_deepsjeng_r
                                datas[60]['column' + str(column_index)] = data.int_541_leela_r
                                datas[61]['column' + str(column_index)] = data.int_548_exchange2_r
                                datas[62]['column' + str(column_index)] = data.int_557_xz_r
                                datas[63]['column' + str(column_index)] = data.int_SPECrate2017_int
                            elif data.dtype == 'fp':
                                datas[64]['column' + str(column_index)] = data.fp_503_bwaves_r
                                datas[65]['column' + str(column_index)] = data.fp_507_cactuBSSN_r
                                datas[66]['column' + str(column_index)] = data.fp_508_namd_r
                                datas[67]['column' + str(column_index)] = data.fp_510_parest_r
                                datas[68]['column' + str(column_index)] = data.fp_511_povray_r
                                datas[69]['column' + str(column_index)] = data.fp_519_lbm_r
                                datas[70]['column' + str(column_index)] = data.fp_521_wrf_r
                                datas[71]['column' + str(column_index)] = data.fp_526_blender_r
                                datas[72]['column' + str(column_index)] = data.fp_527_cam4_r
                                datas[73]['column' + str(column_index)] = data.fp_538_imagick_r
                                datas[74]['column' + str(column_index)] = data.fp_544_nab_r
                                datas[75]['column' + str(column_index)] = data.fp_549_fotonik3d_r
                                datas[76]['column' + str(column_index)] = data.fp_554_roms_r
                                datas[77]['column' + str(column_index)] = data.fp_PECrate2017_fp
                        elif data.thread == '多线程':
                            if data.dtype == 'int':
                                datas[78]['column' + str(column_index)] = data.int_500_perlbench_r
                                datas[79]['column' + str(column_index)] = data.int_502_gcc_r
                                datas[80]['column' + str(column_index)] = data.int_505_mcf_r
                                datas[81]['column' + str(column_index)] = data.int_520_omnetpp_r
                                datas[82]['column' + str(column_index)] = data.int_523_xalancbmk_r
                                datas[83]['column' + str(column_index)] = data.int_525_x264_r
                                datas[84]['column' + str(column_index)] = data.int_531_deepsjeng_r
                                datas[85]['column' + str(column_index)] = data.int_541_leela_r
                                datas[86]['column' + str(column_index)] = data.int_548_exchange2_r
                                datas[87]['column' + str(column_index)] = data.int_557_xz_r
                                datas[88]['column' + str(column_index)] = data.int_SPECrate2017_int
                            elif data.dtype == 'fp':
                                datas[89]['column' + str(column_index)] = data.fp_503_bwaves_r
                                datas[90]['column' + str(column_index)] = data.fp_507_cactuBSSN_r
                                datas[91]['column' + str(column_index)] = data.fp_508_namd_r
                                datas[92]['column' + str(column_index)] = data.fp_510_parest_r
                                datas[93]['column' + str(column_index)] = data.fp_511_povray_r
                                datas[94]['column' + str(column_index)] = data.fp_519_lbm_r
                                datas[95]['column' + str(column_index)] = data.fp_521_wrf_r
                                datas[96]['column' + str(column_index)] = data.fp_526_blender_r
                                datas[97]['column' + str(column_index)] = data.fp_527_cam4_r
                                datas[98]['column' + str(column_index)] = data.fp_538_imagick_r
                                datas[99]['column' + str(column_index)] = data.fp_544_nab_r
                                datas[100]['column' + str(column_index)] = data.fp_549_fotonik3d_r
                                datas[101]['column' + str(column_index)] = data.fp_554_roms_r
                                datas[102]['column' + str(column_index)] = data.fp_PECrate2017_fp
                column_index += 1
                title_index += 1
            # 基准数据和对比数据的平均数据
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = average_base_single_int_rate_500_perlbench_r
            datas[4]['column' + str(column_index)] = average_base_single_int_rate_502_gcc_r
            datas[5]['column' + str(column_index)] = average_base_single_int_rate_505_mcf_r
            datas[6]['column' + str(column_index)] = average_base_single_int_rate_520_omnetpp_r
            datas[7]['column' + str(column_index)] = average_base_single_int_rate_523_xalancbmk_r
            datas[8]['column' + str(column_index)] = average_base_single_int_rate_525_x264_r
            datas[9]['column' + str(column_index)] = average_base_single_int_rate_531_deepsjeng_r
            datas[10]['column' + str(column_index)] = average_base_single_int_rate_541_leela_r
            datas[11]['column' + str(column_index)] = average_base_single_int_rate_548_exchange2_r
            datas[12]['column' + str(column_index)] = average_base_single_int_rate_557_xz_r
            datas[13]['column' + str(column_index)] = average_base_single_int_rate_SPECrate2017_int
            datas[14]['column' + str(column_index)] = average_base_single_fp_rate_503_bwaves_r
            datas[15]['column' + str(column_index)] = average_base_single_fp_rate_507_cactuBSSN_r
            datas[16]['column' + str(column_index)] = average_base_single_fp_rate_508_namd_r
            datas[17]['column' + str(column_index)] = average_base_single_fp_rate_510_parest_r
            datas[18]['column' + str(column_index)] = average_base_single_fp_rate_511_povray_r
            datas[19]['column' + str(column_index)] = average_base_single_fp_rate_519_lbm_r
            datas[20]['column' + str(column_index)] = average_base_single_fp_rate_521_wrf_r
            datas[21]['column' + str(column_index)] = average_base_single_fp_rate_526_blender_r
            datas[22]['column' + str(column_index)] = average_base_single_fp_rate_527_cam4_r
            datas[23]['column' + str(column_index)] = average_base_single_fp_rate_538_imagick_r
            datas[24]['column' + str(column_index)] = average_base_single_fp_rate_544_nab_r
            datas[25]['column' + str(column_index)] = average_base_single_fp_rate_549_fotonik3d_r
            datas[26]['column' + str(column_index)] = average_base_single_fp_rate_554_roms_r
            datas[27]['column' + str(column_index)] = average_base_single_fp_rate_PECrate2017_fp
            datas[28]['column' + str(column_index)] = average_base_multi_int_rate_500_perlbench_r
            datas[29]['column' + str(column_index)] = average_base_multi_int_rate_502_gcc_r
            datas[30]['column' + str(column_index)] = average_base_multi_int_rate_505_mcf_r
            datas[31]['column' + str(column_index)] = average_base_multi_int_rate_520_omnetpp_r
            datas[32]['column' + str(column_index)] = average_base_multi_int_rate_523_xalancbmk_r
            datas[33]['column' + str(column_index)] = average_base_multi_int_rate_525_x264_r
            datas[34]['column' + str(column_index)] = average_base_multi_int_rate_531_deepsjeng_r
            datas[35]['column' + str(column_index)] = average_base_multi_int_rate_541_leela_r
            datas[36]['column' + str(column_index)] = average_base_multi_int_rate_548_exchange2_r
            datas[37]['column' + str(column_index)] = average_base_multi_int_rate_557_xz_r
            datas[38]['column' + str(column_index)] = average_base_multi_int_rate_SPECrate2017_int
            datas[39]['column' + str(column_index)] = average_base_multi_fp_rate_503_bwaves_r
            datas[40]['column' + str(column_index)] = average_base_multi_fp_rate_507_cactuBSSN_r
            datas[41]['column' + str(column_index)] = average_base_multi_fp_rate_508_namd_r
            datas[42]['column' + str(column_index)] = average_base_multi_fp_rate_510_parest_r
            datas[43]['column' + str(column_index)] = average_base_multi_fp_rate_511_povray_r
            datas[44]['column' + str(column_index)] = average_base_multi_fp_rate_519_lbm_r
            datas[45]['column' + str(column_index)] = average_base_multi_fp_rate_521_wrf_r
            datas[46]['column' + str(column_index)] = average_base_multi_fp_rate_526_blender_r
            datas[47]['column' + str(column_index)] = average_base_multi_fp_rate_527_cam4_r
            datas[48]['column' + str(column_index)] = average_base_multi_fp_rate_538_imagick_r
            datas[49]['column' + str(column_index)] = average_base_multi_fp_rate_544_nab_r
            datas[50]['column' + str(column_index)] = average_base_multi_fp_rate_549_fotonik3d_r
            datas[51]['column' + str(column_index)] = average_base_multi_fp_rate_554_roms_r
            datas[52]['column' + str(column_index)] = average_base_multi_fp_rate_PECrate2017_fp
            datas[53]['column' + str(column_index)] = average_peak_single_int_rate_500_perlbench_r
            datas[54]['column' + str(column_index)] = average_peak_single_int_rate_502_gcc_r
            datas[55]['column' + str(column_index)] = average_peak_single_int_rate_505_mcf_r
            datas[56]['column' + str(column_index)] = average_peak_single_int_rate_520_omnetpp_r
            datas[57]['column' + str(column_index)] = average_peak_single_int_rate_523_xalancbmk_r
            datas[58]['column' + str(column_index)] = average_peak_single_int_rate_525_x264_r
            datas[59]['column' + str(column_index)] = average_peak_single_int_rate_531_deepsjeng_r
            datas[60]['column' + str(column_index)] = average_peak_single_int_rate_541_leela_r
            datas[61]['column' + str(column_index)] = average_peak_single_int_rate_548_exchange2_r
            datas[62]['column' + str(column_index)] = average_peak_single_int_rate_557_xz_r
            datas[63]['column' + str(column_index)] = average_peak_single_int_rate_SPECrate2017_int
            datas[64]['column' + str(column_index)] = average_peak_single_fp_rate_503_bwaves_r
            datas[65]['column' + str(column_index)] = average_peak_single_fp_rate_507_cactuBSSN_r
            datas[66]['column' + str(column_index)] = average_peak_single_fp_rate_508_namd_r
            datas[67]['column' + str(column_index)] = average_peak_single_fp_rate_510_parest_r
            datas[68]['column' + str(column_index)] = average_peak_single_fp_rate_511_povray_r
            datas[69]['column' + str(column_index)] = average_peak_single_fp_rate_519_lbm_r
            datas[70]['column' + str(column_index)] = average_peak_single_fp_rate_521_wrf_r
            datas[71]['column' + str(column_index)] = average_peak_single_fp_rate_526_blender_r
            datas[72]['column' + str(column_index)] = average_peak_single_fp_rate_527_cam4_r
            datas[73]['column' + str(column_index)] = average_peak_single_fp_rate_538_imagick_r
            datas[74]['column' + str(column_index)] = average_peak_single_fp_rate_544_nab_r
            datas[75]['column' + str(column_index)] = average_peak_single_fp_rate_549_fotonik3d_r
            datas[76]['column' + str(column_index)] = average_peak_single_fp_rate_554_roms_r
            datas[77]['column' + str(column_index)] = average_peak_single_fp_rate_PECrate2017_fp
            datas[78]['column' + str(column_index)] = average_peak_multi_int_rate_500_perlbench_r
            datas[79]['column' + str(column_index)] = average_peak_multi_int_rate_502_gcc_r
            datas[80]['column' + str(column_index)] = average_peak_multi_int_rate_505_mcf_r
            datas[81]['column' + str(column_index)] = average_peak_multi_int_rate_520_omnetpp_r
            datas[82]['column' + str(column_index)] = average_peak_multi_int_rate_523_xalancbmk_r
            datas[83]['column' + str(column_index)] = average_peak_multi_int_rate_525_x264_r
            datas[84]['column' + str(column_index)] = average_peak_multi_int_rate_531_deepsjeng_r
            datas[85]['column' + str(column_index)] = average_peak_multi_int_rate_541_leela_r
            datas[86]['column' + str(column_index)] = average_peak_multi_int_rate_548_exchange2_r
            datas[87]['column' + str(column_index)] = average_peak_multi_int_rate_557_xz_r
            datas[88]['column' + str(column_index)] = average_peak_multi_int_rate_SPECrate2017_int
            datas[89]['column' + str(column_index)] = average_peak_multi_fp_rate_503_bwaves_r
            datas[90]['column' + str(column_index)] = average_peak_multi_fp_rate_507_cactuBSSN_r
            datas[91]['column' + str(column_index)] = average_peak_multi_fp_rate_508_namd_r
            datas[92]['column' + str(column_index)] = average_peak_multi_fp_rate_510_parest_r
            datas[93]['column' + str(column_index)] = average_peak_multi_fp_rate_511_povray_r
            datas[94]['column' + str(column_index)] = average_peak_multi_fp_rate_519_lbm_r
            datas[95]['column' + str(column_index)] = average_peak_multi_fp_rate_521_wrf_r
            datas[96]['column' + str(column_index)] = average_peak_multi_fp_rate_526_blender_r
            datas[97]['column' + str(column_index)] = average_peak_multi_fp_rate_527_cam4_r
            datas[98]['column' + str(column_index)] = average_peak_multi_fp_rate_538_imagick_r
            datas[99]['column' + str(column_index)] = average_peak_multi_fp_rate_544_nab_r
            datas[100]['column' + str(column_index)] = average_peak_multi_fp_rate_549_fotonik3d_r
            datas[101]['column' + str(column_index)] = average_peak_multi_fp_rate_554_roms_r
            datas[102]['column' + str(column_index)] = average_peak_multi_fp_rate_PECrate2017_fp
            column_index += 1
            if not base_column_index:
                # 记录基准数据
                base_column_index = column_index - 1
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(103):
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
        base_queryset = Cpu2017.objects.filter(env_id=env_id).all()
        datas = [
            {'column1': 'Cpu2017', 'column2': '', 'column3': '', 'column4': '', 'column5': ''},
            {'column1': '执行命令', 'column2': '', 'column3': '', 'column4': '', 'column5': ''},
            {'column1': '修改参数', 'column2': '', 'column3': '', 'column4': '', 'column5': ''},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '500.perlbench_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '502.gcc_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '505.mcf_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '520.omnetpp_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '523.xalancbmk_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '525.x264_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '531.deepsjeng_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '541.leela_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '548.exchange2_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '557.xz_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': 'SPECrate2017_int'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '503.bwaves_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '507.cactuBSSN_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '508.namd_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '510.parest_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '511.povray_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '519.lbm_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '521.wrf_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '526.blender_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '527.cam4_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '538.imagick_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '544.nab_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '549.fotonik3d_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '554.roms_r'},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': 'SPECrate2017_fp'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '500.perlbench_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '502.gcc_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '505.mcf_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '520.omnetpp_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '523.xalancbmk_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '525.x264_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '531.deepsjeng_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '541.leela_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '548.exchange2_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '557.xz_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': 'SPECrate2017_int'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '503.bwaves_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '507.cactuBSSN_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '508.namd_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '510.parest_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '511.povray_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '519.lbm_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '521.wrf_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '526.blender_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '527.cam4_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '538.imagick_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '544.nab_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '549.fotonik3d_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '554.roms_r'},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': 'SPECrate2017_fp'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '500.perlbench_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '502.gcc_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '505.mcf_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '520.omnetpp_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '523.xalancbmk_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '525.x264_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '531.deepsjeng_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '541.leela_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '548.exchange2_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '557.xz_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': 'SPECrate2017_int'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '503.bwaves_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '507.cactuBSSN_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '508.namd_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '510.parest_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '511.povray_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '519.lbm_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '521.wrf_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '526.blender_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '527.cam4_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '538.imagick_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '544.nab_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '549.fotonik3d_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '554.roms_r'},
            {'column1': 'peak', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': 'SPECrate2017_fp'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '500.perlbench_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '502.gcc_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '505.mcf_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '520.omnetpp_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '523.xalancbmk_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '525.x264_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '531.deepsjeng_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '541.leela_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '548.exchange2_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '557.xz_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': 'SPECrate2017_int'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '503.bwaves_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '507.cactuBSSN_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '508.namd_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '510.parest_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '511.povray_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '519.lbm_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '521.wrf_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '526.blender_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '527.cam4_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '538.imagick_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '544.nab_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '549.fotonik3d_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '554.roms_r'},
            {'column1': 'peak', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': 'SPECrate2017_fp'},
        ]
        title_index = 1
        column_index = 6
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)

        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Cpu2017.objects.filter(env_id=comparativeId).all()
                if not comparsion_queryset:
                    return json_response({}, status.HTTP_200_OK, '列表')
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas, title_index, column_index, base_column_index)
        # print(datas)
        return json_response(datas, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_cpu2017_errors = []
        error_message = []
        for k, cpu2017_json in request.__dict__['data_cpu2017'].items():
            if k.lower().startswith('cpu2017'):
                constants.CPU2017_BOOL = True
                for key, value in cpu2017_json['items'].items():
                    data_cpu2017 = {}
                    data_cpu2017['env_id'] = request.__dict__['data_cpu2017']['env_id']
                    data_cpu2017['thread'] = key.split("_")[0]
                    data_cpu2017['mark_name'] = k[-3:]
                    if key.split("_")[1] == "fp":
                        for key1 in value:
                            data_cpu2017['execute_cmd'] = "xx"
                            data_cpu2017['modify_parameters'] = "xx"
                            data_cpu2017['dtype'] = "fp"
                            data_cpu2017['tuneType'] = key1
                            data_cpu2017['fp_503_bwaves_r'] = value[key1]['503.bwaves_r']
                            data_cpu2017['fp_507_cactuBSSN_r'] = value[key1]['507.cactuBSSN_r']
                            data_cpu2017['fp_508_namd_r'] = value[key1]['508.namd_r']
                            data_cpu2017['fp_510_parest_r'] = value[key1]['510.parest_r']
                            data_cpu2017['fp_511_povray_r'] = value[key1]['511.povray_r']
                            data_cpu2017['fp_519_lbm_r'] = value[key1]['519.lbm_r']
                            data_cpu2017['fp_521_wrf_r'] = value[key1]['521.wrf_r']
                            data_cpu2017['fp_526_blender_r'] = value[key1]['526.blender_r']
                            data_cpu2017['fp_527_cam4_r'] = value[key1]['527.cam4_r']
                            data_cpu2017['fp_538_imagick_r'] = value[key1]['538.imagick_r']
                            data_cpu2017['fp_544_nab_r'] = value[key1]['544.nab_r']
                            data_cpu2017['fp_549_fotonik3d_r'] = value[key1]['549.fotonik3d_r']
                            data_cpu2017['fp_554_roms_r'] = value[key1]['554.roms_r']
                            data_cpu2017['fp_PECrate2017_fp'] = value[key1]['SPECrate2017_fp']
                            data_cpu2017['test_time'] = return_time(cpu2017_json['time'])
                            serializer_cpu2017 = Cpu2017Serializer(data=data_cpu2017)
                            if serializer_cpu2017.is_valid():
                                self.perform_create(serializer_cpu2017)
                            serializer_cpu2017_errors.append(serializer_cpu2017.errors)
                            error_message.append(get_error_message(serializer_cpu2017))
                    elif key.split("_")[1] == "int":
                        for key1 in value:
                            data_cpu2017['execute_cmd'] = "xx"
                            data_cpu2017['modify_parameters'] = "xx"
                            data_cpu2017['dtype'] = "int"
                            data_cpu2017['tuneType'] = key1
                            data_cpu2017['int_500_perlbench_r'] = value[key1]['500.perlbench_r']
                            data_cpu2017['int_502_gcc_r'] = value[key1]['502.gcc_r']
                            data_cpu2017['int_505_mcf_r'] = value[key1]['505.mcf_r']
                            data_cpu2017['int_520_omnetpp_r'] = value[key1]['520.omnetpp_r']
                            data_cpu2017['int_523_xalancbmk_r'] = value[key1]['523.xalancbmk_r']
                            data_cpu2017['int_525_x264_r'] = value[key1]['525.x264_r']
                            data_cpu2017['int_531_deepsjeng_r'] = value[key1]['531.deepsjeng_r']
                            data_cpu2017['int_541_leela_r'] = value[key1]['541.leela_r']
                            data_cpu2017['int_548_exchange2_r'] = value[key1]['548.exchange2_r']
                            data_cpu2017['int_557_xz_r'] = value[key1]['557.xz_r']
                            data_cpu2017['int_SPECrate2017_int'] = value[key1]['SPECrate2017_int']
                            data_cpu2017['test_time'] = return_time(cpu2017_json['time'])
                            data_cpu2017 = {key: value if not isinstance(value, str) or value != '' else None for key, value
                                        in data_cpu2017.items()}
                            serializer_cpu2017 = Cpu2017Serializer(data=data_cpu2017)
                            if serializer_cpu2017.is_valid():
                                self.perform_create(serializer_cpu2017)
                            else:
                                serializer_cpu2017_errors.append(serializer_cpu2017.errors)
                                error_message.append(get_error_message(serializer_cpu2017))
        if serializer_cpu2017_errors:
            return json_response(serializer_cpu2017_errors, status.HTTP_400_BAD_REQUEST,
                             error_message)
        else:
            return
