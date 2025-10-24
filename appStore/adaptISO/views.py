"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
# Create your views here.
import logging
from rest_framework import status, viewsets
# Create your views here.
from appStore.adaptISO.models import AdaptISO
from appStore.adaptISO.serializers import AdaptISOListSerializer
from appStore.utils.common import LimsPageSet, json_response
from appStore.utils.constants import TOOLS_URL

log = logging.getLogger('kytuninglog')

class AdaptISOListViewSet(viewsets.ModelViewSet):
    """
     iso适配列表数据管理
    """
    queryset = AdaptISO.objects.all()
    serializer_class = AdaptISOListSerializer
    pagination_class = LimsPageSet

    def list(self, request, *args, **kwargs):
        queryset = AdaptISO.objects.all().order_by('ISO_name')
        serializer = self.get_serializer(queryset, many=True)
        return json_response(serializer.data, status.HTTP_200_OK, '查询完成')

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            data_iso = {}
            data_iso['user_name'] = request.user.chinese_name
            data_iso['http_address'] = request.data.get('http_address')
            data_iso['arch_name'] = request.data.get('arch_name')
            data_iso['ks_file_name'] = TOOLS_URL + '/auto-install/' + request.data.get('ks_file_name')
            data_iso['ISO_name'] = request.data.get('http_address').split('/')[-1]
            if data_iso['ISO_name'].endswith('iso'):
                config_serializer = AdaptISOListSerializer(data=data_iso)
                if config_serializer.is_valid():
                    self.perform_create(config_serializer)
                    return json_response(config_serializer.data, status.HTTP_200_OK, '创建成功！')
                log.info('Adaptiso数据存储错误 ：%s，', config_serializer.errors)
                log.info('Adaptiso存储数据为 ：%s，', data_iso)
                return json_response(config_serializer.errors, status.HTTP_400_BAD_REQUEST, config_serializer.errors)
            else:
                return json_response({}, status.HTTP_400_BAD_REQUEST, '请检查iso路径以iso结尾')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只有管理员才能创建该数据')

    def put(self, request, *args, **kwargs):
        if request.user.is_superuser:
            iso_id = request.data.get('id')
            iso_data = AdaptISO.objects.get(id=iso_id)
            if not iso_id or not iso_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            if iso_data.http_address != request.data.get('http_address'):
                new_iso_name = request.data.get('http_address').split('/')[-1]
                if iso_data.ISO_name != new_iso_name:
                    if AdaptISO.objects.get(ISO_name=new_iso_name):
                        return json_response({}, status.HTTP_205_RESET_CONTENT,
                                             '"ISO_name": [ "具有 ISO名称 的 adapt iso 已存在。"] ')
            iso_data.http_address = request.data.get('http_address')
            iso_data.arch_name = request.data.get('arch_name')
            iso_data.ks_file_name = TOOLS_URL + '/auto-install/' + request.data.get('ks_file_name')
            iso_data.ISO_name = request.data.get('http_address').split('/')[-1]
            iso_data.save()
            return json_response('', status.HTTP_200_OK, '更新成功！')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只有管理员才能修改数据')

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            id = request.data.get('id', None)
            if not id or not AdaptISO.objects.filter(id=id):
                return json_response({}, status.HTTP_205_RESET_CONTENT, '请传递正确的测试id')
            test_case_data = AdaptISO.objects.filter(id=id).first()
            if not test_case_data:
                return json_response({}, status.HTTP_205_RESET_CONTENT, '没有该数据')
            AdaptISO.objects.filter(id=id).delete()
            return json_response({}, status.HTTP_200_OK, '删除成功')
        else:
            return json_response({}, status.HTTP_205_RESET_CONTENT, '只有管理员才能删除该数据')

    def get_ks(self, request, *args, **kwargs):
        # 先手动写四后期在考虑是做成数据库还是读取路径下的ks文件名称
        data=[]
        import requests
        import re
        url = TOOLS_URL+'/auto-install/'
        response = requests.get(url)
        if response.status_code == 200:
            cfg_files = re.findall(r'href="([^"]*\.cfg)"', response.text)
            data = sorted(cfg_files)
        if data:
            return json_response(data, status.HTTP_200_OK, '获取ks列表完成')
        else:
            return json_response(data, status.HTTP_200_OK, '未获取到ks文件，请确认httpd服务器是否工作正常')
