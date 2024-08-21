from django.conf.urls import url, include
from rest_framework import routers

from appStore.cpu2006.views import Cpu2006ViewSet
from appStore.cpu2017.views import Cpu2017ViewSet
from appStore.env.views import EnvViewSet
from appStore.fio.views import FioViewSet
from appStore.iozone.views import IozoneViewSet
from appStore.jvm2008.views import Jvm2008ViewSet
from appStore.lmbench.views import LmbenchViewSet
from appStore.project.views import ProjectViewSet
from appStore.stream.views import StreamViewSet
from appStore.unixbench.views import UnixbenchViewSet
from appStore.users.views import UserProfileViewSet

router = routers.DefaultRouter()
####################
#   公共地址映射  #
###################
router.register(r'cpu2006', Cpu2006ViewSet, basename='cpu2006')
router.register(r'cpu2017', Cpu2017ViewSet, basename='cpu2017')
router.register(r'env', EnvViewSet, basename='env')
router.register(r'fio', FioViewSet, basename='fio')
router.register(r'iozone', IozoneViewSet, basename='iozone')
router.register(r'jvm2008', Jvm2008ViewSet, basename='jvm2008')
router.register(r'lmbench', LmbenchViewSet, basename='lmbench')
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'stream', StreamViewSet, basename='stream')
router.register(r'unixbench', UnixbenchViewSet, basename='unixbench')
router.register(r'users', UserProfileViewSet, basename='users')

urlpatterns = [
    # url(r'^y_upload_file/', y_upload_file),  # upload_file
    url(r'', include(router.urls)),
    url('^get_filter_name/', ProjectViewSet.as_view({'get': 'get_filter_name'}), name='get_filter_name'),
    url('^stream_data/', StreamViewSet.as_view({'get': 'get_stream_data'}), name='stream_data'),
    url('^change_password/', UserProfileViewSet.as_view({'put': 'change_password'}), name='change_password'),
]
