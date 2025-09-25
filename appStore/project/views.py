"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 09:58:09 2024 +0800
"""
# Create your views here.
import os
import json
import logging

from django.http import FileResponse, HttpResponse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from djangoProject import settings
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
from appStore.utils.customer_view import CusModelViewSet

from appStore.utils.export_excel import stream_excel, cpu2017_excel, cpu2006_excel, jvm2008_excel, iozone_excel, \
    fio_excel, unixbench_excel, lmbench_excel, env_excel

log = logging.getLogger('mydjango') #这里的mydjango是settings中loggers里面对应的名字

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
        baseId = request.GET.get('baseId',None)
        comparsionIds = request.GET.get('comparsionIds',None)
        if comparsionIds:
            baseId = baseId + ',' + comparsionIds
        if baseId:
            project_queryset = Project.objects.filter(env_id__in=(baseId.split(',')))
        else:
            project_queryset = Project.objects.all().order_by("-id")
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
        user_name = Project.objects.filter(id=env_id[0]).first().user_name
        if not (request.user.is_superuser or request.user.chinese_name == user_name):
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只能合并自己管理的数据')

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
                log.info('处理的stream的id是 %d，把stream_env = %d 改为 %d ,', Stream.objects.filter(env_id=id).first().id, id, env_id[0])
                Stream.objects.filter(env_id=id).update(env_id=env_id[0])
            if Lmbench.objects.filter(env_id=id):
                log.info('处理的lmbench的id是 %d，把lmbench_env = %d 改为 %d ,', Lmbench.objects.filter(env_id=id).first().id, id, env_id[0])
                Lmbench.objects.filter(env_id=id).update(env_id=env_id[0])
            max_unixbench_number = 0
            if Unixbench.objects.filter(env_id=id):
                for obj in Unixbench.objects.filter(env_id=id):
                    new_unixbench_number = unixbench_number + (int(obj.mark_name[-1]) + 1)
                    max_unixbench_number = max(max_unixbench_number, new_unixbench_number)
                    new_mark_name = obj.mark_name[:-1] + str(new_unixbench_number)
                    obj.env_id = env_id[0]
                    obj.mark_name = new_mark_name
                    log.info('处理的unixbench的id是 %d，把unixbench_env = %d 改为 %d ,', obj.id, id, env_id[0])
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
                    log.info('处理的fio的id是 %d，把fio_env = %d 改为 %d ,', obj.id, id, env_id[0])
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
                    log.info('处理的iozone的id是 %d，把iozone_env = %d 改为 %d ,', obj.id, id, env_id[0])
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
                    log.info('处理的jvm2008的id是 %d，把jvm2008_env = %d 改为 %d ,', obj.id, id, env_id[0])
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
                    log.info('处理的cpu2006的id是 %d，把cpu2006_env = %d 改为 %d ,', obj.id, id, env_id[0])
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
                    log.info('处理的cpu2017的id是 %d，把cpu2017_env = %d 改为 %d ,', obj.id, id, env_id[0])
                    obj.save()
                cpu2017_number = max_cpu2017_number


        # 3、合并all_json_data文件
        json_file_path = '/var/www/html/all_json_data_file/'
        # 找到需要合并的全部数据
        base_env_time = Env.objects.filter(id=env_id[0]).first().time
        compar_env_times = list(set([d.time for d in Env.objects.filter(id__in=env_ids)]))

        if os.path.exists(json_file_path + base_env_time+'.json'):
            stream_max_number = -1
            unixbench_max_number = -1
            fio_max_number = -1
            iozone_max_number = -1
            jvm2008_max_number = -1
            cpu2006_max_number = -1
            cpu2017_max_number = -1
            data_ = None
            base_lmbench_keys = 'lmbench'
            with open(json_file_path + base_env_time+'.json', 'r') as f:
                json_data = f.read()
                # 将 JSON 字符串解析为 Python 对象
                base_file_data = json.loads(json_data)
                # 获取base数据的lmbench最后一位的key
                if [key for key in base_file_data.keys() if key.startswith('lmbench')]:
                    base_lmbench_keys = sorted([key for key in base_file_data.keys() if key.startswith('lmbench')])[-1]
                data_ = base_file_data.copy()
                stream_keys_number = []
                unixbench_keys_number = []
                fio_keys_number = []
                iozone_keys_number = []
                jvm2008_keys_number = []
                cpu2006_keys_number = []
                cpu2017_keys_number = []
                for key in base_file_data.keys():
                    if key.startswith('stream'):
                        stream_keys_number.append(int(key.split('-')[-1]))
                    elif key.startswith('Unixbench'):
                       unixbench_keys_number.append(int(key.split('-')[-1]))
                    elif key.startswith('fio'):
                       fio_keys_number.append(int(key.split('-')[-1]))
                    elif key.startswith('iozone'):
                       iozone_keys_number.append(int(key.split('-')[-1]))
                    elif key.startswith('specjvm'):
                        jvm2008_keys_number.append(int(key.split('-')[-1]))
                    elif key.startswith('cpu2006'):
                       cpu2006_keys_number.append(int(key.split('-')[-1]))
                    elif key.startswith('cpu2017'):
                       cpu2017_keys_number.append(int(key.split('-')[-1]))

                stream_max_number = max(stream_keys_number) if stream_keys_number else stream_max_number
                unixbench_max_number = max(unixbench_keys_number) if unixbench_keys_number else unixbench_max_number
                fio_max_number = max(fio_keys_number) if fio_keys_number else fio_max_number
                iozone_max_number = max(iozone_keys_number) if iozone_keys_number else iozone_max_number
                jvm2008_max_number = max(jvm2008_keys_number) if jvm2008_keys_number else jvm2008_max_number
                cpu2006_max_number = max(cpu2006_keys_number) if cpu2006_keys_number else cpu2006_max_number
                cpu2017_max_number = max(cpu2017_keys_number) if cpu2017_keys_number else cpu2017_max_number

            for file_name in compar_env_times:
                if os.path.exists(json_file_path + file_name + '.json'):
                    with open(json_file_path + file_name + '.json', 'r') as f:
                        json_data = f.read()
                        # 将 JSON 字符串解析为 Python 对象
                        compar_file_data = json.loads(json_data)
                        # 因为lmbench的数据存储格式不通单独处理lmbench。lmbench的最后一组数据中有全部的数据
                        lmbench_keys = 'lmbench'
                        if [key for key in compar_file_data.keys() if key.startswith('lmbench')]:
                            lmbench_keys = sorted([key for key in compar_file_data.keys() if key.startswith('lmbench')])[-1]
                        for key,value in compar_file_data.items():
                            if key.startswith('stream'):
                                data_['stream-5.9-1-null-0-'+str(int(key.split('-')[-1]) + stream_max_number + 1)] = value
                            elif key == lmbench_keys:
                                # 因为lmbench的测试段数据存储是会保存上一条的测试数据，所以特殊处理。
                                if base_lmbench_keys == 'lmbench':
                                    data_[lmbench_keys] = value
                                else:
                                    data_[base_lmbench_keys]['items'].extend(value['items'])
                            elif key.startswith('Unixbench'):
                                data_[key[:-int(len(key.split('-')[-1]))] + str(int(key[-int(len(key.split('-')[-1]))]) + unixbench_max_number + 1)] = value
                            elif key.startswith('fio'):
                                data_[key[:-int(len(key.split('-')[-1]))] + str(int(key[-int(len(key.split('-')[-1]))]) + fio_max_number + 1)] = value
                            elif key.startswith('iozone'):
                                data_[key[:-int(len(key.split('-')[-1]))] + str(int(key[-int(len(key.split('-')[-1]))]) + iozone_max_number + 1)] = value
                            elif key.startswith('specjvm'):
                                data_[key[:-int(len(key.split('-')[-1]))] + str(int(key[-int(len(key.split('-')[-1]))]) + jvm2008_max_number + 1)] = value
                            elif key.startswith('cpu2006'):
                                data_[key[:-int(len(key.split('-')[-1]))] + str(int(key[-int(len(key.split('-')[-1]))]) + cpu2006_max_number + 1)] = value
                            elif key.startswith('cpu2017'):
                                data_[key[:-int(len(key.split('-')[-1]))] + str(int(key[-int(len(key.split('-')[-1]))]) + cpu2006_max_number + 1)] = value
                        compar_stream_keys = []
                        compar_unixbench_keys = []
                        compar_fio_keys = []
                        compar_iozone_keys = []
                        compar_jvm2008_keys = []
                        compar_cpu2006_keys = []
                        compar_cpu2017_keys = []
                        for key in compar_file_data.keys():
                            if key.startswith('stream'):
                                compar_stream_keys.append(int(key.split('-')[-1]))
                            elif key.startswith('Unixbench'):
                                compar_unixbench_keys.append(int(key.split('-')[-1]))
                            elif key.startswith('fio'):
                                compar_fio_keys.append(int(key.split('-')[-1]))
                            elif key.startswith('iozone'):
                                compar_iozone_keys.append(int(key.split('-')[-1]))
                            elif key.startswith('specjvm'):
                                compar_jvm2008_keys.append(int(key.split('-')[-1]))
                            elif key.startswith('cpu2006'):
                                compar_cpu2006_keys.append(int(key.split('-')[-1]))
                            elif key.startswith('cpu2017'):
                                compar_cpu2017_keys.append(int(key.split('-')[-1]))
                        stream_max_number = stream_max_number + max(compar_stream_keys) + 1 if compar_stream_keys else stream_max_number
                        unixbench_max_number = unixbench_max_number + max(compar_unixbench_keys) + 1 if compar_unixbench_keys else unixbench_max_number
                        fio_max_number = fio_max_number + max(compar_fio_keys) + 1 if compar_fio_keys else fio_max_number
                        iozone_max_number = iozone_max_number + max(compar_iozone_keys) + 1 if compar_iozone_keys else iozone_max_number
                        jvm2008_max_number = jvm2008_max_number + max(compar_jvm2008_keys) + 1 if compar_jvm2008_keys else jvm2008_max_number
                        cpu2006_max_number = cpu2006_max_number + max(compar_cpu2006_keys) + 1 if compar_cpu2006_keys else cpu2006_max_number
                        cpu2017_max_number = cpu2017_max_number + max(compar_cpu2017_keys) + 1 if compar_cpu2017_keys else cpu2017_max_number

            new_json_file = json_file_path + str(base_env_time)+'.json'
            os.rename(new_json_file, new_json_file + '-env_' + str(env_id[0]) + '-base-old')

            with open(new_json_file, 'w', encoding='utf-8') as f_new:
                json.dump(data_, f_new)

            # 5、删除旧的数据
            for name in compar_env_times:
                os.rename(json_file_path + str(name)+'.json', json_file_path + str(name)+'.json-env_' + str(env_id[0]) +'-compar-old')
                log.info(new_json_file, '数据和', json_file_path + str(name) + '.json' + '数据合并完成')


        # 4、删除env_id的env表，删除env_id对应的project表
        Env.objects.filter(id__in=env_ids).delete()
        Project.objects.filter(env_id__in=env_ids).delete()
        # 5、修改project表对应测试项目的值
        stream_number = len(Stream.objects.filter(env_id=env_id[0]))
        lmbench_number = len(Lmbench.objects.filter(env_id=env_id[0]))
        Project.objects.filter(env_id=env_id[0]).update(stream=stream_number, lmbench=lmbench_number,
                                                        unixbench=unixbench_number + 1, fio=fio_number + 1,
                                                        iozone=iozone_number + 1, jvm2008=jvm2008_number + 1,
                                                        cpu2006=cpu2006_number + 1, cpu2017=cpu2017_number + 1)

        return json_response({}, status.HTTP_200_OK, '合并数据成功')

    def create(self, request, *args, **kwargs):
        data_project = {}
        data_project['env_id'] = request.__dict__['data_project']['env_id']
        if request.__dict__['project_message']:
            data_project['message'] = str(request.__dict__['project_message'])
        else:
            data_project['message'] = None
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

    def simulate_request(self, view_class, request_params):
        """
        模拟请求
        :param view_class:
        :param request_params:
        :return:
        """
        # 创建一个工厂对象
        factory = APIRequestFactory()
        # 创建一个视图的实例
        view = view_class()
        # 设置视图的属性
        view.request = factory.get('/path/to/view/', request_params)
        view.format_kwarg = None
        view.args = ()
        view.kwargs = {}
        # 调用视图的方法，得到响应对象
        response = view.list(view.request, *view.args, **view.kwargs)

        # 返回响应内容
        return response.content

    def download_excel(self, request, *args, **kwargs):
        """
        下载excel表格
        """
        # 再去获取全部的数据
        env_id = request.GET.get('env_id')
        comparsionIds = request.GET.get('comparsionIds')

        """env数据"""
        # 因为listhan函数中有self.get_serializer(serializer_, many=True)，如果用到的话会报错。所以不能像create方法那样使用
        from appStore.env.views import EnvViewSet
        env_data = self.simulate_request(EnvViewSet, {'env_id': env_id, 'comparsionIds': ""})
        env_data = json.loads(env_data)
        env_excel(request.user,env_data)

        """stream数据"""
        if Project.objects.filter(env_id = env_id).first().stream:
            from appStore.stream.views import StreamViewSet
            stream_data = self.simulate_request(StreamViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            stream_data = json.loads(stream_data)
            stream_excel(request.user,stream_data)

        """lmbench数据"""
        if Project.objects.filter(env_id=env_id).first().lmbench:
            from appStore.lmbench.views import LmbenchViewSet
            lmbench_data = self.simulate_request(LmbenchViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            lmbench_data = json.loads(lmbench_data)
            lmbench_excel(request.user,lmbench_data)

        """unixbench数据"""
        if Project.objects.filter(env_id=env_id).first().unixbench:
            from appStore.unixbench.views import UnixbenchViewSet
            unixbench_data = self.simulate_request(UnixbenchViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            unixbench_data = json.loads(unixbench_data)
            unixbench_excel(request.user,unixbench_data)

        """fio数据"""
        if Project.objects.filter(env_id=env_id).first().fio:
            from appStore.fio.views import FioViewSet
            fio_data = self.simulate_request(FioViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            fio_data = json.loads(fio_data)
            fio_excel(request.user,fio_data)

        """iozone数据"""
        if Project.objects.filter(env_id = env_id).first().iozone:
            from appStore.iozone.views import IozoneViewSet
            iozone_data = self.simulate_request(IozoneViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            iozone_data = json.loads(iozone_data)
            iozone_excel(request.user,iozone_data)

        """jvm2008数据"""
        if Project.objects.filter(env_id = env_id).first().jvm2008:
            from appStore.jvm2008.views import Jvm2008ViewSet
            jvm2008_data = self.simulate_request(Jvm2008ViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            jvm2008_data  = json.loads(jvm2008_data)
            jvm2008_excel(request.user,jvm2008_data)

        """speccpu2006数据"""
        if Project.objects.filter(env_id = env_id).first().cpu2006:
            from appStore.cpu2006.views import Cpu2006ViewSet
            cpu2006_data = self.simulate_request(Cpu2006ViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            cpu2006_data = json.loads(cpu2006_data)
            cpu2006_data_base = {'data': cpu2006_data["data"][:66]}
            cpu2006_data_peak = {'data': cpu2006_data["data"][:4] + cpu2006_data["data"][66:]}
            sheetname = "Speccpu2006(base)"
            cpu2006_excel(request.user,sheetname, cpu2006_data_base)
            sheetname = "Speccpu2006(peak)"
            cpu2006_excel(request.user,sheetname, cpu2006_data_peak)

        """speccpu2017数据"""
        if Project.objects.filter(env_id = env_id).first().cpu2017:
            from appStore.cpu2017.views import Cpu2017ViewSet
            cpu2017_data = self.simulate_request(Cpu2017ViewSet, {'env_id': env_id, 'comparsionIds': comparsionIds})
            cpu2017_data = json.loads(cpu2017_data)
            cpu2017_data_base = {'data': cpu2017_data["data"][:54]}
            cpu2017_data_peak = {'data': cpu2017_data["data"][:4] + cpu2017_data["data"][54:]}
            sheetname = "Speccpu2017(base)"
            cpu2017_excel(request.user,sheetname, cpu2017_data_base)
            sheetname = "Speccpu2017(peak)"
            cpu2017_excel(request.user,sheetname, cpu2017_data_peak)

        # todo 是否需要实现多线程记录数据，目前测试可以，如果有很多组数据的化可能会获取失败。
        # 打开文件
        file_path = os.path.join(settings.BASE_DIR, 'tem_excel/%s.xlsx'%(request.user))
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True,status=200)
        return HttpResponse('文件不存在', status=404)

