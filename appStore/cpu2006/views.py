from django.shortcuts import render

# Create your views here.
from rest_framework import status
from appStore.cpu2006.serializers import Cpu2006Serializer
from appStore.utils.common import  json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class Cpu2006ViewSet(CusModelViewSet):
    """
    Cpu2006数据管理
    """
    # queryset = Stream.objects.all().order_by('id')
    serializer_class = Cpu2006Serializer

    def create(self, request, *args, **kwargs):
        serializer_cpu2006_errors = []
        error_message = []
        for k, cpu2006_json in request.__dict__['data_cpu2006'].items():
            # print(k, k.lower().startswith('cpu2006'), 111)
            if k.lower().startswith('cpu2006'):
                # print(cpu2006_json, 222)
                for key, value in cpu2006_json['items'].items():
                    data_cpu2006 = {}
                    data_cpu2006['env_id'] = request.__dict__['data_cpu2006']['env_id']
                    data_cpu2006['thread'] = key.split("_")[0]
                    # print(key.split("_")[0],key,value,"----")
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
                            # print(cpu2006_json,"----------")
                            data_cpu2006['test_time'] = return_time(cpu2006_json['time'])
                            serializer_cpu2006 = Cpu2006Serializer(data=data_cpu2006)
                            # print(data_cpu2006, 333)
                            if serializer_cpu2006.is_valid():
                                # print(data_cpu2006,44444)
                                # self.perform_create(serializer_cpu2006)
                                pass
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
                            # print(data_cpu2006, 333)
                            if serializer_cpu2006.is_valid():
                                # print(data_cpu2006, 44444)
                                pass
                                # self.perform_create(serializer_cpu2006)
                            serializer_cpu2006_errors.append(serializer_cpu2006.errors)
                            error_message.append(get_error_message(serializer_cpu2006))

        return json_response(serializer_cpu2006_errors, status.HTTP_400_BAD_REQUEST,
                             error_message)