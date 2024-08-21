from rest_framework.authentication import SessionAuthentication

from appStore.users.models import UserProfile
from rest_framework import status
from appStore.users.serializers import UserProfileSerializer
from appStore.utils.common import json_response, get_error_message
from appStore.utils.customer_view import CusModelViewSet
# Create your views here.

class UserProfileViewSet(CusModelViewSet):
    """
    用户数据管理
    """

    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = UserProfile.objects.create_user(username=serializer.data['username'],
                                                   password=serializer.data['password'],
                                                   chinese_name=serializer.data['chinese_name'])
            # 可以根据需要设置其他用户属性
            user.save()
            return json_response(serializer.data, status.HTTP_200_OK, '创建成功！')
        return json_response(serializer.errors, status.HTTP_400_BAD_REQUEST, get_error_message(serializer))


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
            return json_response({'new_password':new_password1}, status.HTTP_200_OK, '修改密码完成')
        else:
            return json_response({}, status.HTTP_201_CREATED, '两次密码不一致')