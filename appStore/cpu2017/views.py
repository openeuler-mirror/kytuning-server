import json

from django.http import JsonResponse, request
from django.shortcuts import render

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

    # def list(self, request, *args, **kwargs):
    #     """
    #     返回列表
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     env_id = request.GET.get('env_id')
    #     queryset = Cpu2017.objects.filter(env_id=env_id).all()
    #     queryset = self.filter_queryset(queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return json_response(serializer.data, status.HTTP_200_OK, '列表')

    def get_data(self, serializer):
        # 初始化数据为空 否则如果下面只获取的单线程或者多线程另外一组获取不到可能会报错
        execute_cmd = serializer.data[0]['execute_cmd']
        modify_parameters = serializer.data[0]['modify_parameters']

        base_single_int_rate_500_perlbench_r = ''
        base_single_int_rate_502_gcc_r = ''
        base_single_int_rate_505_mcf_r = ''
        base_single_int_rate_520_omnetpp_r = ''
        base_single_int_rate_523_xalancbmk_r = ''
        base_single_int_rate_525_x264_r = ''
        base_single_int_rate_531_deepsjeng_r = ''
        base_single_int_rate_541_leela_r = ''
        base_single_int_rate_548_exchange2_r = ''
        base_single_int_rate_557_xz_r = ''
        base_single_int_rate_SPECrate2017_int = ''
        base_single_fp_rate_503_bwaves_r = ''
        base_single_fp_rate_507_cactuBSSN_r = ''
        base_single_fp_rate_508_namd_r = ''
        base_single_fp_rate_510_parest_r = ''
        base_single_fp_rate_511_povray_r = ''
        base_single_fp_rate_519_lbm_r = ''
        base_single_fp_rate_521_wrf_r = ''
        base_single_fp_rate_526_blender_r = ''
        base_single_fp_rate_527_cam4_r = ''
        base_single_fp_rate_538_imagick_r = ''
        base_single_fp_rate_544_nab_r = ''
        base_single_fp_rate_549_fotonik3d_r = ''
        base_single_fp_rate_554_roms_r = ''
        base_single_fp_rate_PECrate2017_fp = ''

        base_multi_int_rate_500_perlbench_r = ''
        base_multi_int_rate_502_gcc_r = ''
        base_multi_int_rate_505_mcf_r = ''
        base_multi_int_rate_520_omnetpp_r = ''
        base_multi_int_rate_523_xalancbmk_r = ''
        base_multi_int_rate_525_x264_r = ''
        base_multi_int_rate_531_deepsjeng_r = ''
        base_multi_int_rate_541_leela_r = ''
        base_multi_int_rate_548_exchange2_r = ''
        base_multi_int_rate_557_xz_r = ''
        base_multi_int_rate_SPECrate2017_int = ''
        base_multi_fp_rate_503_bwaves_r = ''
        base_multi_fp_rate_507_cactuBSSN_r = ''
        base_multi_fp_rate_508_namd_r = ''
        base_multi_fp_rate_510_parest_r = ''
        base_multi_fp_rate_511_povray_r = ''
        base_multi_fp_rate_519_lbm_r = ''
        base_multi_fp_rate_521_wrf_r = ''
        base_multi_fp_rate_526_blender_r = ''
        base_multi_fp_rate_527_cam4_r = ''
        base_multi_fp_rate_538_imagick_r = ''
        base_multi_fp_rate_544_nab_r = ''
        base_multi_fp_rate_549_fotonik3d_r = ''
        base_multi_fp_rate_554_roms_r = ''
        base_multi_fp_rate_PECrate2017_fp = ''

        peak_single_int_rate_500_perlbench_r = ''
        peak_single_int_rate_502_gcc_r = ''
        peak_single_int_rate_505_mcf_r = ''
        peak_single_int_rate_520_omnetpp_r = ''
        peak_single_int_rate_523_xalancbmk_r = ''
        peak_single_int_rate_525_x264_r = ''
        peak_single_int_rate_531_deepsjeng_r = ''
        peak_single_int_rate_541_leela_r = ''
        peak_single_int_rate_548_exchange2_r = ''
        peak_single_int_rate_557_xz_r = ''
        peak_single_int_rate_SPECrate2017_int = ''
        peak_single_fp_rate_503_bwaves_r = ''
        peak_single_fp_rate_507_cactuBSSN_r = ''
        peak_single_fp_rate_508_namd_r = ''
        peak_single_fp_rate_510_parest_r = ''
        peak_single_fp_rate_511_povray_r = ''
        peak_single_fp_rate_519_lbm_r = ''
        peak_single_fp_rate_521_wrf_r = ''
        peak_single_fp_rate_526_blender_r = ''
        peak_single_fp_rate_527_cam4_r = ''
        peak_single_fp_rate_538_imagick_r = ''
        peak_single_fp_rate_544_nab_r = ''
        peak_single_fp_rate_549_fotonik3d_r = ''
        peak_single_fp_rate_554_roms_r = ''
        peak_single_fp_rate_PECrate2017_fp = ''

        peak_multi_int_rate_500_perlbench_r = ''
        peak_multi_int_rate_502_gcc_r = ''
        peak_multi_int_rate_505_mcf_r = ''
        peak_multi_int_rate_520_omnetpp_r = ''
        peak_multi_int_rate_523_xalancbmk_r = ''
        peak_multi_int_rate_525_x264_r = ''
        peak_multi_int_rate_531_deepsjeng_r = ''
        peak_multi_int_rate_541_leela_r = ''
        peak_multi_int_rate_548_exchange2_r = ''
        peak_multi_int_rate_557_xz_r = ''
        peak_multi_int_rate_SPECrate2017_int = ''
        peak_multi_fp_rate_503_bwaves_r = ''
        peak_multi_fp_rate_507_cactuBSSN_r = ''
        peak_multi_fp_rate_508_namd_r = ''
        peak_multi_fp_rate_510_parest_r = ''
        peak_multi_fp_rate_511_povray_r = ''
        peak_multi_fp_rate_519_lbm_r = ''
        peak_multi_fp_rate_521_wrf_r = ''
        peak_multi_fp_rate_526_blender_r = ''
        peak_multi_fp_rate_527_cam4_r = ''
        peak_multi_fp_rate_538_imagick_r = ''
        peak_multi_fp_rate_544_nab_r = ''
        peak_multi_fp_rate_549_fotonik3d_r = ''
        peak_multi_fp_rate_554_roms_r = ''
        peak_multi_fp_rate_PECrate2017_fp = ''

        # thread dtype tuneType
        # 先判断数据的TuneType确定是base还是peak
        # 在判断数据的thread确定是单线程还是多线程
        # 在判断tuneType确定是int还是fp
        for data in serializer.data:
            # 判断数据的TuneType确定是base还是peak
            if data['tuneType'] == 'base':
                if data['thread'] == '单线程':
                    if data['dtype'] == 'int':
                        base_single_int_rate_500_perlbench_r = data['int_500_perlbench_r']
                        base_single_int_rate_502_gcc_r = data['int_502_gcc_r']
                        base_single_int_rate_505_mcf_r = data['int_505_mcf_r']
                        base_single_int_rate_520_omnetpp_r = data['int_520_omnetpp_r']
                        base_single_int_rate_523_xalancbmk_r = data['int_523_xalancbmk_r']
                        base_single_int_rate_525_x264_r = data['int_525_x264_r']
                        base_single_int_rate_531_deepsjeng_r = data['int_531_deepsjeng_r']
                        base_single_int_rate_541_leela_r = data['int_541_leela_r']
                        base_single_int_rate_548_exchange2_r = data['int_548_exchange2_r']
                        base_single_int_rate_557_xz_r = data['int_557_xz_r']
                        base_single_int_rate_SPECrate2017_int = data['int_SPECrate2017_int']
                    elif data['dtype'] == 'fp':
                        base_single_fp_rate_503_bwaves_r = data['fp_503_bwaves_r']
                        base_single_fp_rate_507_cactuBSSN_r = data['fp_507_cactuBSSN_r']
                        base_single_fp_rate_508_namd_r = data['fp_508_namd_r']
                        base_single_fp_rate_510_parest_r = data['fp_510_parest_r']
                        base_single_fp_rate_511_povray_r = data['fp_511_povray_r']
                        base_single_fp_rate_519_lbm_r = data['fp_519_lbm_r']
                        base_single_fp_rate_521_wrf_r = data['fp_521_wrf_r']
                        base_single_fp_rate_526_blender_r = data['fp_526_blender_r']
                        base_single_fp_rate_527_cam4_r = data['fp_527_cam4_r']
                        base_single_fp_rate_538_imagick_r = data['fp_538_imagick_r']
                        base_single_fp_rate_544_nab_r = data['fp_544_nab_r']
                        base_single_fp_rate_549_fotonik3d_r = data['fp_549_fotonik3d_r']
                        base_single_fp_rate_554_roms_r = data['fp_554_roms_r']
                        base_single_fp_rate_PECrate2017_fp = data['fp_PECrate2017_fp']
                elif data['thread'] == '多线程':
                    if data['dtype'] == 'int':
                        base_multi_int_rate_500_perlbench_r = data['int_500_perlbench_r']
                        base_multi_int_rate_502_gcc_r = data['int_502_gcc_r']
                        base_multi_int_rate_505_mcf_r = data['int_505_mcf_r']
                        base_multi_int_rate_520_omnetpp_r = data['int_520_omnetpp_r']
                        base_multi_int_rate_523_xalancbmk_r = data['int_523_xalancbmk_r']
                        base_multi_int_rate_525_x264_r = data['int_525_x264_r']
                        base_multi_int_rate_531_deepsjeng_r = data['int_531_deepsjeng_r']
                        base_multi_int_rate_541_leela_r = data['int_541_leela_r']
                        base_multi_int_rate_548_exchange2_r = data['int_548_exchange2_r']
                        base_multi_int_rate_557_xz_r = data['int_557_xz_r']
                        base_multi_int_rate_SPECrate2017_int = data['int_SPECrate2017_int']
                    elif data['dtype'] == 'fp':
                        base_multi_fp_rate_503_bwaves_r = data['fp_503_bwaves_r']
                        base_multi_fp_rate_507_cactuBSSN_r = data['fp_507_cactuBSSN_r']
                        base_multi_fp_rate_508_namd_r = data['fp_508_namd_r']
                        base_multi_fp_rate_510_parest_r = data['fp_510_parest_r']
                        base_multi_fp_rate_511_povray_r = data['fp_511_povray_r']
                        base_multi_fp_rate_519_lbm_r = data['fp_519_lbm_r']
                        base_multi_fp_rate_521_wrf_r = data['fp_521_wrf_r']
                        base_multi_fp_rate_526_blender_r = data['fp_526_blender_r']
                        base_multi_fp_rate_527_cam4_r = data['fp_527_cam4_r']
                        base_multi_fp_rate_538_imagick_r = data['fp_538_imagick_r']
                        base_multi_fp_rate_544_nab_r = data['fp_544_nab_r']
                        base_multi_fp_rate_549_fotonik3d_r = data['fp_549_fotonik3d_r']
                        base_multi_fp_rate_554_roms_r = data['fp_554_roms_r']
                        base_multi_fp_rate_PECrate2017_fp = data['fp_PECrate2017_fp']
            elif data['tuneType'] == 'peak':
                if data['thread'] == '单线程':
                    if data['dtype'] == 'int':
                        peak_single_int_rate_500_perlbench_r = data['int_500_perlbench_r']
                        peak_single_int_rate_502_gcc_r = data['int_502_gcc_r']
                        peak_single_int_rate_505_mcf_r = data['int_505_mcf_r']
                        peak_single_int_rate_520_omnetpp_r = data['int_520_omnetpp_r']
                        peak_single_int_rate_523_xalancbmk_r = data['int_523_xalancbmk_r']
                        peak_single_int_rate_525_x264_r = data['int_525_x264_r']
                        peak_single_int_rate_531_deepsjeng_r = data['int_531_deepsjeng_r']
                        peak_single_int_rate_541_leela_r = data['int_541_leela_r']
                        peak_single_int_rate_548_exchange2_r = data['int_548_exchange2_r']
                        peak_single_int_rate_557_xz_r = data['int_557_xz_r']
                        peak_single_int_rate_SPECrate2017_int = data['int_SPECrate2017_int']
                    elif data['dtype'] == 'fp':
                        peak_single_fp_rate_503_bwaves_r = data['fp_503_bwaves_r']
                        peak_single_fp_rate_507_cactuBSSN_r = data['fp_507_cactuBSSN_r']
                        peak_single_fp_rate_508_namd_r = data['fp_508_namd_r']
                        peak_single_fp_rate_510_parest_r = data['fp_510_parest_r']
                        peak_single_fp_rate_511_povray_r = data['fp_511_povray_r']
                        peak_single_fp_rate_519_lbm_r = data['fp_519_lbm_r']
                        peak_single_fp_rate_521_wrf_r = data['fp_521_wrf_r']
                        peak_single_fp_rate_526_blender_r = data['fp_526_blender_r']
                        peak_single_fp_rate_527_cam4_r = data['fp_527_cam4_r']
                        peak_single_fp_rate_538_imagick_r = data['fp_538_imagick_r']
                        peak_single_fp_rate_544_nab_r = data['fp_544_nab_r']
                        peak_single_fp_rate_549_fotonik3d_r = data['fp_549_fotonik3d_r']
                        peak_single_fp_rate_554_roms_r = data['fp_554_roms_r']
                        peak_single_fp_rate_PECrate2017_fp = data['fp_PECrate2017_fp']
                elif data['thread'] == '多线程':
                    if data['dtype'] == 'int':
                        peak_multi_int_rate_500_perlbench_r = data['int_500_perlbench_r']
                        peak_multi_int_rate_502_gcc_r = data['int_502_gcc_r']
                        peak_multi_int_rate_505_mcf_r = data['int_505_mcf_r']
                        peak_multi_int_rate_520_omnetpp_r = data['int_520_omnetpp_r']
                        peak_multi_int_rate_523_xalancbmk_r = data['int_523_xalancbmk_r']
                        peak_multi_int_rate_525_x264_r = data['int_525_x264_r']
                        peak_multi_int_rate_531_deepsjeng_r = data['int_531_deepsjeng_r']
                        peak_multi_int_rate_541_leela_r = data['int_541_leela_r']
                        peak_multi_int_rate_548_exchange2_r = data['int_548_exchange2_r']
                        peak_multi_int_rate_557_xz_r = data['int_557_xz_r']
                        peak_multi_int_rate_SPECrate2017_int = data['int_SPECrate2017_int']
                    elif data['dtype'] == 'fp':
                        peak_multi_fp_rate_503_bwaves_r = data['fp_503_bwaves_r']
                        peak_multi_fp_rate_507_cactuBSSN_r = data['fp_507_cactuBSSN_r']
                        peak_multi_fp_rate_508_namd_r = data['fp_508_namd_r']
                        peak_multi_fp_rate_510_parest_r = data['fp_510_parest_r']
                        peak_multi_fp_rate_511_povray_r = data['fp_511_povray_r']
                        peak_multi_fp_rate_519_lbm_r = data['fp_519_lbm_r']
                        peak_multi_fp_rate_521_wrf_r = data['fp_521_wrf_r']
                        peak_multi_fp_rate_526_blender_r = data['fp_526_blender_r']
                        peak_multi_fp_rate_527_cam4_r = data['fp_527_cam4_r']
                        peak_multi_fp_rate_538_imagick_r = data['fp_538_imagick_r']
                        peak_multi_fp_rate_544_nab_r = data['fp_544_nab_r']
                        peak_multi_fp_rate_549_fotonik3d_r = data['fp_549_fotonik3d_r']
                        peak_multi_fp_rate_554_roms_r = data['fp_554_roms_r']
                        peak_multi_fp_rate_PECrate2017_fp = data['fp_PECrate2017_fp']

        new_data = {'execute_cmd': execute_cmd,
                    'modify_parameters': modify_parameters,

                    'base_single_int_rate_500_perlbench_r': base_single_int_rate_500_perlbench_r,
                    'base_single_int_rate_502_gcc_r': base_single_int_rate_502_gcc_r,
                    'base_single_int_rate_505_mcf_r': base_single_int_rate_505_mcf_r,
                    'base_single_int_rate_520_omnetpp_r': base_single_int_rate_520_omnetpp_r,
                    'base_single_int_rate_523_xalancbmk_r': base_single_int_rate_523_xalancbmk_r,
                    'base_single_int_rate_525_x264_r': base_single_int_rate_525_x264_r,
                    'base_single_int_rate_531_deepsjeng_r': base_single_int_rate_531_deepsjeng_r,
                    'base_single_int_rate_541_leela_r': base_single_int_rate_541_leela_r,
                    'base_single_int_rate_548_exchange2_r': base_single_int_rate_548_exchange2_r,
                    'base_single_int_rate_557_xz_r': base_single_int_rate_557_xz_r,
                    'base_single_int_rate_SPECrate2017_int': base_single_int_rate_SPECrate2017_int,
                    'base_single_fp_rate_503_bwaves_r': base_single_fp_rate_503_bwaves_r,
                    'base_single_fp_rate_507_cactuBSSN_r': base_single_fp_rate_507_cactuBSSN_r,
                    'base_single_fp_rate_508_namd_r': base_single_fp_rate_508_namd_r,
                    'base_single_fp_rate_510_parest_r': base_single_fp_rate_510_parest_r,
                    'base_single_fp_rate_511_povray_r': base_single_fp_rate_511_povray_r,
                    'base_single_fp_rate_519_lbm_r': base_single_fp_rate_519_lbm_r,
                    'base_single_fp_rate_521_wrf_r': base_single_fp_rate_521_wrf_r,
                    'base_single_fp_rate_526_blender_r': base_single_fp_rate_526_blender_r,
                    'base_single_fp_rate_527_cam4_r': base_single_fp_rate_527_cam4_r,
                    'base_single_fp_rate_538_imagick_r': base_single_fp_rate_538_imagick_r,
                    'base_single_fp_rate_544_nab_r': base_single_fp_rate_544_nab_r,
                    'base_single_fp_rate_549_fotonik3d_r': base_single_fp_rate_549_fotonik3d_r,
                    'base_single_fp_rate_554_roms_r': base_single_fp_rate_554_roms_r,
                    'base_single_fp_rate_PECrate2017_fp': base_single_fp_rate_PECrate2017_fp,
                    'base_multi_int_rate_500_perlbench_r': base_multi_int_rate_500_perlbench_r,
                    'base_multi_int_rate_502_gcc_r': base_multi_int_rate_502_gcc_r,
                    'base_multi_int_rate_505_mcf_r': base_multi_int_rate_505_mcf_r,
                    'base_multi_int_rate_520_omnetpp_r': base_multi_int_rate_520_omnetpp_r,
                    'base_multi_int_rate_523_xalancbmk_r': base_multi_int_rate_523_xalancbmk_r,
                    'base_multi_int_rate_525_x264_r': base_multi_int_rate_525_x264_r,
                    'base_multi_int_rate_531_deepsjeng_r': base_multi_int_rate_531_deepsjeng_r,
                    'base_multi_int_rate_541_leela_r': base_multi_int_rate_541_leela_r,
                    'base_multi_int_rate_548_exchange2_r': base_multi_int_rate_548_exchange2_r,
                    'base_multi_int_rate_557_xz_r': base_multi_int_rate_557_xz_r,
                    'base_multi_int_rate_SPECrate2017_int': base_multi_int_rate_SPECrate2017_int,
                    'base_multi_fp_rate_503_bwaves_r': base_multi_fp_rate_503_bwaves_r,
                    'base_multi_fp_rate_507_cactuBSSN_r': base_multi_fp_rate_507_cactuBSSN_r,
                    'base_multi_fp_rate_508_namd_r': base_multi_fp_rate_508_namd_r,
                    'base_multi_fp_rate_510_parest_r': base_multi_fp_rate_510_parest_r,
                    'base_multi_fp_rate_511_povray_r': base_multi_fp_rate_511_povray_r,
                    'base_multi_fp_rate_519_lbm_r': base_multi_fp_rate_519_lbm_r,
                    'base_multi_fp_rate_521_wrf_r': base_multi_fp_rate_521_wrf_r,
                    'base_multi_fp_rate_526_blender_r': base_multi_fp_rate_526_blender_r,
                    'base_multi_fp_rate_527_cam4_r': base_multi_fp_rate_527_cam4_r,
                    'base_multi_fp_rate_538_imagick_r': base_multi_fp_rate_538_imagick_r,
                    'base_multi_fp_rate_544_nab_r': base_multi_fp_rate_544_nab_r,
                    'base_multi_fp_rate_549_fotonik3d_r': base_multi_fp_rate_549_fotonik3d_r,
                    'base_multi_fp_rate_554_roms_r': base_multi_fp_rate_554_roms_r,
                    'base_multi_fp_rate_PECrate2017_fp': base_multi_fp_rate_PECrate2017_fp,
                    'peak_single_int_rate_500_perlbench_r': peak_single_int_rate_500_perlbench_r,
                    'peak_single_int_rate_502_gcc_r': peak_single_int_rate_502_gcc_r,
                    'peak_single_int_rate_505_mcf_r': peak_single_int_rate_505_mcf_r,
                    'peak_single_int_rate_520_omnetpp_r': peak_single_int_rate_520_omnetpp_r,
                    'peak_single_int_rate_523_xalancbmk_r': peak_single_int_rate_523_xalancbmk_r,
                    'peak_single_int_rate_525_x264_r': peak_single_int_rate_525_x264_r,
                    'peak_single_int_rate_531_deepsjeng_r': peak_single_int_rate_531_deepsjeng_r,
                    'peak_single_int_rate_541_leela_r': peak_single_int_rate_541_leela_r,
                    'peak_single_int_rate_548_exchange2_r': peak_single_int_rate_548_exchange2_r,
                    'peak_single_int_rate_557_xz_r': peak_single_int_rate_557_xz_r,
                    'peak_single_int_rate_SPECrate2017_int': peak_single_int_rate_SPECrate2017_int,
                    'peak_single_fp_rate_503_bwaves_r': peak_single_fp_rate_503_bwaves_r,
                    'peak_single_fp_rate_507_cactuBSSN_r': peak_single_fp_rate_507_cactuBSSN_r,
                    'peak_single_fp_rate_508_namd_r': peak_single_fp_rate_508_namd_r,
                    'peak_single_fp_rate_510_parest_r': peak_single_fp_rate_510_parest_r,
                    'peak_single_fp_rate_511_povray_r': peak_single_fp_rate_511_povray_r,
                    'peak_single_fp_rate_519_lbm_r': peak_single_fp_rate_519_lbm_r,
                    'peak_single_fp_rate_521_wrf_r': peak_single_fp_rate_521_wrf_r,
                    'peak_single_fp_rate_526_blender_r': peak_single_fp_rate_526_blender_r,
                    'peak_single_fp_rate_527_cam4_r': peak_single_fp_rate_527_cam4_r,
                    'peak_single_fp_rate_538_imagick_r': peak_single_fp_rate_538_imagick_r,
                    'peak_single_fp_rate_544_nab_r': peak_single_fp_rate_544_nab_r,
                    'peak_single_fp_rate_549_fotonik3d_r': peak_single_fp_rate_549_fotonik3d_r,
                    'peak_single_fp_rate_554_roms_r': peak_single_fp_rate_554_roms_r,
                    'peak_single_fp_rate_PECrate2017_fp': peak_single_fp_rate_PECrate2017_fp,
                    'peak_multi_int_rate_500_perlbench_r': peak_multi_int_rate_500_perlbench_r,
                    'peak_multi_int_rate_502_gcc_r': peak_multi_int_rate_502_gcc_r,
                    'peak_multi_int_rate_505_mcf_r': peak_multi_int_rate_505_mcf_r,
                    'peak_multi_int_rate_520_omnetpp_r': peak_multi_int_rate_520_omnetpp_r,
                    'peak_multi_int_rate_523_xalancbmk_r': peak_multi_int_rate_523_xalancbmk_r,
                    'peak_multi_int_rate_525_x264_r': peak_multi_int_rate_525_x264_r,
                    'peak_multi_int_rate_531_deepsjeng_r': peak_multi_int_rate_531_deepsjeng_r,
                    'peak_multi_int_rate_541_leela_r': peak_multi_int_rate_541_leela_r,
                    'peak_multi_int_rate_548_exchange2_r': peak_multi_int_rate_548_exchange2_r,
                    'peak_multi_int_rate_557_xz_r': peak_multi_int_rate_557_xz_r,
                    'peak_multi_int_rate_SPECrate2017_int': peak_multi_int_rate_SPECrate2017_int,
                    'peak_multi_fp_rate_503_bwaves_r': peak_multi_fp_rate_503_bwaves_r,
                    'peak_multi_fp_rate_507_cactuBSSN_r': peak_multi_fp_rate_507_cactuBSSN_r,
                    'peak_multi_fp_rate_508_namd_r': peak_multi_fp_rate_508_namd_r,
                    'peak_multi_fp_rate_510_parest_r': peak_multi_fp_rate_510_parest_r,
                    'peak_multi_fp_rate_511_povray_r': peak_multi_fp_rate_511_povray_r,
                    'peak_multi_fp_rate_519_lbm_r': peak_multi_fp_rate_519_lbm_r,
                    'peak_multi_fp_rate_521_wrf_r': peak_multi_fp_rate_521_wrf_r,
                    'peak_multi_fp_rate_526_blender_r': peak_multi_fp_rate_526_blender_r,
                    'peak_multi_fp_rate_527_cam4_r': peak_multi_fp_rate_527_cam4_r,
                    'peak_multi_fp_rate_538_imagick_r': peak_multi_fp_rate_538_imagick_r,
                    'peak_multi_fp_rate_544_nab_r': peak_multi_fp_rate_544_nab_r,
                    'peak_multi_fp_rate_549_fotonik3d_r': peak_multi_fp_rate_549_fotonik3d_r,
                    'peak_multi_fp_rate_554_roms_r': peak_multi_fp_rate_554_roms_r,
                    'peak_multi_fp_rate_PECrate2017_fp': peak_multi_fp_rate_PECrate2017_fp,
                    }
        return new_data

    def do_base_data(self, data):
        datas = [
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '500.perlbench_r',
             'column6': data['base_single_int_rate_500_perlbench_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '502.gcc_r',
             'column6': data['base_single_int_rate_502_gcc_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '505.mcf_r',
             'column6': data['base_single_int_rate_505_mcf_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '520.omnetpp_r',
             'column6': data['base_single_int_rate_520_omnetpp_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '523.xalancbmk_r',
             'column6': data['base_single_int_rate_523_xalancbmk_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '525.x264_r',
             'column6': data['base_single_int_rate_525_x264_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '531.deepsjeng_r',
             'column6': data['base_single_int_rate_531_deepsjeng_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '541.leela_r',
             'column6': data['base_single_int_rate_541_leela_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '548.exchange2_r',
             'column6': data['base_single_int_rate_548_exchange2_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': '557.xz_r',
             'column6': data['base_single_int_rate_557_xz_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'int', 'column4': 'rate', 'column5': 'SPECrate2017_int',
             'column6': data['base_single_int_rate_SPECrate2017_int']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '503.bwaves_r',
             'column6': data['base_single_fp_rate_503_bwaves_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '507.cactuBSSN_r',
             'column6': data['base_single_fp_rate_507_cactuBSSN_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '508.namd_r',
             'column6': data['base_single_fp_rate_508_namd_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '510.parest_r',
             'column6': data['base_single_fp_rate_510_parest_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '511.povray_r',
             'column6': data['base_single_fp_rate_511_povray_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '519.lbm_r',
             'column6': data['base_single_fp_rate_519_lbm_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '521.wrf_r',
             'column6': data['base_single_fp_rate_521_wrf_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '526.blender_r',
             'column6': data['base_single_fp_rate_526_blender_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '527.cam4_r',
             'column6': data['base_single_fp_rate_527_cam4_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '538.imagick_r',
             'column6': data['base_single_fp_rate_538_imagick_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '544.nab_r',
             'column6': data['base_single_fp_rate_544_nab_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '549.fotonik3d_r',
             'column6': data['base_single_fp_rate_549_fotonik3d_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': '554.roms_r',
             'column6': data['base_single_fp_rate_554_roms_r']},
            {'column1': 'base', 'column2': '单线程', 'column3': 'fp', 'column4': 'rate', 'column5': 'SPECrate2017_fp',
             'column6': data['base_single_fp_rate_PECrate2017_fp']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '500.perlbench_r',
             'column6': data['base_multi_int_rate_500_perlbench_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '502.gcc_r',
             'column6': data['base_multi_int_rate_502_gcc_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '505.mcf_r',
             'column6': data['base_multi_int_rate_505_mcf_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '520.omnetpp_r',
             'column6': data['base_multi_int_rate_520_omnetpp_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '523.xalancbmk_r',
             'column6': data['base_multi_int_rate_523_xalancbmk_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '525.x264_r',
             'column6': data['base_multi_int_rate_525_x264_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '531.deepsjeng_r',
             'column6': data['base_multi_int_rate_531_deepsjeng_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '541.leela_r',
             'column6': data['base_multi_int_rate_541_leela_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '548.exchange2_r',
             'column6': data['base_multi_int_rate_548_exchange2_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': '557.xz_r',
             'column6': data['base_multi_int_rate_557_xz_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'int', 'column4': 'rate', 'column5': 'SPECrate2017_int',
             'column6': data['base_multi_int_rate_SPECrate2017_int']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '503.bwaves_r',
             'column6': data['base_multi_fp_rate_503_bwaves_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '507.cactuBSSN_r',
             'column6': data['base_multi_fp_rate_507_cactuBSSN_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '508.namd_r',
             'column6': data['base_multi_fp_rate_508_namd_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '510.parest_r',
             'column6': data['base_multi_fp_rate_510_parest_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '511.povray_r',
             'column6': data['base_multi_fp_rate_511_povray_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '519.lbm_r',
             'column6': data['base_multi_fp_rate_519_lbm_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '521.wrf_r',
             'column6': data['base_multi_fp_rate_521_wrf_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '526.blender_r',
             'column6': data['base_multi_fp_rate_526_blender_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '527.cam4_r',
             'column6': data['base_multi_fp_rate_527_cam4_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '538.imagick_r',
             'column6': data['base_multi_fp_rate_538_imagick_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '544.nab_r',
             'column6': data['base_multi_fp_rate_544_nab_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '549.fotonik3d_r',
             'column6': data['base_multi_fp_rate_549_fotonik3d_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': '554.roms_r',
             'column6': data['base_multi_fp_rate_554_roms_r']},
            {'column1': 'base', 'column2': '多线程', 'column3': 'fp', 'column4': 'rate', 'column5': 'SPECrate2017_fp',
             'column6': data['base_multi_fp_rate_PECrate2017_fp']},

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
        base_queryset = Cpu2017.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        json_datas = self.get_data(base_serializer)
        base_datas = self.do_base_data(json_datas)
        others = [{'column1': 'Cpu2006', 'column2': '', 'column3': '', 'column4': '', 'column5': '',
                   'column6': 'Cpu2006#1'},
                  {'column1': '执行命令', 'column2': '', 'column3': '', 'column4': '', 'column5': '',
                   'column6': base_serializer.data[0]['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': '', 'column4': '', 'column5': '',
                   'column6': base_serializer.data[0]['modify_parameters']}]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 7
                comparsion_queryset = Cpu2017.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_serializer)

                others[0]['column' + str(new_index)] = 'Cpu2017#' + str(index + 2)
                others[1]['column' + str(new_index)] = comparsion_serializer.data[0]['execute_cmd']
                others[2]['column' + str(new_index)] = comparsion_serializer.data[0]['modify_parameters']

                others[0]['column' + str(new_index + 1)] = ''
                others[1]['column' + str(new_index + 1)] = ''
                others[2]['column' + str(new_index + 1)] = ''

                base_datas[0]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_500_perlbench_r']
                base_datas[1]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_502_gcc_r']
                base_datas[2]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_505_mcf_r']
                base_datas[3]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_520_omnetpp_r']
                base_datas[4]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_523_xalancbmk_r']
                base_datas[5]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_525_x264_r']
                base_datas[6]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_531_deepsjeng_r']
                base_datas[7]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_541_leela_r']
                base_datas[8]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_548_exchange2_r']
                base_datas[9]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_557_xz_r']
                base_datas[10]['column' + str(new_index)] = comparsion_datas['base_single_int_rate_SPECrate2017_int']
                base_datas[11]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_503_bwaves_r']
                base_datas[12]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_507_cactuBSSN_r']
                base_datas[13]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_508_namd_r']
                base_datas[14]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_510_parest_r']
                base_datas[15]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_511_povray_r']
                base_datas[16]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_519_lbm_r']
                base_datas[17]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_521_wrf_r']
                base_datas[18]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_526_blender_r']
                base_datas[19]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_527_cam4_r']
                base_datas[20]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_538_imagick_r']
                base_datas[21]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_544_nab_r']
                base_datas[22]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_549_fotonik3d_r']
                base_datas[23]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_554_roms_r']
                base_datas[24]['column' + str(new_index)] = comparsion_datas['base_single_fp_rate_PECrate2017_fp']
                base_datas[25]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_500_perlbench_r']
                base_datas[26]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_502_gcc_r']
                base_datas[27]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_505_mcf_r']
                base_datas[28]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_520_omnetpp_r']
                base_datas[29]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_523_xalancbmk_r']
                base_datas[30]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_525_x264_r']
                base_datas[31]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_531_deepsjeng_r']
                base_datas[32]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_541_leela_r']
                base_datas[33]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_548_exchange2_r']
                base_datas[34]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_557_xz_r']
                base_datas[35]['column' + str(new_index)] = comparsion_datas['base_multi_int_rate_SPECrate2017_int']
                base_datas[36]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_503_bwaves_r']
                base_datas[37]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_507_cactuBSSN_r']
                base_datas[38]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_508_namd_r']
                base_datas[39]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_510_parest_r']
                base_datas[40]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_511_povray_r']
                base_datas[41]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_519_lbm_r']
                base_datas[42]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_521_wrf_r']
                base_datas[43]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_526_blender_r']
                base_datas[44]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_527_cam4_r']
                base_datas[45]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_538_imagick_r']
                base_datas[46]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_544_nab_r']
                base_datas[47]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_549_fotonik3d_r']
                base_datas[48]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_554_roms_r']
                base_datas[49]['column' + str(new_index)] = comparsion_datas['base_multi_fp_rate_PECrate2017_fp']
                base_datas[50]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_500_perlbench_r']
                base_datas[51]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_502_gcc_r']
                base_datas[52]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_505_mcf_r']
                base_datas[53]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_520_omnetpp_r']
                base_datas[54]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_523_xalancbmk_r']
                base_datas[55]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_525_x264_r']
                base_datas[56]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_531_deepsjeng_r']
                base_datas[57]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_541_leela_r']
                base_datas[58]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_548_exchange2_r']
                base_datas[59]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_557_xz_r']
                base_datas[60]['column' + str(new_index)] = comparsion_datas['peak_single_int_rate_SPECrate2017_int']
                base_datas[61]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_503_bwaves_r']
                base_datas[62]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_507_cactuBSSN_r']
                base_datas[63]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_508_namd_r']
                base_datas[64]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_510_parest_r']
                base_datas[65]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_511_povray_r']
                base_datas[66]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_519_lbm_r']
                base_datas[67]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_521_wrf_r']
                base_datas[68]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_526_blender_r']
                base_datas[69]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_527_cam4_r']
                base_datas[70]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_538_imagick_r']
                base_datas[71]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_544_nab_r']
                base_datas[72]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_549_fotonik3d_r']
                base_datas[73]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_554_roms_r']
                base_datas[74]['column' + str(new_index)] = comparsion_datas['peak_single_fp_rate_PECrate2017_fp']
                base_datas[75]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_500_perlbench_r']
                base_datas[76]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_502_gcc_r']
                base_datas[77]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_505_mcf_r']
                base_datas[78]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_520_omnetpp_r']
                base_datas[79]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_523_xalancbmk_r']
                base_datas[80]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_525_x264_r']
                base_datas[81]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_531_deepsjeng_r']
                base_datas[82]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_541_leela_r']
                base_datas[83]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_548_exchange2_r']
                base_datas[84]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_557_xz_r']
                base_datas[85]['column' + str(new_index)] = comparsion_datas['peak_multi_int_rate_SPECrate2017_int']
                base_datas[86]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_503_bwaves_r']
                base_datas[87]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_507_cactuBSSN_r']
                base_datas[88]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_508_namd_r']
                base_datas[89]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_510_parest_r']
                base_datas[90]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_511_povray_r']
                base_datas[91]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_519_lbm_r']
                base_datas[92]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_521_wrf_r']
                base_datas[93]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_526_blender_r']
                base_datas[94]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_527_cam4_r']
                base_datas[95]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_538_imagick_r']
                base_datas[96]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_544_nab_r']
                base_datas[97]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_549_fotonik3d_r']
                base_datas[98]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_554_roms_r']
                base_datas[99]['column' + str(new_index)] = comparsion_datas['peak_multi_fp_rate_PECrate2017_fp']
                # 在datas中增加计算数据
                base_datas[0]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[0]['column' + str(new_index)] - base_datas[0]['column6']) / base_datas[0][                    'column6'] * 100)
                base_datas[1]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[1]['column' + str(new_index)] - base_datas[1]['column6']) / base_datas[1][                    'column6'] * 100)
                base_datas[2]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[2]['column' + str(new_index)] - base_datas[2]['column6']) / base_datas[2][                    'column6'] * 100)
                base_datas[3]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[3]['column' + str(new_index)] - base_datas[3]['column6']) / base_datas[3][                    'column6'] * 100)
                base_datas[4]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[4]['column' + str(new_index)] - base_datas[4]['column6']) / base_datas[4][                    'column6'] * 100)
                base_datas[5]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[5]['column' + str(new_index)] - base_datas[5]['column6']) / base_datas[5][                    'column6'] * 100)
                base_datas[6]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[6]['column' + str(new_index)] - base_datas[6]['column6']) / base_datas[6][                    'column6'] * 100)
                base_datas[7]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[7]['column' + str(new_index)] - base_datas[7]['column6']) / base_datas[7][                    'column6'] * 100)
                base_datas[8]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[8]['column' + str(new_index)] - base_datas[8]['column6']) / base_datas[8][                    'column6'] * 100)
                base_datas[9]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[9]['column' + str(new_index)] - base_datas[9]['column6']) / base_datas[9][                    'column6'] * 100)
                base_datas[10]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[10]['column' + str(new_index)] - base_datas[10]['column6']) / base_datas[10][                    'column6'] * 100)
                base_datas[11]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[11]['column' + str(new_index)] - base_datas[11]['column6']) / base_datas[11][                    'column6'] * 100)
                base_datas[12]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[12]['column' + str(new_index)] - base_datas[12]['column6']) / base_datas[12][                    'column6'] * 100)
                base_datas[13]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[13]['column' + str(new_index)] - base_datas[13]['column6']) / base_datas[13][                    'column6'] * 100)
                base_datas[14]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[14]['column' + str(new_index)] - base_datas[14]['column6']) / base_datas[14][                    'column6'] * 100)
                base_datas[15]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[15]['column' + str(new_index)] - base_datas[15]['column6']) / base_datas[15][                    'column6'] * 100)
                base_datas[16]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[16]['column' + str(new_index)] - base_datas[16]['column6']) / base_datas[16][                    'column6'] * 100)
                base_datas[17]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[17]['column' + str(new_index)] - base_datas[17]['column6']) / base_datas[17][                    'column6'] * 100)
                base_datas[18]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[18]['column' + str(new_index)] - base_datas[18]['column6']) / base_datas[18][                    'column6'] * 100)
                base_datas[19]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[19]['column' + str(new_index)] - base_datas[19]['column6']) / base_datas[19][                    'column6'] * 100)
                base_datas[20]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[20]['column' + str(new_index)] - base_datas[20]['column6']) / base_datas[20][                    'column6'] * 100)
                base_datas[21]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[21]['column' + str(new_index)] - base_datas[21]['column6']) / base_datas[21][                    'column6'] * 100)
                base_datas[22]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[22]['column' + str(new_index)] - base_datas[22]['column6']) / base_datas[22][                    'column6'] * 100)
                base_datas[23]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[23]['column' + str(new_index)] - base_datas[23]['column6']) / base_datas[23][                    'column6'] * 100)
                base_datas[24]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[24]['column' + str(new_index)] - base_datas[24]['column6']) / base_datas[24][                    'column6'] * 100)
                base_datas[25]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[25]['column' + str(new_index)] - base_datas[25]['column6']) / base_datas[25][                    'column6'] * 100)
                base_datas[26]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[26]['column' + str(new_index)] - base_datas[26]['column6']) / base_datas[26][                    'column6'] * 100)
                base_datas[27]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[27]['column' + str(new_index)] - base_datas[27]['column6']) / base_datas[27][                    'column6'] * 100)
                base_datas[28]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[28]['column' + str(new_index)] - base_datas[28]['column6']) / base_datas[28][                    'column6'] * 100)
                base_datas[29]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[29]['column' + str(new_index)] - base_datas[29]['column6']) / base_datas[29][                    'column6'] * 100)
                base_datas[30]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[30]['column' + str(new_index)] - base_datas[30]['column6']) / base_datas[30][                    'column6'] * 100)
                base_datas[31]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[31]['column' + str(new_index)] - base_datas[31]['column6']) / base_datas[31][                    'column6'] * 100)
                base_datas[32]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[32]['column' + str(new_index)] - base_datas[32]['column6']) / base_datas[32][                    'column6'] * 100)
                base_datas[33]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[33]['column' + str(new_index)] - base_datas[33]['column6']) / base_datas[33][                    'column6'] * 100)
                base_datas[34]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[34]['column' + str(new_index)] - base_datas[34]['column6']) / base_datas[34][                    'column6'] * 100)
                base_datas[35]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[35]['column' + str(new_index)] - base_datas[35]['column6']) / base_datas[35][                    'column6'] * 100)
                base_datas[36]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[36]['column' + str(new_index)] - base_datas[36]['column6']) / base_datas[36][                    'column6'] * 100)
                base_datas[37]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[37]['column' + str(new_index)] - base_datas[37]['column6']) / base_datas[37][                    'column6'] * 100)
                base_datas[38]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[38]['column' + str(new_index)] - base_datas[38]['column6']) / base_datas[38][                    'column6'] * 100)
                base_datas[39]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[39]['column' + str(new_index)] - base_datas[39]['column6']) / base_datas[39][                    'column6'] * 100)
                base_datas[40]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[40]['column' + str(new_index)] - base_datas[40]['column6']) / base_datas[40][                    'column6'] * 100)
                base_datas[41]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[41]['column' + str(new_index)] - base_datas[41]['column6']) / base_datas[41][                    'column6'] * 100)
                base_datas[42]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[42]['column' + str(new_index)] - base_datas[42]['column6']) / base_datas[42][                    'column6'] * 100)
                base_datas[43]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[43]['column' + str(new_index)] - base_datas[43]['column6']) / base_datas[43][                    'column6'] * 100)
                base_datas[44]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[44]['column' + str(new_index)] - base_datas[44]['column6']) / base_datas[44][                    'column6'] * 100)
                base_datas[45]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[45]['column' + str(new_index)] - base_datas[45]['column6']) / base_datas[45][                    'column6'] * 100)
                base_datas[46]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[46]['column' + str(new_index)] - base_datas[46]['column6']) / base_datas[46][                    'column6'] * 100)
                base_datas[47]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[47]['column' + str(new_index)] - base_datas[47]['column6']) / base_datas[47][                    'column6'] * 100)
                base_datas[48]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[48]['column' + str(new_index)] - base_datas[48]['column6']) / base_datas[48][                    'column6'] * 100)
                base_datas[49]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[49]['column' + str(new_index)] - base_datas[49]['column6']) / base_datas[49][                    'column6'] * 100)
                base_datas[50]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[50]['column' + str(new_index)] - base_datas[50]['column6']) / base_datas[50][                    'column6'] * 100)
                base_datas[51]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[51]['column' + str(new_index)] - base_datas[51]['column6']) / base_datas[51][                    'column6'] * 100)
                base_datas[52]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[52]['column' + str(new_index)] - base_datas[52]['column6']) / base_datas[52][                    'column6'] * 100)
                base_datas[53]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[53]['column' + str(new_index)] - base_datas[53]['column6']) / base_datas[53][                    'column6'] * 100)
                base_datas[54]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[54]['column' + str(new_index)] - base_datas[54]['column6']) / base_datas[54][                    'column6'] * 100)
                base_datas[55]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[55]['column' + str(new_index)] - base_datas[55]['column6']) / base_datas[55][                    'column6'] * 100)
                base_datas[56]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[56]['column' + str(new_index)] - base_datas[56]['column6']) / base_datas[56][                    'column6'] * 100)
                base_datas[57]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[57]['column' + str(new_index)] - base_datas[57]['column6']) / base_datas[57][                    'column6'] * 100)
                base_datas[58]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[58]['column' + str(new_index)] - base_datas[58]['column6']) / base_datas[58][                    'column6'] * 100)
                base_datas[59]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[59]['column' + str(new_index)] - base_datas[59]['column6']) / base_datas[59][                    'column6'] * 100)
                base_datas[60]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[60]['column' + str(new_index)] - base_datas[60]['column6']) / base_datas[60][                    'column6'] * 100)
                base_datas[61]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[61]['column' + str(new_index)] - base_datas[61]['column6']) / base_datas[61][                    'column6'] * 100)
                base_datas[62]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[62]['column' + str(new_index)] - base_datas[62]['column6']) / base_datas[62][                    'column6'] * 100)
                base_datas[63]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[63]['column' + str(new_index)] - base_datas[63]['column6']) / base_datas[63][                    'column6'] * 100)
                base_datas[64]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[64]['column' + str(new_index)] - base_datas[64]['column6']) / base_datas[64][                    'column6'] * 100)
                base_datas[65]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[65]['column' + str(new_index)] - base_datas[65]['column6']) / base_datas[65][                    'column6'] * 100)
                base_datas[66]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[66]['column' + str(new_index)] - base_datas[66]['column6']) / base_datas[66][                    'column6'] * 100)
                base_datas[67]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[67]['column' + str(new_index)] - base_datas[67]['column6']) / base_datas[67][                    'column6'] * 100)
                base_datas[68]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[68]['column' + str(new_index)] - base_datas[68]['column6']) / base_datas[68][                    'column6'] * 100)
                base_datas[69]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[69]['column' + str(new_index)] - base_datas[69]['column6']) / base_datas[69][                    'column6'] * 100)
                base_datas[70]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[70]['column' + str(new_index)] - base_datas[70]['column6']) / base_datas[70][                    'column6'] * 100)
                base_datas[71]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[71]['column' + str(new_index)] - base_datas[71]['column6']) / base_datas[71][                    'column6'] * 100)
                base_datas[72]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[72]['column' + str(new_index)] - base_datas[72]['column6']) / base_datas[72][                    'column6'] * 100)
                base_datas[73]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[73]['column' + str(new_index)] - base_datas[73]['column6']) / base_datas[73][                    'column6'] * 100)
                base_datas[74]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[74]['column' + str(new_index)] - base_datas[74]['column6']) / base_datas[74][                    'column6'] * 100)
                base_datas[75]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[75]['column' + str(new_index)] - base_datas[75]['column6']) / base_datas[75][                    'column6'] * 100)
                base_datas[76]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[76]['column' + str(new_index)] - base_datas[76]['column6']) / base_datas[76][                    'column6'] * 100)
                base_datas[77]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[77]['column' + str(new_index)] - base_datas[77]['column6']) / base_datas[77][                    'column6'] * 100)
                base_datas[78]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[78]['column' + str(new_index)] - base_datas[78]['column6']) / base_datas[78][                    'column6'] * 100)
                base_datas[79]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[79]['column' + str(new_index)] - base_datas[79]['column6']) / base_datas[79][                    'column6'] * 100)
                base_datas[80]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[80]['column' + str(new_index)] - base_datas[80]['column6']) / base_datas[80][                    'column6'] * 100)
                base_datas[81]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[81]['column' + str(new_index)] - base_datas[81]['column6']) / base_datas[81][                    'column6'] * 100)
                base_datas[82]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[82]['column' + str(new_index)] - base_datas[82]['column6']) / base_datas[82][                    'column6'] * 100)
                base_datas[83]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[83]['column' + str(new_index)] - base_datas[83]['column6']) / base_datas[83][                    'column6'] * 100)
                base_datas[84]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[84]['column' + str(new_index)] - base_datas[84]['column6']) / base_datas[84][                    'column6'] * 100)
                base_datas[85]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[85]['column' + str(new_index)] - base_datas[85]['column6']) / base_datas[85][                    'column6'] * 100)
                base_datas[86]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[86]['column' + str(new_index)] - base_datas[86]['column6']) / base_datas[86][                    'column6'] * 100)
                base_datas[87]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[87]['column' + str(new_index)] - base_datas[87]['column6']) / base_datas[87][                    'column6'] * 100)
                base_datas[88]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[88]['column' + str(new_index)] - base_datas[88]['column6']) / base_datas[88][                    'column6'] * 100)
                base_datas[89]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[89]['column' + str(new_index)] - base_datas[89]['column6']) / base_datas[89][                    'column6'] * 100)
                base_datas[90]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[90]['column' + str(new_index)] - base_datas[90]['column6']) / base_datas[90][                    'column6'] * 100)
                base_datas[91]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[91]['column' + str(new_index)] - base_datas[91]['column6']) / base_datas[91][                    'column6'] * 100)
                base_datas[92]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[92]['column' + str(new_index)] - base_datas[92]['column6']) / base_datas[92][                    'column6'] * 100)
                base_datas[93]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[93]['column' + str(new_index)] - base_datas[93]['column6']) / base_datas[93][                    'column6'] * 100)
                base_datas[94]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[94]['column' + str(new_index)] - base_datas[94]['column6']) / base_datas[94][                    'column6'] * 100)
                base_datas[95]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[95]['column' + str(new_index)] - base_datas[95]['column6']) / base_datas[95][                    'column6'] * 100)
                base_datas[96]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[96]['column' + str(new_index)] - base_datas[96]['column6']) / base_datas[96][                    'column6'] * 100)
                base_datas[97]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[97]['column' + str(new_index)] - base_datas[97]['column6']) / base_datas[97][                    'column6'] * 100)
                base_datas[98]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[98]['column' + str(new_index)] - base_datas[98]['column6']) / base_datas[98][                    'column6'] * 100)
                base_datas[99]['column' + str(new_index + 1)] = "%.2f%%" % (
                        (base_datas[99]['column' + str(new_index)] - base_datas[99]['column6']) / base_datas[99][                    'column6'] * 100)
        cpu2017_data = {'others': others, 'data': base_datas}
        return json_response(cpu2017_data, status.HTTP_200_OK, '列表')

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
                            serializer_cpu2017 = Cpu2017Serializer(data=data_cpu2017)
                            if serializer_cpu2017.is_valid():
                                # self.perform_create(serializer_cpu2017)
                                pass
                            serializer_cpu2017_errors.append(serializer_cpu2017.errors)
                            error_message.append(get_error_message(serializer_cpu2017))

        return json_response(serializer_cpu2017_errors, status.HTTP_400_BAD_REQUEST,
                             error_message)
