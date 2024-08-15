from rest_framework.authentication import SessionAuthentication

from appStore.users.models import UserProfile
from rest_framework import status
from appStore.users.serializers import UserProfileSerializer
from appStore.utils.common import json_response
from appStore.utils.customer_view import CusModelViewSet
# Create your views here.

class UserProfileViewSet(CusModelViewSet):
    """
    用户数据管理
    """
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer