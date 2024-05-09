import numpy as np

# Create your views here.
from rest_framework import status

from appStore.iozone.models import Iozone
from appStore.iozone.serializers import IozoneSerializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class IozoneViewSet(CusModelViewSet):
    """
    iozone数据管理
    """
    queryset = Iozone.objects.all().order_by('id')
    serializer_class = IozoneSerializer

    def get_data(self,serializer_):
        serializer = self.get_serializer(serializer_, many=True)
        datas = []
        groups = set([d['mark_name'] for d in serializer.data])
        if len(groups) == 1:
            for data in serializer.data:
                data = {'testcase_name': data['testcase_name'],
                        'file_size': data['file_size'],
                        'write_test': data['write_test'],
                        'rewrite_test': data['rewrite_test'],
                        'read_test': data['read_test'],
                        'reread_test': data['reread_test'],
                        'random_read_test': data['random_read_test'],
                        'random_write_test': data['random_write_test'],}
                datas.append(data)
        else:
            test_types = set([d['testcase_name'] for d in serializer.data])
            for test_type in test_types:
                test_type_data_ = serializer_.filter(testcase_name=test_type)
                # 处理half数据，将每个字典转换为NumPy数组
                file_size_list = [d.file_size for d in test_type_data_]
                write_test_list = [d.write_test for d in test_type_data_]
                rewrite_test_list = [d.rewrite_test for d in test_type_data_]
                read_test_list = [d.read_test for d in test_type_data_]
                reread_test_list = [d.reread_test for d in test_type_data_]
                random_read_test_list = [d.random_read_test for d in test_type_data_]
                random_write_test_list = [d.random_write_test for d in test_type_data_]
                # 计算每个数组的平均值
                file_size = np.mean(file_size_list).round(2)
                write_test = np.mean(write_test_list).round(2)
                rewrite_test = np.mean(rewrite_test_list).round(2)
                read_test = np.mean(read_test_list).round(2)
                reread_test = np.mean(reread_test_list).round(2)
                random_read_test = np.mean(random_read_test_list).round(2)
                random_write_test = np.mean(random_write_test_list).round(2)

                data = {'testcase_name': test_type,
                        'file_size': file_size,
                        'write_test': write_test,
                        'rewrite_test': rewrite_test,
                        'read_test': read_test,
                        'reread_test': reread_test,
                        'random_read_test': random_read_test,
                        'random_write_test': random_write_test, }
                datas.append(data)
        return datas

    def do_base_data(self, datas):
        new_data = []
        for value in datas:
            data = [
                {'column1': value['testcase_name'] + '-' + '写测试（KB/s）', 'column2':  value['file_size'], 'column3': value['write_test']},
                {'column1': value['testcase_name'] + '-' + '重写测试（KB/s）', 'column2':  value['file_size'], 'column3': value['rewrite_test']},
                {'column1': value['testcase_name'] + '-' + '读测试（KB/s）', 'column2':  value['file_size'], 'column3': value['read_test']},
                {'column1': value['testcase_name'] + '-' + '重读测试（KB/s）', 'column2':  value['file_size'], 'column3': value['reread_test']},
                {'column1': value['testcase_name'] + '-' + '随机读测试（KB/s）', 'column2':  value['file_size'], 'column3': value['random_read_test']},
                {'column1': value['testcase_name'] + '-' + '随机写测试（KB/s）', 'column2':  value['file_size'], 'column3': value['random_write_test']},
                    ]
            new_data.extend(data)
        return new_data


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
        base_queryset = Iozone.objects.filter(env_id=env_id).all()
        base_serializer = self.get_serializer(base_queryset, many=True)
        if not base_queryset:
            return json_response({}, status.HTTP_200_OK, '未获取到数据')
        base_datas = self.get_data(base_queryset)
        datas = self.do_base_data(base_datas)
        others = [{'column1': 'Iozone', 'column2': '', 'column3': 'Iozone#1 (基准数据)'},
                  {'column1': '执行命令', 'column2': '', 'column3': base_serializer.data[0]['execute_cmd']},
                  {'column1': '修改参数：', 'column2': '', 'column3': base_serializer.data[0]['modify_parameters']}]

        if comparsionIds != ['']:
            # 处理对比数据
            for index, comparativeId in enumerate(comparsionIds):
                new_index = 2 * index + 4
                comparsion_queryset = Iozone.objects.filter(env_id=comparativeId).all()
                comparsion_serializer = self.get_serializer(comparsion_queryset, many=True)
                if not base_queryset:
                    return json_response({}, status.HTTP_200_OK, '未获取到数据')
                comparsion_datas = self.get_data(comparsion_queryset)
                others[0]['column' + str(new_index)] = 'Iozone#'+str(index + 2)
                others[1]['column' + str(new_index)] = comparsion_serializer.data[0]['execute_cmd']
                others[2]['column' + str(new_index)] = comparsion_serializer.data[0]['modify_parameters']
                others[0]['column' + str(new_index + 1)] = ''
                others[1]['column' + str(new_index + 1)] = ''
                others[2]['column' + str(new_index + 1)] = ''

                for value in comparsion_datas:
                    # 判断comparsion_datas数据中的column1字段和datas中的column1字段相同，则在datas中增加值对应值
                    for index2, data_ in enumerate(datas):
                        if data_['column1'].split('-')[0] == value['testcase_name']:
                            # 在datas中增加对比数据
                            datas[index2]['column' + str(new_index)] = value['write_test']
                            datas[index2 + 1]['column' + str(new_index)] = value['rewrite_test']
                            datas[index2 + 2]['column' + str(new_index)] = value['read_test']
                            datas[index2 + 3]['column' + str(new_index)] = value['reread_test']
                            datas[index2 + 4]['column' + str(new_index)] = value['random_read_test']
                            datas[index2 + 5]['column' + str(new_index)] = value['random_write_test']
                            # 在datas中增加计算数据
                            datas[index2]['column' + str(new_index + 1)] = "%.2f%%" % ((datas[index2]['column' + str(new_index)] - datas[index2]['column3']) / datas[index2]['column3'] * 100)
                            datas[index2 + 1]['column' + str(new_index + 1)] = "%.2f%%" % ((datas[index2]['column' + str(new_index)] - datas[index2]['column3']) / datas[index2]['column3'] * 100)
                            datas[index2 + 2]['column' + str(new_index + 1)] = "%.2f%%" % ((datas[index2]['column' + str(new_index)] - datas[index2]['column3']) / datas[index2]['column3'] * 100)
                            datas[index2 + 3]['column' + str(new_index + 1)] = "%.2f%%" % ((datas[index2]['column' + str(new_index)] - datas[index2]['column3']) / datas[index2]['column3'] * 100)
                            datas[index2 + 4]['column' + str(new_index + 1)] = "%.2f%%" % ((datas[index2]['column' + str(new_index)] - datas[index2]['column3']) / datas[index2]['column3'] * 100)
                            datas[index2 + 5]['column' + str(new_index + 1)] = "%.2f%%" % ((datas[index2]['column' + str(new_index)] - datas[index2]['column3']) / datas[index2]['column3'] * 100)
                            break
        iozone_data = {'others': others, 'data': datas}
        return json_response(iozone_data, status.HTTP_200_OK, '列表')

    def create(self, request, *args, **kwargs):
        serializer_iozone_errors = []
        error_message = []
        for k, iozone_json in request.__dict__['data_iozone'].items():
            if k.lower().startswith('iozone'):
                constants.IOZONE_BOOL = True
                data_iozone = {}
                data_iozone['env_id'] = request.__dict__['data_iozone']['env_id']
                data_iozone['execute_cmd'] = "xxx"
                data_iozone['modify_parameters'] = "xxx"
                data_iozone['testcase_name'] = k.split('-')[-3]
                data_iozone['mark_name'] = k[-3:]
                data_iozone['file_size'] = iozone_json['测试记录'][0]['文件大小']
                data_iozone['block_size'] = iozone_json['测试记录'][0]['块大小']
                data_iozone['write_test'] = iozone_json['测试记录'][0]['写测试（KB/s）']
                data_iozone['rewrite_test'] = iozone_json['测试记录'][0]['重写测试（KB/s）']
                data_iozone['read_test'] = iozone_json['测试记录'][0]['读测试（KB/s）']
                data_iozone['reread_test'] = iozone_json['测试记录'][0]['重读测试（KB/s）']
                data_iozone['random_read_test'] = iozone_json['测试记录'][0]['随机读测试（KB/s）']
                data_iozone['random_write_test'] = iozone_json['测试记录'][0]['随机写测试（KB/s）']
                data_iozone['test_time'] = return_time(iozone_json['time'])
                data_iozone = {key: value if not isinstance(value, str) or value != '' else None for key, value in
                                data_iozone.items()}
                serializer_iozone = IozoneSerializer(data=data_iozone)
                if serializer_iozone.is_valid():
                    self.perform_create(serializer_iozone)
                else:
                    return json_response(serializer_iozone.errors, status.HTTP_400_BAD_REQUEST,
                                         get_error_message(serializer_iozone))
        if serializer_iozone_errors:
            print(serializer_iozone_errors, "iozone")
            return json_response(serializer_iozone_errors, status.HTTP_400_BAD_REQUEST, error_message)
        else:
            return
