import json
from base64 import b64decode

from django.http import JsonResponse, request, HttpRequest
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from appStore.project.models import Project
from appStore.project.serializers import ProjectSerializer
from appStore.utils import constants
from appStore.utils.common import LimsPageSet, json_response, get_error_message, return_time
from appStore.utils.customer_view import CusModelViewSet


class ProjectViewSet(CusModelViewSet):
    """
    project数据管理
    """
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    # pagination_class = LimsPageSet

    def create(self, request, *args, **kwargs):
        data_project = {}
        data_project['env_id'] = request.__dict__['data_project']['env_id']
        data_project['user_name'] = request.__dict__['data_project']['user_name']
        data_project['project_name'] = request.__dict__['data_project']['project_name']
        data_project['arm'] = request.__dict__['data_project']['arm']
        data_project['os_version'] = request.__dict__['data_project']['os_version']
        data_project['hwinfo_machineinfo_serialnumber'] = \
        request.__dict__['data_project']['envinfo']['hwinfo']['machineinfo']['serialnumber']
        # 获取所有文件名对应的key，判断每种测试迭代了几次
        # 对应数据条数默认值为0，遍历、判断这个key的startwith，在取最后一位数+1，与对应数据条数对比，如果大于则替换，
        data_project['cpu2006'] = 0
        data_project['cpu2017'] = 0
        data_project['fio'] = 0
        data_project['iozone'] = 0
        data_project['jvm2008'] = 0
        data_project['lmbench'] = 0
        data_project['stream'] = 0
        data_project['unxibench'] = 0
        for key in request.__dict__['data_project'].keys():
            if key.lower().startswith('cpu2006'):
                data_project['cpu2006'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['cpu2006'] else data_project['cpu2006']
            elif key.lower().startswith('cpu2017'):
                data_project['cpu2017'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['cpu2017'] else data_project['cpu2017']
            elif key.lower().startswith('fio'):
                data_project['fio'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['fio'] else data_project['fio']
            elif key.lower().startswith('iozone'):
                data_project['iozone'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['iozone'] else data_project['iozone']
            elif key.lower().startswith('specjvm'):
                data_project['jvm2008'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['jvm2008'] else data_project['jvm2008']
            elif key.lower().startswith('lmbench'):
                data_project['lmbench'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['lmbench'] else data_project['lmbench']
            elif key.lower().startswith('stream'):
                data_project['stream'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['stream'] else data_project['stream']
            elif key.lower().startswith('unixbench'):
                data_project['unixbench'] = int(key[-1]) + 1 if int(key[-1]) + 1 > data_project['unxibench'] else data_project['unxibench']
        # 查到serialnumber数据的次数后+1
        queryset = Project.objects.filter(
            hwinfo_machineinfo_serialnumber=data_project['hwinfo_machineinfo_serialnumber']).order_by('times').last()
        if not queryset:
            data_project['times'] = 1
        else:
            data_project['times'] = queryset.times + 1
        serializer_project = ProjectSerializer(data=data_project)
        if serializer_project.is_valid():
            # self.perform_create(serializer_project)
            pass
        else:
            print(serializer_project.errors, "project")
            return json_response(serializer_project.errors, status.HTTP_400_BAD_REQUEST,
                                 get_error_message(serializer_project))
