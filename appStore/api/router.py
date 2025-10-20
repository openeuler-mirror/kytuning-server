"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:19:26 2024 +0800
"""
from django.conf.urls import url, include
from rest_framework import routers

from appStore.adaptISO.views import AdaptISOListViewSet
from appStore.cpu2006.views import Cpu2006ViewSet
from appStore.cpu2017.views import Cpu2017ViewSet
from appStore.env.views import EnvViewSet
from appStore.errorList.views import ErrorListViewSet
from appStore.fio.views import FioViewSet
from appStore.iozone.views import IozoneViewSet
from appStore.jvm2008.views import Jvm2008ViewSet
from appStore.lmbench.views import LmbenchViewSet
from appStore.project.views import ProjectViewSet
from appStore.stream.views import StreamViewSet
from appStore.testCase.views import TestCaseViewSet
from appStore.testMachine.views import TestMachineViewSet
from appStore.unixbench.views import UnixbenchViewSet
from appStore.userConfig.views import UserConfigViewSet
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
router.register(r'test_case', TestCaseViewSet, basename='test_case')
router.register(r'user_config', UserConfigViewSet, basename='user_config')
router.register(r'error_list', ErrorListViewSet, basename='error_list')
router.register(r'machine_list', TestMachineViewSet, basename='machine_list')
router.register(r'get_adapt_ISO', AdaptISOListViewSet, basename='adapt_ISO')

urlpatterns = [
    url(r'', include(router.urls)),
    url('^apply_use_machine/', TestMachineViewSet.as_view({'post': 'apply_use_machine'}), name='apply_use_machine'),
    url('^cancel_apply_use_machine/', TestMachineViewSet.as_view({'post': 'cancel_apply_use_machine'}), name='cancel_apply_use_machine'),
    url('^finished_using/', TestMachineViewSet.as_view({'post': 'finished_using'}), name='finished_using'),
    url('^update_status/', TestMachineViewSet.as_view({'post': 'update_status'}), name='update_status'),
    url('^modify_server/', TestMachineViewSet.as_view({'post': 'modify_server'}), name='modify_server'),
    url('^get_filter_name/', ProjectViewSet.as_view({'get': 'get_filter_name'}), name='get_filter_name'),
    url('^merge_data/', ProjectViewSet.as_view({'post': 'merge_data'}), name='merge_data'),
    url('^download_excel/', ProjectViewSet.as_view({'get': 'download_excel'}), name='download_excel'),
    url('^get_modify_stream/', StreamViewSet.as_view({'get': 'get_modify_stream'}), name='get_modify_stream'),
    url('^change_password/', UserProfileViewSet.as_view({'put': 'change_password'}), name='change_password'),
    url('^do_test_case/', TestCaseViewSet.as_view({'post': 'do_test_case'}), name='do_test_case'),
    url('^down_message/', TestCaseViewSet.as_view({'get': 'down_message'}), name='down_message'),

]
