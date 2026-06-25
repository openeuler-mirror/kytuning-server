"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Mon Feb 26 11:15:07 2024 +0800
"""
# -*- coding: utf-8 -*-
import os
import re
import json
import requests
import hashlib
import base64
import hmac
import time

from appStore.utils.constants import lanxin_url, secret

# 需要修改kytuning.cfg中project_name为特殊的指定格式，目前定义为"定时任务-IP"
CONFIF_FILE = '/root/run_kytuning-ffdev/conf/kytuning.cfg'

def get_compar_url(CONFIF_FILE):
    if not os.path.exists(CONFIF_FILE):
        # 这里还需要验证用户账号密码，设备权限等，所以直接让用户再页面提交一次测试
        print("没有初始化，请现在页面提交一次测试并配置好需要测试的项目")
        exit(0)

    # 读取文件内容
    with open(CONFIF_FILE, encoding='utf-8') as f:
        file_content = f.read()

    # 去除以#开头的注释行
    lines = file_content.split('\n')
    filtered_lines = [line for line in lines if not line.strip().startswith('#')]
    filtered_content = '\n'.join(filtered_lines)

    # 使用正则表达式匹配键值对
    pattern = re.compile(r'^(.*?)=(.*?)$', re.MULTILINE)
    matches = pattern.findall(filtered_content)

    config = dict(matches)

    # 获取对应的键值
    project_name = config.get('project_name')
    username = config.get('username')
    password = config.get('password')
    token = config.get('token')
    kytuning_web_url = config.get('kytuning_web_url')

    if not token:
        login_url = kytuning_web_url + '/kytuning/api-token-auth/'
        response = requests.post(login_url, data={'username': username, 'password': password}, verify=False)
        if response.status_code != 200:
            print("请确认账号密码正确！")
            exit(0)
        token = 'Bearer ' + response.json()['token']
    # 发送 curl 请求
    get_compar_url = kytuning_web_url + '/kytuning/project/?ProjectWeb=false&project_name={}&user_name=&os_names=&cpu_names='.format(project_name)
    headers = {
        'User-Agent': 'curl/7.58.0',
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    response = requests.get(get_compar_url, headers=headers, verify=False)
    # 输出服务器响应
    sorted_env_ids = sorted([entry['env_id'] for entry in json.loads(response.content.decode('utf-8'))['data']], reverse=True)
    compar_url = kytuning_web_url+'/stream/{}/{}'.format(sorted_env_ids[0],sorted_env_ids[1])
    print(compar_url)
    return compar_url


def send_lanxin_message(username, compar_url):
    timestamp = int(round(time.time()))
    string_to_sign = '{}@{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')

    headers = {
        'User-Agent': 'curl/7.58.0',
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    if username:
        data = {
            "timestamp": str(timestamp),
            "sign": sign,
            "msgType": "text",
            "msgData": {
                "text": {
                    "content": "@{} 您的测试已完成请及时查看：{}".format(username, compar_url),
                }
            }
        }
    else:
        data = {
            "timestamp": str(timestamp),
            "sign": sign,
            "msgType": "text",
            "msgData": {
                "text": {
                    "content": """
【迭代测试发布通知】 
数据对比地址：{}
请及时协调人员排查
(虚拟机测试阶段请不用理会)""".format(compar_url),
                    "reminder": {
                        "all": True,
                    }
                }
            }
        }
    requests.post(lanxin_url, headers=headers, json=data, verify=False)
    # 输出服务器响应
    # print(json.loads(response.content.decode('utf-8')))
    return

# 在迭代更新的机器中打开
# compar_url = get_compar_url(CONFIF_FILE)
# send_lanxin_message(username, compar_url)
