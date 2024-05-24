# kytuning-server

#### 介绍
1. 在操作系统性能基准测试优化过程中，往往存在基准测试工具繁多、数据对比繁琐、缺乏高效的性能问题分析工具等问题。Kytuning提供了一种工具，可以帮助完成繁琐和重复的任务，从而释放人力，并使工程师能够专注于分析和解决性能问题。 

   Kytuning最初计划支持以下基准测试工具： 

   - unixbench
   - lmbench
   - fio
   - iozone
   - specjvm2008
   - stream
   - speccpu2006
   - speccpu2017

   #### 软件构架

   软件架构描述在Kytuning测试系统的整体架构中主要有三个角色：目标测试机、Kytuning测试系统服务和Web管理客户端。kytuning-server作为测试管理、数据存储、页面显示终端 

   #### 软件构架

   软件体系结构描述 

   #### 安装

   1. pip3 install -r requirements.txt
   2. yun install -r nginx httpd

   #### 指令

   1. 构建和配置nginx+uwsgi服务 
   2. 启动uwsgi : uwsgi --ini uwsgi.ini
   3. 重启nginx : systemctl 重启nginx.service

   #### Contribution

   1. 克隆仓库
   2. 提交代码 
   3. 创建合并请求 

   #### Gitee Feature Gitee功能

   1. 您可以使用Readme_XXX. md来支持不同的语言，例如Readme_en. md、Readme_zh.md 
   2. Gitee博客[blog.gitee.com](https://blog.gitee.com)
   3. 探索开源项目https://gitee.com/explore 
   4. 最有价值的开源项目GVP 
   5. Gitee手册https://gitee.com/help 
   6. 最受欢迎的会员https://gitee.com/gitee-stars/ 
