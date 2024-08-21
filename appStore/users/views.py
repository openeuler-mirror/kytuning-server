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


