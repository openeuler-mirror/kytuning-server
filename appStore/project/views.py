# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from appStore.cpu2006.models import Cpu2006
from appStore.cpu2017.models import Cpu2017
from appStore.env.models import Env
from appStore.fio.models import Fio
from appStore.iozone.models import Iozone
from appStore.jvm2008.models import Jvm2008
from appStore.lmbench.models import Lmbench
from appStore.project.models import Project
from appStore.project.serializers import ProjectSerializer
from appStore.stream.models import Stream
from appStore.unixbench.models import Unixbench
from appStore.users.models import UserProfile
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

    def put(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        project_name = request.data.get('project_name', None)
        message = request.data.get('message', None)
        if not project_name and not id:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递项目id和project_name')
        user_name = Project.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            Project.objects.filter(id=id).update(id=id,project_name=project_name,message=message)
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '该用户不允许修改此数据')
        queryset = Project.objects.filter(id=id)
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '修改project数据完成')

    def delete(self, request):
        id = request.data.get('id', None)
        if not id:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递项目id')
        user_name = Project.objects.filter(id=id).first().user_name
        if request.user.is_superuser or request.user.chinese_name == user_name:
            project_data = Project.objects.filter(id=id).first()
            if not project_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            if project_data.stream:
                Stream.objects.filter(id=project_data.env_id).delete()
            if project_data.unixbench:
                Unixbench.objects.filter(id=project_data.env_id).delete()
            if project_data.lmbench:
                Lmbench.objects.filter(id=project_data.env_id).delete()
            if project_data.fio:
                Fio.objects.filter(id=project_data.env_id).delete()
            if project_data.iozone:
                Iozone.objects.filter(id=project_data.env_id).delete()
            if project_data.jvm2008:
                Jvm2008.objects.filter(id=project_data.env_id).delete()
            if project_data.cpu2006:
                Cpu2006.objects.filter(id=project_data.env_id).delete()
            if project_data.cpu2017:
                Cpu2017.objects.filter(id=project_data.env_id).delete()
            Env.objects.filter(id=project_data.env_id).delete()
            Project.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '此用户不允许删除该数据')

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
        data_project['user_name'] = UserProfile.objects.filter(
            username = request.__dict__['data_project']['user_name']).first().chinese_name
        data_project['os_version'] = request.__dict__['data_project']['envinfo']['swinfo']['os']['osversion']
        data_project['cpu_module_name'] = request.__dict__['data_project']['envinfo']['hwinfo']['cpu']['model_name']
        data_project['ip'] = \
            request.__dict__['data_project']['envinfo']['nwinfo']['nic'][0]['ip']
        # 获取所有文件名对应的key，判断每种测试迭代了几次
        data_project['cpu2006'] = -1
        data_project['cpu2017'] = -1
        data_project['fio'] = -1
        data_project['iozone'] = -1
        data_project['jvm2008'] = -1
        data_project['lmbench'] = -1
        data_project['stream'] = -1
        data_project['unixbench'] = -1
        for key in request.__dict__['data_project'].keys():
            if key.lower().startswith('stream'):
                data_project['stream'] = max(data_project['stream'], int(key.split('-')[-1]))
            elif key.lower().startswith('lmbench'):
                data_project['lmbench'] = max(data_project['lmbench'], int(key.split('-')[-1]))
            elif key.lower().startswith('unixbench'):
                data_project['unixbench'] = max(data_project['unixbench'], int(key.split('-')[-1]))
            elif key.lower().startswith('fio'):
                data_project['fio'] = max(data_project['fio'], int(key.split('-')[-1]))
            elif key.lower().startswith('iozone'):
                data_project['iozone'] = max(data_project['iozone'], int(key.split('-')[-1]))
            elif key.lower().startswith('specjvm'):
                data_project['jvm2008'] = max(data_project['jvm2008'], int(key.split('-')[-1]))
            elif key.lower().startswith('cpu2006'):
                data_project['cpu2006'] = max(data_project['cpu2006'], int(key.split('-')[-1]))
            elif key.lower().startswith('cpu2017'):
                data_project['cpu2017'] = max(data_project['cpu2017'], int(key.split('-')[-1]))
        data_project['cpu2006'] += 1
        data_project['cpu2017'] += 1
        data_project['fio'] += 1
        data_project['iozone'] += 1
        data_project['jvm2008'] += 1
        data_project['lmbench'] += 1
        data_project['stream'] += 1
        data_project['unixbench'] += 1

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
