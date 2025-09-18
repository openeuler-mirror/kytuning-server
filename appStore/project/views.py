"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 09:58:09 2024 +0800
"""
# Create your views here.
from rest_framework import status

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
from appStore.utils.customer_view import CusModelViewSet, CusUpdateModelViewSet


class ProjectViewSet(CusModelViewSet):
    """
    project数据管理
    """
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

    def merge_data(self, request, *args, **kwargs):
        env_id = request.data.get('env_id', None)
        env_ids = request.data.get('env_ids', None)
        # 1、判断是否属于同一个项目等
        base_project = Project.objects.filter(env_id=env_id[0]).first()
        project_names = list(set([d.project_name for d in Project.objects.filter(env_id__in=env_ids)]))
        user_names = list(set([d.user_name for d in Project.objects.filter(env_id__in=env_ids)]))
        os_versions = list(set([d.os_version for d in Project.objects.filter(env_id__in=env_ids)]))
        cpu_module_names = list(set([d.cpu_module_name for d in Project.objects.filter(env_id__in=env_ids)]))
        all_project_names = all(name == base_project.project_name for name in project_names)
        all_user_names = all(name == base_project.user_name for name in user_names)
        all_os_versions = all(name == base_project.os_version for name in os_versions)
        all_cpu_module_names = all(name == base_project.cpu_module_name for name in cpu_module_names)

        if not all([all_project_names, all_user_names, all_os_versions, all_cpu_module_names]):
            return json_response({}, status.HTTP_204_NO_CONTENT, '请确保所有的"项目名称"、"上传人员"、"系统版本"、"cpu型号都相同"')

        # 2、修改数据的env_id和mark_name
        stream_number = 0
        lmbench_number = 0
        unixbench_number = -1
        fio_number = -1
        iozone_number = -1
        jvm2008_number = -1
        cpu2006_number = -1
        cpu2017_number = -1
        # 多数据测试项目，project的表中在直接替换成这个数据
        if Unixbench.objects.filter(env_id=env_id[0]):
            unixbench_mark_name_list = set([d.mark_name for d in Unixbench.objects.filter(env_id=env_id[0])])
            unixbench_number = max(int(string[-1]) for string in unixbench_mark_name_list)

        if Fio.objects.filter(env_id=env_id[0]):
            fio_mark_name_list = set([d.mark_name for d in Fio.objects.filter(env_id=env_id[0])])
            fio_number = max(int(string[-1]) for string in fio_mark_name_list)

        if Iozone.objects.filter(env_id=env_id[0]):
            iozone_mark_name_list = set([d.mark_name for d in Iozone.objects.filter(env_id=env_id[0])])
            iozone_number = max(int(string[-1]) for string in iozone_mark_name_list)

        if Jvm2008.objects.filter(env_id=env_id[0]):
            jvm2008_mark_name_list = set([d.mark_name for d in Jvm2008.objects.filter(env_id=env_id[0])])
            jvm2008_number = max(int(string[-1]) for string in jvm2008_mark_name_list)

        if Cpu2006.objects.filter(env_id=env_id[0]):
            cpu2006_mark_name_list = set([d.mark_name for d in Cpu2006.objects.filter(env_id=env_id[0])])
            cpu2006_number = max(int(string[-1]) for string in cpu2006_mark_name_list)

        if Cpu2017.objects.filter(env_id=env_id[0]):
            cpu2017_mark_name_list = set([d.mark_name for d in Cpu2017.objects.filter(env_id=env_id[0])])
            cpu2017_number = max(int(string[-1]) for string in cpu2017_mark_name_list)

        for id in env_ids:
            if Stream.objects.filter(env_id=id):
                stream_number += len(Stream.objects.filter(env_id=id))
                Stream.objects.filter(env_id=id).update(env_id=env_id[0])
            if Lmbench.objects.filter(env_id=id):
                lmbench_number += len(Lmbench.objects.filter(env_id=id))
                Lmbench.objects.filter(env_id=id).update(env_id=env_id[0])
            max_unixbench_number = 0
            if Unixbench.objects.filter(env_id=id):
                for obj in Unixbench.objects.filter(env_id=id):
                    new_unixbench_number = unixbench_number + (int(obj.mark_name[-1]) + 1)
                    max_unixbench_number = max(max_unixbench_number, new_unixbench_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_unixbench_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    obj.save()
                unixbench_number = max_unixbench_number
            max_fio_number = 0
            if Fio.objects.filter(env_id=id):
                for obj in Fio.objects.filter(env_id=id):
                    new_fio_number = fio_number + (int(obj.mark_name[-1]) + 1)
                    max_fio_number = max(max_fio_number, new_fio_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_fio_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    obj.save()
                fio_number = max_fio_number
            max_iozone_number = 0
            if Iozone.objects.filter(env_id=id):
                for obj in Iozone.objects.filter(env_id=id):
                    new_iozone_number = iozone_number + (int(obj.mark_name[-1]) + 1)
                    max_iozone_number = max(max_iozone_number, new_iozone_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_iozone_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    obj.save()
                iozone_number = max_iozone_number
            max_jvm2008_number = 0
            if Jvm2008.objects.filter(env_id=id):
                for obj in Jvm2008.objects.filter(env_id=id):
                    new_jvm2008_number = jvm2008_number + (int(obj.mark_name[-1]) + 1)
                    max_jvm2008_number = max(max_jvm2008_number, new_jvm2008_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_jvm2008_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    obj.save()
                jvm2008_number = max_jvm2008_number
            max_cpu2006_number = 0
            if Cpu2006.objects.filter(env_id=id):
                for obj in Cpu2006.objects.filter(env_id=id):
                    new_cpu2006_number = cpu2006_number + (int(obj.mark_name[-1]) + 1)
                    max_cpu2006_number = max(max_cpu2006_number, new_cpu2006_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_cpu2006_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    obj.save()
                cpu2006_number = max_cpu2006_number
            max_cpu2017_number = 0
            if Cpu2017.objects.filter(env_id=id):
                for obj in Cpu2017.objects.filter(env_id=id):
                    new_cpu2017_number = cpu2017_number + (int(obj.mark_name[-1]) + 1)
                    max_cpu2017_number = max(max_cpu2017_number, new_cpu2017_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_cpu2017_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    obj.save()
                cpu2017_number = max_cpu2017_number

        # 3、删除env_id的env表，删除env_id对应的project表
        Env.objects.filter(id__in=env_ids).delete()
        Project.objects.filter(env_id__in=env_ids).delete()
        # 4、修改project表对应测试项目的值
        stream_number = Project.objects.filter(env_id=env_id[0]).first().stream + stream_number
        lmbench_number = Project.objects.filter(env_id=env_id[0]).first().lmbench + lmbench_number

        Project.objects.filter(env_id=env_id[0]).update(stream=stream_number, lmbench=lmbench_number,
                                                        unixbench=unixbench_number + 1, fio=fio_number + 1,
                                                        iozone=iozone_number + 1, jvm2008=jvm2008_number + 1,
                                                        cpu2006=cpu2006_number + 1, cpu2017=cpu2017_number + 1)

        return json_response({}, status.HTTP_200_OK, '合并数据成功')

    def create(self, request, *args, **kwargs):
        data_project = {}
        data_project['env_id'] = request.__dict__['data_project']['env_id']
        data_project['project_name'] = request.__dict__['data_project']['project_name']
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

