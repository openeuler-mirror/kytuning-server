"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Mar 1 10:09:12 2024 +0800
"""

# 后端项目运行日志存放路径
LOGGING_DIR = '/var/log/kytuning/'

# 服务端记录测试端的测试日志路径
RESULT_LOG_FILE = '/var/www/html/result_log_file/'

# 用户配置文件路径
RUN_KYTUNING_CONFIG_TEMP = '/opt/kytuning/run_kytuning_config_temp/'

# 制作用户所需表格路径
EXCEL_TEMP = '/opt/kytuning/excel_temp/'

# todo 这个地方因为要发送请求所以IP是不可避免的，或者申请一个域名。
# 测试项目对应的tools包网址
TOOLS_URL = 'http://localhost:9000/tools/'

# kytuning web 网址
KYTUNING_WEB_URL = 'https://localhost'

# 蓝信机器人的密钥
# 下面两个不要暴露出去，因为此处要测试暂时放这里！！！
SECRET = "xxxxx"
LANXIN_URL = 'https://apigw-cec.cec.com.cn/v1/bot/hook/messages/create?hook_token=xxxx'

# 自动化安装时的变量
NEW_SERVER_NAME = 'root'
NEW_SERVER_PASSWORD = 'xxxxx'
ROOT_SIZE = 300
SWAP_SIZE = 4
DNS = '8.8.8.8'

# 检查2小时超时代表安装失败
CHECK_TIMEOUT = 7200
# INTERVAL = 1200  # 每20分钟检查一次
INTERVAL = 30  # 每20分钟检查一次
# {ip:开始时间}
START_TIME = {}

KOJIFILES_MD5 = {}
# 3天一次
MONITOR_KOJIFILES_TIME = 30
