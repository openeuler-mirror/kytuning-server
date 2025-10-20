"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""
from rest_framework import serializers

from appStore.adaptISO.models import AdaptISO


class AdaptISOListSerializer(serializers.ModelSerializer):
    """
    errorList数据序列化
    """

    class Meta:
        model = AdaptISO
        fields = '__all__'

