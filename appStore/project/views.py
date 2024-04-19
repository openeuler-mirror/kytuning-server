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
        data_project['cpu2006'] = constants.CPU2006_BOOL
        data_project['cpu2017'] = constants.CPU2017_BOOL
        data_project['fio'] = constants.FIO_BOOL
        data_project['iozone'] = constants.IOZONE_BOOL
        data_project['jvm2008'] = constants.JVM2008_BOOL
        data_project['lmbench'] = constants.LMBENCH_BOOL
        data_project['stream'] = constants.STREAM_BOOL
        data_project['unxibench'] = constants.UNIXBENCH_BOOL
        # 查到serialnumber数据的次数后+1
        queryset = Project.objects.filter(
            hwinfo_machineinfo_serialnumber=data_project['hwinfo_machineinfo_serialnumber']).order_by('times').last()
        if not queryset:
            data_project['times'] = 1
        else:
            data_project['times'] = queryset.times + 1
        serializer_project = ProjectSerializer(data=data_project)
        if serializer_project.is_valid():
            self.perform_create(serializer_project)
        else:
            print(serializer_project.errors, "project")
            return json_response(serializer_project.errors, status.HTTP_400_BAD_REQUEST,
                                 get_error_message(serializer_project))
