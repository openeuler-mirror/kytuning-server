kylin-kytuning-backend
介绍
性能测试工具服务端，其中包括stream测试、lmbench测试、unixbench测试、fio测试、iozone测试、jvm2008测试、cpu2016测试、cpu2017测试。

软件架构
软件架构说明

安装教程
pip3 install -r requirements.txt
使用说明
# 创建setting.py文件中对应的数据库用户及表
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
参与贡献
Fork 本仓库
新建 Feat_xxx 分支
提交代码
新建 Pull Request
特技
使用 Readme_XXX.md 来支持不同的语言，例如 Readme_en.md, Readme_zh.md
Gitee 官方博客 blog.gitee.com
你可以 https://gitee.com/explore 这个地址来了解 Gitee 上的优秀开源项目
GVP 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
Gitee 官方提供的使用手册 https://gitee.com/help
Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 https://gitee.com/gitee-stars/