from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
####################
#   公共地址映射  #
###################

urlpatterns = [
    url(r'', include(router.urls)),
]
