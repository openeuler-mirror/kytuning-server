"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:19:26 2024 +0800
"""
import django_filters
from django_filters import rest_framework as filters

from appStore.errorList.models import KytuningError


class ErrorFilter(filters.FilterSet):
    """
    错误排查
    """
    mix_id = django_filters.NumberFilter(field_name='id', lookup_expr='gt')
    error_type = django_filters.CharFilter(field_name='error_type', lookup_expr='icontains')
    test_type = django_filters.CharFilter(field_name='test_type', lookup_expr='icontains')
    error_description = django_filters.CharFilter(field_name='error_description', lookup_expr='icontains')
    error_log_excerpt = django_filters.CharFilter(field_name='error_log_excerpt', lookup_expr='icontains')
    class Meta:
        model = KytuningError
        fields = ['mix_id',] # 允许精准查询的字段
        search_fields = ['error_type','test_type','error_description','error_log_excerpt'] # 允许模糊查询的字段


