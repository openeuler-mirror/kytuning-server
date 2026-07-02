"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""

import logging
from rest_framework import status, viewsets
# Create your views here.
from appStore.users.models import UserProfile
from appStore.users.serializers import UserProfileSerializer
from appStore.utils.common import json_response, get_error_message

log = logging.getLogger('kytuninglog')


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    用户数据管理
    """
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer_user = self.get_serializer(data=request.data)
        if serializer_user.is_valid():
            user = UserProfile.objects.create_user(username=serializer_user.data['username'],
                                                   password=serializer_user.data['password'],
                                                   chinese_name=serializer_user.data['chinese_name'])
            # 可以根据需要设置其他用户属性
            user.save()
            return json_response(serializer_user.data, status.HTTP_200_OK, '创建成功！')
        log.info('user数据存储错误 ：%s，' % serializer_user.errors)
        return json_response(serializer_user.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer_user))

    def change_password(self, request, *args, **kwargs):
        # 获取当前用户
        user = request.user
        # 获取新密码
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        if new_password1 == new_password2:
            # 修改密码
            user.set_password(new_password1)
            user.save()
            # 返回密码修改成功的响应
            return json_response({'new_password': new_password1}, status.HTTP_200_OK, '修改密码完成')
        else:
            return json_response({}, status.HTTP_400_BAD_REQUEST, '两次密码不一致')
