# -*- coding: utf-8 -*-
import re
import json
import requests

# 需要修改kytuning.cfg中project_name为特殊的指定格式，目前定义为"定时任务-IP"
CONFIF_FILE = '/root/run_kytuning-ffdev/conf/kytuning.cfg'

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
    response = requests.post(login_url,data={'username':username,'password':password}, verify=False)
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
url=kytuning_web_url+'/stream/{}/{}'.format(sorted_env_ids[0],sorted_env_ids[1])
print(url)

# 再次对接蓝信API
