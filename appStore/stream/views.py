# Create your views here.
from rest_framework import status
from appStore.stream.models import Stream
from appStore.stream.serializers import StreamSerializer
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class StreamViewSet(CusModelViewSet):
    """
    stream数据管理
    """
    queryset = Stream.objects.all().order_by('id')
    serializer_class = StreamSerializer

    def create(self, request, *args, **kwargs):
        serializer_stream_errors = []
        error_message = []
        for k, stream_json in request.__dict__['data_stream'].items():
            if k.lower().startswith('stream'):
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
                    pass
                    # todo 放开
                    # self.perform_create(serializer_stream)
                print(serializer_stream.errors,"stream")
                serializer_stream_errors.append(serializer_stream.errors)
                error_message.append(get_error_message(serializer_stream))

        if serializer_stream_errors:
            print(serializer_stream_errors, "stream")
            return json_response(serializer_stream_errors, status.HTTP_400_BAD_REQUEST, error_message)
