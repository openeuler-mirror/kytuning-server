import numpy as np

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

    def get_data(self, serializer_, datas, title_index, column_index, base_average):
        serializer = self.get_serializer(serializer_, many=True)
        if len(serializer_) == 0:
            # todo 后期做优化考虑怎么未查找到的情况
            pass
        elif len(serializer_) == 1:
            # 基准数据和对比数据的全部数据
            datas[0]['column' + str(column_index)] = 'stream#' + str(title_index)
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            datas[3]['column' + str(column_index)] = serializer.data[0]['single_array_size']
            datas[4]['column' + str(column_index)] = serializer.data[0]['single_copy']
            datas[5]['column' + str(column_index)] = serializer.data[0]['single_scale']
            datas[6]['column' + str(column_index)] = serializer.data[0]['single_add']
            datas[7]['column' + str(column_index)] = serializer.data[0]['single_triad']
            datas[8]['column' + str(column_index)] = serializer.data[0]['multi_array_size']
            datas[9]['column' + str(column_index)] = serializer.data[0]['multi_copy']
            datas[10]['column' + str(column_index)] = serializer.data[0]['multi_scale']
            datas[11]['column' + str(column_index)] = serializer.data[0]['multi_add']
            datas[12]['column' + str(column_index)] = serializer.data[0]['multi_triad']
            column_index += 1
            title_index += 1
            # 基准数据和对比数据的平均数据
            title = '平均值(基准数据)' if not base_average else '平均数据'
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            datas[3]['column' + str(column_index)] = serializer.data[0]['single_array_size']
            datas[4]['column' + str(column_index)] = serializer.data[0]['single_copy']
            datas[5]['column' + str(column_index)] = serializer.data[0]['single_scale']
            datas[6]['column' + str(column_index)] = serializer.data[0]['single_add']
            datas[7]['column' + str(column_index)] = serializer.data[0]['single_triad']
            datas[8]['column' + str(column_index)] = serializer.data[0]['multi_array_size']
            datas[9]['column' + str(column_index)] = serializer.data[0]['multi_copy']
            datas[10]['column' + str(column_index)] = serializer.data[0]['multi_scale']
            datas[11]['column' + str(column_index)] = serializer.data[0]['multi_add']
            datas[12]['column' + str(column_index)] = serializer.data[0]['multi_triad']
            column_index += 1
            title_index += 1
            if not base_average:
                # 记录基准数据
                base_average['single_array_size'] = serializer.data[0]['single_array_size']
                base_average['single_copy'] = serializer.data[0]['single_copy']
                base_average['single_scale'] = serializer.data[0]['single_scale']
                base_average['single_add'] = serializer.data[0]['single_add']
                base_average['single_triad'] = serializer.data[0]['single_triad']
                base_average['multi_array_size'] = serializer.data[0]['multi_array_size']
                base_average['multi_copy'] = serializer.data[0]['multi_copy']
                base_average['multi_scale'] = serializer.data[0]['multi_scale']
                base_average['multi_add'] = serializer.data[0]['multi_add']
                base_average['multi_triad'] = serializer.data[0]['multi_triad']
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                datas[3]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['single_array_size'] - base_average['single_array_size']) /
                            base_average['single_array_size'])
                datas[4]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['single_copy'] - base_average['single_copy']) / base_average[
                        'single_copy'])
                datas[5]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['single_scale'] - base_average['single_scale']) / base_average[
                        'single_scale'])
                datas[6]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['single_add'] - base_average['single_add']) / base_average[
                        'single_add'])
                datas[7]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['single_triad'] - base_average['single_triad']) / base_average[
                        'single_triad'])
                datas[8]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['multi_array_size'] - base_average['multi_array_size']) / base_average[
                        'multi_array_size'])
                datas[9]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['multi_copy'] - base_average['multi_copy']) / base_average[
                        'multi_copy'])
                datas[10]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['multi_scale'] - base_average['multi_scale']) / base_average[
                        'multi_scale'])
                datas[11]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['multi_add'] - base_average['multi_add']) / base_average['multi_add'])
                datas[12]['column' + str(column_index)] = "%.2f%%" % (
                            (serializer.data[0]['multi_triad'] - base_average['multi_triad']) / base_average[
                        'multi_triad'])
                column_index += 1
        else:
            # 计算平均值
            single_array_size_list = [d.single_array_size for d in serializer_]
            single_copy_list = [d.single_copy for d in serializer_]
            single_scale_list = [d.single_scale for d in serializer_]
            single_add_list = [d.single_add for d in serializer_]
            single_triad_list = [d.single_triad for d in serializer_]
            multi_array_size_list = [d.multi_array_size for d in serializer_]
            multi_copy_list = [d.multi_copy for d in serializer_]
            multi_scale_list = [d.multi_scale for d in serializer_]
            multi_add_list = [d.multi_add for d in serializer_]
            multi_triad_list = [d.multi_triad for d in serializer_]

            # 计算每个数组的平均值
            single_array_size = np.mean(single_array_size_list).round(2)
            single_copy = np.mean(single_copy_list).round(2)
            single_scale = np.mean(single_scale_list).round(2)
            single_add = np.mean(single_add_list).round(2)
            single_triad = np.mean(single_triad_list).round(2)
            multi_array_size = np.mean(multi_array_size_list).round(2)
            multi_copy = np.mean(multi_copy_list).round(2)
            multi_scale = np.mean(multi_scale_list).round(2)
            multi_add = np.mean(multi_add_list).round(2)
            multi_triad = np.mean(multi_triad_list).round(2)

            # 基准数据和对比数据的全部数据
            for data in serializer_:
                datas[0]['column' + str(column_index)] = 'stream#' + str(title_index)
                datas[1]['column' + str(column_index)] = data.execute_cmd
                datas[2]['column' + str(column_index)] = data.modify_parameters
                datas[3]['column' + str(column_index)] = data.single_array_size
                datas[4]['column' + str(column_index)] = data.single_copy
                datas[5]['column' + str(column_index)] = data.single_scale
                datas[6]['column' + str(column_index)] = data.single_add
                datas[7]['column' + str(column_index)] = data.single_triad
                datas[8]['column' + str(column_index)] = data.multi_array_size
                datas[9]['column' + str(column_index)] = data.multi_copy
                datas[10]['column' + str(column_index)] = data.multi_scale
                datas[11]['column' + str(column_index)] = data.multi_add
                datas[12]['column' + str(column_index)] = data.multi_triad
                column_index += 1
                title_index += 1
            title = '平均值(基准数据)' if not base_average else '平均数据'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            datas[3]['column' + str(column_index)] = single_array_size
            datas[4]['column' + str(column_index)] = single_copy
            datas[5]['column' + str(column_index)] = single_scale
            datas[6]['column' + str(column_index)] = single_add
            datas[7]['column' + str(column_index)] = single_triad
            datas[8]['column' + str(column_index)] = multi_array_size
            datas[9]['column' + str(column_index)] = multi_copy
            datas[10]['column' + str(column_index)] = multi_scale
            datas[11]['column' + str(column_index)] = multi_add
            datas[12]['column' + str(column_index)] = multi_triad
            column_index += 1
            if not base_average:
                # 记录基准数据
                base_average['single_array_size'] = single_array_size
                base_average['single_copy'] = single_copy
                base_average['single_scale'] = single_scale
                base_average['single_add'] = single_add
                base_average['single_triad'] = single_triad
                base_average['multi_array_size'] = multi_array_size
                base_average['multi_copy'] = multi_copy
                base_average['multi_scale'] = multi_scale
                base_average['multi_add'] = multi_add
                base_average['multi_triad'] = multi_triad
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                datas[3]['column' + str(column_index)] = "%.2f%%" % ((single_array_size - base_average['single_array_size']) / base_average['single_array_size'])
                datas[4]['column' + str(column_index)] = "%.2f%%" % ((single_copy - base_average['single_copy']) / base_average['single_copy'])
                datas[5]['column' + str(column_index)] = "%.2f%%" % ((single_scale - base_average['single_scale']) / base_average['single_scale'])
                datas[6]['column' + str(column_index)] = "%.2f%%" % ((single_add - base_average['single_add']) / base_average['single_add'])
                datas[7]['column' + str(column_index)] = "%.2f%%" % ((single_triad - base_average['single_triad']) / base_average['single_triad'])
                datas[8]['column' + str(column_index)] = "%.2f%%" % ((multi_array_size - base_average['multi_array_size']) / base_average['multi_array_size'])
                datas[9]['column' + str(column_index)] = "%.2f%%" % ((multi_copy - base_average['multi_copy']) / base_average['multi_copy'])
                datas[10]['column' + str(column_index)] = "%.2f%%" % ((multi_scale - base_average['multi_scale']) / base_average['multi_scale'])
                datas[11]['column' + str(column_index)] = "%.2f%%" % ((multi_add - base_average['multi_add']) / base_average['multi_add'])
                datas[12]['column' + str(column_index)] = "%.2f%%" % ((multi_triad - base_average['multi_triad']) / base_average['multi_triad'])
                column_index += 1

        return datas, title_index, column_index

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
        if not base_queryset:
            return json_response({}, status.HTTP_200_OK, '列表')
        datas = [{'column1': 'Stream', 'column2': ''}, {'column1': '执行命令', 'column2': ''},
                 {'column1': '修改参数：', 'column2': ''}, {'column1': '单线程', 'column2': 'Array size'},
                 {'column1': '单线程', 'column2': 'Copy'}, {'column1': '单线程', 'column2': 'Scale'},
                 {'column1': '单线程', 'column2': 'Add'}, {'column1': '单线程', 'column2': 'Triad'},
                 {'column1': '多线程', 'column2': 'Array size'}, {'column1': '多线程', 'column2': 'Copy'},
                 {'column1': '多线程', 'column2': 'Scale'}, {'column1': '多线程', 'column2': 'Add'},
                 {'column1': '多线程', 'column2': 'Triad'}, ]
        title_index = 1
        column_index = 3
        base_average = {}
        datas, title_index, column_index = self.get_data(base_queryset, datas, title_index, column_index, base_average)
        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Stream.objects.filter(env_id=comparativeId).all()
                if not comparsion_queryset:
                    return json_response({}, status.HTTP_200_OK, '列表')
                datas, title_index, column_index = self.get_data(comparsion_queryset, datas, title_index, column_index, base_average)
        return json_response(datas, status.HTTP_200_OK, '列表')

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
                data_stream = {key: value if not isinstance(value, str) or value != '' else None for key, value in
                               data_stream.items()}
                serializer_stream = StreamSerializer(data=data_stream)
                if serializer_stream.is_valid():
                    self.perform_create(serializer_stream)
                else:
                    serializer_stream_errors.append(serializer_stream.errors)
                    error_message.append(get_error_message(serializer_stream))

        if serializer_stream_errors:
            print(serializer_stream_errors, "stream")
            return json_response(serializer_stream_errors, status.HTTP_400_BAD_REQUEST, error_message)
        else:
            return
