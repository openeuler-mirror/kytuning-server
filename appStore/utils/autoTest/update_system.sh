#!/bin/bash

# 第一步需要手动配置对应的kojifiles源

# 使用yum获取更新列表，去除标题行，提取包名，然后去除最后一个点号及之后的内容
updates=$(yum list updates | grep -v "Available" | grep -v "Last" | awk '{print $1}' | sed 's/\.[^.]*$//')

rm -rf package_list.txt
update=false
for package in $updates; do
    update=true
    echo "rpm包版本记录-----" >> package_list.txt
    echo `rpm -qa | grep ^$package` >> package_list.txt
    #yum install $package -y
    echo `rpm -qa | grep ^$package` >> package_list.txt
done
echo $update
if [ "$update" = true ];then
  `cd run_kytuning-ffdev;sh run.sh`
  # 获取配置文件中的项目名称信息
  python3 get_compar_url.py
fi
