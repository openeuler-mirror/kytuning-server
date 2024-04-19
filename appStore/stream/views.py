import json

from django.http import JsonResponse, request
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from appStore.stream.models import Stream
from appStore.stream.serializers import StreamSerializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class StreamViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Stream.objects.all().order_by('id')
    serializer_class = StreamSerializer

    def get_data(self, serializer):
        # todo 目前先做project只对应一个stream
        data = {'single_array_size': serializer.data[0]['single_array_size'],
                'single_copy': serializer.data[0]['single_copy'],
                'single_scale': serializer.data[0]['single_scale'],
                'single_add': serializer.data[0]['single_add'],
                'single_triad': serializer.data[0]['single_triad'],
                'multi_array_size': serializer.data[0]['multi_array_size'],
                'multi_copy': serializer.data[0]['multi_copy'],
                'multi_scale': serializer.data[0]['multi_scale'],
                'multi_add': serializer.data[0]['multi_add'],
                'multi_triad': serializer.data[0]['multi_triad'],
                'execute_cmd': serializer.data[0]['execute_cmd'],
                'modify_parameters': serializer.data[0]['modify_parameters']
                }
        return data

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
        base_queryset = Stream.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        base_count = len(base_queryset)
        # 当大于两条数据是展示平均数
        data = self.get_data(base_count, base_serializer)
        others = [{'column1':'Stream','column2':'', 'column3':'Stream#1'},{'column1': '执行命令','column2':'', 'column3': data['execute_cmd']}, {'column1': '修改参数：', 'column2':'', 'column3':data['modify_parameters']}]
        datas = [
            {'column1': '单线程', 'column2': 'Array size', 'column3': data['single_array_size']},
            {'column1': '单线程', 'column2': 'Copy', 'column3': data['single_copy']},
            {'column1': '单线程', 'column2': 'Scale', 'column3': data['single_scale']},
            {'column1': '单线程', 'column2': 'Add', 'column3': data['single_add']},
            {'column1': '单线程', 'column2': 'Triad', 'column3': data['single_triad']},
            {'column1': '多线程', 'column2': 'Array size', 'column3': data['multi_array_size']},
            {'column1': '多线程', 'column2': 'Copy', 'column3': data['multi_copy']},
            {'column1': '多线程', 'column2': 'Scale', 'column3': data['multi_scale']},
            {'column1': '多线程', 'column2': 'Add', 'column3': data['multi_add']},
            {'column1': '多线程', 'column2': 'Triad', 'column3': data['multi_triad']}
            ]

        if comparsionIds != ['']:
            # 处理对比数据
            for index ,comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Stream.objects.filter(env_id=comparativeId).all()
                comparsion_count = len(comparsion_queryset)
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                comparsion_datas = self.get_data(comparsion_count, comparsion_serializer)
                others[0]['column'+str(new_index)] = 'Stream#'+str(index + 2)
                others[1]['column'+str(new_index)] = comparsion_datas['execute_cmd']
                others[2]['column'+str(new_index)] = comparsion_datas['modify_parameters']
                others[0]['column'+str(new_index+1)] = ''
                others[1]['column'+str(new_index+1)] = ''
                others[2]['column'+str(new_index+1)] = ''

                datas[0]['column'+str(new_index)] = comparsion_datas['single_array_size']
                datas[1]['column'+str(new_index)] = comparsion_datas['single_copy']
                datas[2]['column'+str(new_index)] = comparsion_datas['single_scale']
                datas[3]['column'+str(new_index)] = comparsion_datas['single_add']
                datas[4]['column'+str(new_index)] = comparsion_datas['single_triad']
                datas[5]['column'+str(new_index)] = comparsion_datas['multi_array_size']
                datas[6]['column'+str(new_index)] = comparsion_datas['multi_copy']
                datas[7]['column'+str(new_index)] = comparsion_datas['multi_scale']
                datas[8]['column'+str(new_index)] = comparsion_datas['multi_add']
                datas[9]['column'+str(new_index)] = comparsion_datas['multi_triad']

                datas[0]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[0]['column'+str(new_index)] - datas[0]['column3'])/datas[0]['column3'] * 100)
                datas[1]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[1]['column'+str(new_index)] - datas[1]['column3'])/datas[1]['column3'] * 100)
                datas[2]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[2]['column'+str(new_index)] - datas[2]['column3'])/datas[2]['column3'] * 100)
                datas[3]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[3]['column'+str(new_index)] - datas[3]['column3'])/datas[3]['column3'] * 100)
                datas[4]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[4]['column'+str(new_index)] - datas[4]['column3'])/datas[4]['column3'] * 100)
                datas[5]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[5]['column'+str(new_index)] - datas[5]['column3'])/datas[5]['column3'] * 100)
                datas[6]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[6]['column'+str(new_index)] - datas[6]['column3'])/datas[6]['column3'] * 100)
                datas[7]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[7]['column'+str(new_index)] - datas[7]['column3'])/datas[7]['column3'] * 100)
                datas[8]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[8]['column'+str(new_index)] - datas[8]['column3'])/datas[8]['column3'] * 100)
                datas[9]['column'+str(new_index+1)]  = "%.2f%%" % ((datas[9]['column'+str(new_index)] - datas[9]['column3'])/datas[9]['column3'] * 100)

        stream_data = {'others': others, 'data': datas}
        return json_response(stream_data, status.HTTP_200_OK, '列表')


    def create(self, request, *args, **kwargs):
        serializer_stream_errors = []
        error_message = []
        for k, stream_json in request.__dict__['data_stream'].items():
            if k.lower().startswith('stream'):
                constants.STREAM_BOOL = True
                data_stream = {}
                data_stream['env_id'] = request.__dict__['data_stream']['env_id']
                # todo 所有的参数 、 cmd 是在哪里保存的
                data_stream['single_thread'] = '单线程'
                data_stream['multi_threading'] = '多线程'
                data_stream['execute_cmd'] = 'xx'
                data_stream['modify_parameters'] = '参数'
                data_stream['single_array_size'] = stream_json['单线程']['Array size']
                data_stream['single_copy'] = stream_json['单线程']['Copy']
                data_stream['single_scale'] = stream_json['单线程']['Scale']
                data_stream['single_add'] = stream_json['单线程']['Add']
                data_stream['single_triad'] = stream_json['单线程']['Triad']
                data_stream['multi_array_size'] = stream_json['多线程']['Array size']
                data_stream['multi_copy'] = stream_json['多线程']['Copy']
                data_stream['multi_scale'] = stream_json['多线程']['Scale']
                data_stream['multi_add'] = stream_json['多线程']['Add']
                data_stream['multi_triad'] = stream_json['多线程']['Triad']
                data_stream['test_time'] = return_time(stream_json['time'])
                serializer_stream = StreamSerializer(data=data_stream)
                if serializer_stream.is_valid():
                    self.perform_create(serializer_stream)
                serializer_stream_errors.append(serializer_stream.errors)
                error_message.append(get_error_message(serializer_stream))

        if serializer_stream_errors:
            print(serializer_stream_errors, "stream")
            return json_response(serializer_stream_errors, status.HTTP_400_BAD_REQUEST, error_message)
