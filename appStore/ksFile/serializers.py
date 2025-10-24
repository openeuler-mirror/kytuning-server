"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 10:58:36 2024 +0800
"""
from rest_framework import serializers
from appStore.ksFile.models import KsFile


class KsFileListSerializer(serializers.ModelSerializer):
    """
    ks文件数据序列化
    """

    class Meta:
        model = KsFile
        fields = '__all__'
