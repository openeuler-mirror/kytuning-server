from django.conf.urls import url, include
from rest_framework import routers

from appStore.env.views import EnvViewSet

router = routers.DefaultRouter()
####################
#   公共地址映射  #
###################
router.register(r'env', EnvViewSet, basename='env')

urlpatterns = [
    # url(r'^y_upload_file/', y_upload_file),  # upload_file
    url(r'', include(router.urls)),
]
