#!/bin/bash
# clear_kytuning_efibootmgr.sh
echo "=========运行clear_kytuning_efibootmgr.sh脚本========"
# 获取所有包含 "Kytuning" 的引导项的引导号
boot_entries=$(efibootmgr | awk '/Kytuning/ {print $1}')

if [ -n "$boot_entries" ]; then
  # 删除每个引导项
  for entry in $boot_entries; do
    # 清理引导号中的无效字符*并去掉 "Boot" 字段
    clean_entry=$(echo "$entry" | tr -cd '[:alnum:]' | sed 's/Boot//')

    # 删除引导项
    efibootmgr -b "$clean_entry" -B
    echo "已成功删除引导项 '$clean_entry'"
  done
fi