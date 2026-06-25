"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 10:00:37 2024 +0800
"""
# 后端项目运行日志存放路径
LOGGING_DIR = "/var/log/kytuning/"

# 服务端记录测试端的测试日志路径
RESULT_LOG_FILE = '/var/www/html/result_log_file/'

#用户配置文件路径
RUN_KYTUNING_CONFIG_TEMP = '/opt/kytuning/run_kytuning_config_temp/'

# 制作用户所需表格路径
EXCEL_TEMP = '/opt/kytuning/excel_temp/'

# 测试项目对应的tools包网址
TOOLS_URL = 'http://localhost:9000/tools/run_kytuning-ffdev-94.zip'
kytuning_web_url='https://localhost'

# 蓝信机器人的密钥
# 下面两个不要暴露出去，因为此处要测试暂时放这里！！！
secret = "xxxxx"
lanxin_url = 'https://apigw-cec.cec.com.cn/v1/bot/hook/messages/create?hook_token=xxxx'
