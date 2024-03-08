from django.conf.urls import url, include
from rest_framework import routers

from appStore.env.views import EnvViewSet
from appStore.project.views import ProjectViewSet
from appStore.stream.views import StreamViewSet


router = routers.DefaultRouter()
####################
#   公共地址映射  #
###################
router.register(r'stream', StreamViewSet, basename='stream')
router.register(r'env', EnvViewSet, basename='env')
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = [
    # url(r'^y_upload_file/', y_upload_file),  # upload_file
    url(r'', include(router.urls)),
    router.register(r'project', ProjectViewSet, basename='project')
]
