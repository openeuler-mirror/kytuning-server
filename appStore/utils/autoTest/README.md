# 迭代测试全流程

#### 介绍
```
此功能实现了在ISO迭代的过程中能够及时更新迭代的包，并发起性能测试，当测试完成后获取最近的两条测试数据通过蓝信通知发送给测试人员
```

#### 使用说明

```
1、安装迭代最新一版本的操作系统
2、在yum源中配置迭代过程中的源地址
3、使crontab设置定时执行update_system.sh脚本实现自动安装最新版本的软件包
4、需要修改kytuning.cfg中project_name名称，因为通过这个字段获取对比数据，需要注意自动化更新的project_name需要为指定格式，目前定义为"定时任务-IP"如"定时任务-127.0.0.1"
5、当运行脚本后会判断是否有软件包更新，如果有软件包更新则会发起测试指令
6、测试完成后发送测试数据与上次的数据形成对比连接并通过蓝信发送给用户
```

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
