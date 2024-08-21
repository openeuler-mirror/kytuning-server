# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from appStore.project.models import Project
from appStore.project.serializers import ProjectSerializer
from appStore.utils.common import json_response, get_error_message
from appStore.utils.customer_mixin import CusUpdateModelMixin
from appStore.utils.customer_view import CusModelViewSet, CusUpdateModelViewSet


class ProjectViewSet(CusModelViewSet):
    """
    project数据管理
    """
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        project_queryset = Project.objects.all()
        if not project_queryset:
            return json_response({}, status.HTTP_204_NO_CONTENT, '未查询到project')
        serializer = self.get_serializer(project_queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, 'project数据获取完成')

    def put(self, request):
        id = request.data.get('id', None)
        user_name = request.data.get('user_name', None)
        project_name = request.data.get('project_name', None)
        message = request.data.get('message', None)
        print(id,user_name,project_name,message)
        Project.objects.filter(id=id).update(id=id,user_name=user_name,project_name=project_name,message=message)
        queryset = Project.objects.filter(id=id)
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '修改project数据完成')


    def get_filter_name(self, request, *args, **kwargs):
        project_queryset = Project.objects.all()
        serializer = self.get_serializer(project_queryset, many=True)
        projectNames_ = set([d['project_name'] for d in serializer.data])
        userNames_ = list(set([d['user_name'] for d in serializer.data]))
        osNames_ = list(set([d['os_version'] for d in serializer.data]))
        cpuNames_ = list(set([d['cpu_module_name'] for d in serializer.data]))
        projectNames = [{'text': name, 'value': name} for name in projectNames_]
        userNames = [{'text': name, 'value': name} for name in userNames_]
        osNames = [{'text': name, 'value': name} for name in osNames_]
        cpuNames = [{'text': name, 'value': name} for name in cpuNames_]
        datas = {'projectNames': projectNames, 'userNames': userNames, 'osNames': osNames, 'cpuNames': cpuNames}
        return json_response(datas, status.HTTP_200_OK, '筛选数据获取完成')

    def create(self, request, *args, **kwargs):
        data_project = {}
        data_project['env_id'] = request.__dict__['data_project']['env_id']
        data_project['user_name'] = request.__dict__['data_project']['user_name']
        data_project['project_name'] = request.__dict__['data_project']['project_name']
        data_project['os_version'] = request.__dict__['data_project']['envinfo']['swinfo']['os']['osversion']
        data_project['cpu_module_name'] = request.__dict__['data_project']['envinfo']['hwinfo']['cpu']['model_name']
        data_project['ip'] = \
            request.__dict__['data_project']['envinfo']['nwinfo']['nic'][0]['ip']
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
            ip=data_project['ip']).order_by('times').last()
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
