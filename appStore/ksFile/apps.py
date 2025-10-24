"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 10:58:36 2024 +0800
"""

from django.apps import AppConfig


class KsFileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appStore.ksFile'
