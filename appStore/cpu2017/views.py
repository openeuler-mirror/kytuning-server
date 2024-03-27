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

    def list(self, request, *args, **kwargs):
        """
        返回列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        env_id = request.GET.get('env_id')
        queryset = Cpu2017.objects.filter(env_id=env_id).all()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '列表')


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
