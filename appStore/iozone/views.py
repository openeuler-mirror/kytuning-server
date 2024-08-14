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

    def get_data(self, serializer_, datas, title_index, column_index, base_column_index):
        serializer = self.get_serializer(serializer_, many=True)
        average_datas = []
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
                average_datas.append(data)

            # 补全column2 = file_size
            if column_index == 2:
                datas[0]['column' + str(column_index)] = '(file size)'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for data in average_datas:
                    if data['testcase_name'] == 'double':
                        datas[3]['column' + str(column_index)] = data['file_size']
                        datas[4]['column' + str(column_index)] = data['file_size']
                        datas[5]['column' + str(column_index)] = data['file_size']
                        datas[6]['column' + str(column_index)] = data['file_size']
                        datas[7]['column' + str(column_index)] = data['file_size']
                        datas[8]['column' + str(column_index)] = data['file_size']
                    elif data['testcase_name'] == 'full':
                        datas[9]['column' + str(column_index)] = data['file_size']
                        datas[10]['column' + str(column_index)] = data['file_size']
                        datas[11]['column' + str(column_index)] = data['file_size']
                        datas[12]['column' + str(column_index)] = data['file_size']
                        datas[13]['column' + str(column_index)] = data['file_size']
                        datas[14]['column' + str(column_index)] = data['file_size']
                    elif data['testcase_name'] == 'half':
                        datas[15]['column' + str(column_index)] = data['file_size']
                        datas[16]['column' + str(column_index)] = data['file_size']
                        datas[17]['column' + str(column_index)] = data['file_size']
                        datas[18]['column' + str(column_index)] = data['file_size']
                        datas[19]['column' + str(column_index)] = data['file_size']
                        datas[20]['column' + str(column_index)] = data['file_size']
                column_index += 1

            # 基准数据和对比数据的全部数据
            datas[0]['column' + str(column_index)] = 'Iozone#' + str(title_index)
            datas[1]['column' + str(column_index)] = serializer.data[0]['execute_cmd']
            datas[2]['column' + str(column_index)] = serializer.data[0]['modify_parameters']
            for data in average_datas:
                if data['testcase_name'] == 'double':
                    # 增加double数据
                    datas[3]['column' + str(column_index)] = data['read_test']
                    datas[4]['column' + str(column_index)] = data['reread_test']
                    datas[5]['column' + str(column_index)] = data['random_read_test']
                    datas[6]['column' + str(column_index)] = data['write_test']
                    datas[7]['column' + str(column_index)] = data['rewrite_test']
                    datas[8]['column' + str(column_index)] = data['random_write_test']
                elif data['testcase_name']== 'full':
                    # 增加full数据
                    datas[9]['column' + str(column_index)] = data['read_test']
                    datas[10]['column' + str(column_index)] = data['reread_test']
                    datas[11]['column' + str(column_index)] = data['random_read_test']
                    datas[12]['column' + str(column_index)] = data['write_test']
                    datas[13]['column' + str(column_index)] = data['rewrite_test']
                    datas[14]['column' + str(column_index)] = data['random_write_test']
                elif data['testcase_name'] == 'half':
                    # 增加half数据
                    datas[15]['column' + str(column_index)] = data['read_test']
                    datas[16]['column' + str(column_index)] = data['reread_test']
                    datas[17]['column' + str(column_index)] = data['random_read_test']
                    datas[18]['column' + str(column_index)] = data['write_test']
                    datas[19]['column' + str(column_index)] = data['rewrite_test']
                    datas[20]['column' + str(column_index)] = data['random_write_test']
            column_index += 1
            title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = ''
            datas[2]['column' + str(column_index)] = ''
            for i in range(21):
                if i > 2:
                    datas[i]['column' + str(column_index)] = datas[i]['column' + str(column_index - 1)]
            column_index += 1
            # 记录基准数据
            if not base_column_index:
                base_column_index = column_index - 1
            # 对比数据的对比值
            else:
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(21):
                    if i > 2:
                        datas[i]['column' + str(column_index)] = \
                            "%.2f%%" % ((datas[i]['column' + str(column_index - 1)] - datas[i]['column' + str(base_column_index)]) / datas[i]['column' + str(base_column_index)] * 100) if datas[i]['column' + str(column_index - 1)] is not None and datas[i]['column' + str(base_column_index)] is not None else None
                column_index += 1
        else:
            # 计算平均值
            test_types = set([d['testcase_name'] for d in serializer.data])
            for test_type in test_types:
                test_type_data_ = serializer_.filter(testcase_name=test_type)
                # 处理half数据，将每个字典转换为NumPy数组
                file_size_list = [d.file_size for d in test_type_data_ if d.file_size is not None]
                write_test_list = [d.write_test for d in test_type_data_ if d.write_test is not None]
                rewrite_test_list = [d.rewrite_test for d in test_type_data_ if d.rewrite_test is not None]
                read_test_list = [d.read_test for d in test_type_data_ if d.read_test is not None]
                reread_test_list = [d.reread_test for d in test_type_data_ if d.reread_test is not None]
                random_read_test_list = [d.random_read_test for d in test_type_data_ if d.random_read_test is not None]
                random_write_test_list = [d.random_write_test for d in test_type_data_ if d.random_write_test is not None]
                # 计算每个数组的平均值
                file_size = np.mean(file_size_list).round(2) if not file_size_list else None
                write_test = np.mean(write_test_list).round(2) if not write_test_list else None
                rewrite_test = np.mean(rewrite_test_list).round(2) if not rewrite_test_list else None
                read_test = np.mean(read_test_list).round(2) if not read_test_list else None
                reread_test = np.mean(reread_test_list).round(2) if not reread_test_list else None
                random_read_test = np.mean(random_read_test_list).round(2) if not random_read_test_list else None
                random_write_test = np.mean(random_write_test_list).round(2) if not random_write_test_list else None

                data = {'testcase_name': test_type,
                        test_type + '_file_size': file_size,
                        'read_test': read_test,
                        'reread_test': reread_test,
                        'random_read_test': random_read_test,
                        'rewrite_test': rewrite_test,
                        'write_test': write_test,
                        'random_write_test': random_write_test, }
                average_datas.append(data)
            # 补全column2 = file_size
            if column_index == 2:
                datas[0]['column' + str(column_index)] = '(file size)'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for data in average_datas:
                    if data['testcase_name'] == 'double':
                        datas[3]['column' + str(column_index)] = data['double_file_size']
                        datas[4]['column' + str(column_index)] = data['double_file_size']
                        datas[5]['column' + str(column_index)] = data['double_file_size']
                        datas[6]['column' + str(column_index)] = data['double_file_size']
                        datas[7]['column' + str(column_index)] = data['double_file_size']
                        datas[8]['column' + str(column_index)] = data['double_file_size']
                    elif data['testcase_name'] == 'full':
                        datas[9]['column' + str(column_index)] = data['full_file_size']
                        datas[10]['column' + str(column_index)] = data['full_file_size']
                        datas[11]['column' + str(column_index)] = data['full_file_size']
                        datas[12]['column' + str(column_index)] = data['full_file_size']
                        datas[13]['column' + str(column_index)] = data['full_file_size']
                        datas[14]['column' + str(column_index)] = data['full_file_size']
                    elif data['testcase_name'] == 'half':
                        datas[15]['column' + str(column_index)] = data['half_file_size']
                        datas[16]['column' + str(column_index)] = data['half_file_size']
                        datas[17]['column' + str(column_index)] = data['half_file_size']
                        datas[18]['column' + str(column_index)] = data['half_file_size']
                        datas[19]['column' + str(column_index)] = data['half_file_size']
                        datas[20]['column' + str(column_index)] = data['half_file_size']
                column_index += 1

            # 基准数据和对比数据的全部数据
            for mark_name in groups:
                temp_mark_datas = serializer_.filter(mark_name=mark_name)
                # 基准数据和对比数据的全部数据
                datas[0]['column' + str(column_index)] = 'unixbench#' + str(title_index)
                datas[1]['column' + str(column_index)] = temp_mark_datas[0].execute_cmd
                datas[2]['column' + str(column_index)] = temp_mark_datas[0].modify_parameters
                for data in temp_mark_datas:
                    if data.testcase_name == 'double':
                        # 增加double数据
                        datas[3]['column' + str(column_index)] = data.read_test
                        datas[4]['column' + str(column_index)] = data.reread_test
                        datas[5]['column' + str(column_index)] = data.random_read_test
                        datas[6]['column' + str(column_index)] = data.write_test
                        datas[7]['column' + str(column_index)] = data.rewrite_test
                        datas[8]['column' + str(column_index)] = data.random_write_test
                    elif data.testcase_name == 'full':
                        # 增加full数据
                        datas[9]['column' + str(column_index)] = data.read_test
                        datas[10]['column' + str(column_index)] = data.reread_test
                        datas[11]['column' + str(column_index)] = data.random_read_test
                        datas[12]['column' + str(column_index)] = data.write_test
                        datas[13]['column' + str(column_index)] = data.rewrite_test
                        datas[14]['column' + str(column_index)] = data.random_write_test
                    elif data.testcase_name == 'half':
                        # 增加half数据
                        datas[15]['column' + str(column_index)] = data.read_test
                        datas[16]['column' + str(column_index)] = data.reread_test
                        datas[17]['column' + str(column_index)] = data.random_read_test
                        datas[18]['column' + str(column_index)] = data.write_test
                        datas[19]['column' + str(column_index)] = data.rewrite_test
                        datas[20]['column' + str(column_index)] = data.random_write_test
                column_index += 1
                title_index += 1
            title = '平均值(基准数据)' if not base_column_index else '平均值'
            # 基准数据和对比数据的平均数据
            datas[0]['column' + str(column_index)] = title
            datas[1]['column' + str(column_index)] = serializer_[0].execute_cmd
            datas[2]['column' + str(column_index)] = serializer_[0].modify_parameters
            # 因为当没有某种数据的时候会出现column为增加的情况，所以需要先初始化一下所有的column为空
            for i in range(3,21):
                datas[i]['column' + str(column_index)] = None
            for data in average_datas:
                if data['testcase_name'] == 'double':
                    # 增加double数据
                    datas[3]['column' + str(column_index)] = data['read_test']
                    datas[4]['column' + str(column_index)] = data['reread_test']
                    datas[5]['column' + str(column_index)] = data['random_read_test']
                    datas[6]['column' + str(column_index)] = data['write_test']
                    datas[7]['column' + str(column_index)] = data['rewrite_test']
                    datas[8]['column' + str(column_index)] = data['random_write_test']
                elif data['testcase_name'] == 'full':
                    # 增加full数据
                    datas[9]['column' + str(column_index)] = data['read_test']
                    datas[10]['column' + str(column_index)] = data['reread_test']
                    datas[11]['column' + str(column_index)] = data['random_read_test']
                    datas[12]['column' + str(column_index)] = data['write_test']
                    datas[13]['column' + str(column_index)] = data['rewrite_test']
                    datas[14]['column' + str(column_index)] = data['random_write_test']
                elif data['testcase_name'] == 'half':
                    # 增加half数据
                    datas[15]['column' + str(column_index)] = data['read_test']
                    datas[16]['column' + str(column_index)] = data['reread_test']
                    datas[17]['column' + str(column_index)] = data['random_read_test']
                    datas[18]['column' + str(column_index)] = data['write_test']
                    datas[19]['column' + str(column_index)] = data['rewrite_test']
                    datas[20]['column' + str(column_index)] = data['random_write_test']
            column_index += 1
            if not base_column_index:
            # 记录基准数据
                base_column_index = column_index - 1
            else:
                # 对比数据的对比值
                datas[0]['column' + str(column_index)] = '对比值'
                datas[1]['column' + str(column_index)] = ''
                datas[2]['column' + str(column_index)] = ''
                for i in range(21):
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
        base_queryset = Iozone.objects.filter(env_id=env_id).all()
        if not base_queryset:
            return json_response({}, status.HTTP_200_OK, '未获取到数据')
        datas = [
            {'column1': 'Iozone', 'column2': ''},
            {'column1': '执行命令', 'column2': ''},
            {'column1': '修改参数', 'column2': ''},
            {'column1': 'double-读测试（KB/s）'},
            {'column1': 'double-重读测试（KB/s）'},
            {'column1': 'double-随机读测试（KB/s）'},
            {'column1': 'double-写测试（KB/s）'},
            {'column1': 'double-重写测试（KB/s）'},
            {'column1': 'double-随机写测试（KB/s）'},
            {'column1': 'full-读测试（KB/s）'},
            {'column1': 'full-重读测试（KB/s）'},
            {'column1': 'full-随机读测试（KB/s）'},
            {'column1': 'full-写测试（KB/s）'},
            {'column1': 'full-重写测试（KB/s）'},
            {'column1': 'full-随机写测试（KB/s）'},
            {'column1': 'half-读测试（KB/s）'},
            {'column1': 'half-重读测试（KB/s）'},
            {'column1': 'half-随机读测试（KB/s）'},
            {'column1': 'half-写测试（KB/s）'},
            {'column1': 'half-重写测试（KB/s）'},
            {'column1': 'half-随机写测试（KB/s）'},
        ]
        title_index = 1
        column_index = 2
        base_column_index = ''
        datas, title_index, column_index, base_column_index = self.get_data(base_queryset, datas, title_index, column_index, base_column_index)
        if comparsionIds != ['']:
            # 处理对比数据
            for comparativeId in comparsionIds:
                comparsion_queryset = Iozone.objects.filter(env_id=comparativeId).all()
                if not comparsion_queryset:
                    return json_response({}, status.HTTP_200_OK, '列表')
                datas, title_index, column_index, base_column_index = self.get_data(comparsion_queryset, datas, title_index, column_index, base_column_index)
        return json_response(datas, status.HTTP_200_OK, '列表')

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
