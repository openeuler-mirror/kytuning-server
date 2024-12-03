"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Thu Feb 29 16:18:43 2024 +0800
"""
# Generated by Django 3.2.18 on 2023-03-23 00:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iozone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_id', models.IntegerField(verbose_name='环境id')),
                ('execute_cmd', models.CharField(blank=True, max_length=255, null=True, verbose_name='执行命令')),
                ('modify_parameters', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改参数')),
                ('testcase_name', models.CharField(max_length=10, verbose_name='testcase name')),
                ('file_size', models.FloatField(verbose_name='文件大小')),
                ('block_size', models.FloatField(verbose_name='块大小')),
                ('Write_test', models.FloatField(verbose_name='写测试（KB/s）')),
                ('Rewrite_test', models.FloatField(verbose_name='重写测试（KB/s）')),
                ('read_test', models.FloatField(verbose_name='读测试（KB/s）')),
                ('reread_test', models.FloatField(verbose_name='重读测试（KB/s）')),
                ('random_read_test', models.FloatField(verbose_name='随机读测试（KB/s）')),
                ('random_write_test', models.FloatField(verbose_name='随机写测试（KB/s）')),
                ('test_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='测试时间')),
            ],
            options={
                'db_table': 'iozone',
            },
        ),
    ]
