#!/bin/bash
mkdir wqz
# 获取所有包含 "Kytuning" 的引导项的引导号
boot_entries=$(sudo efibootmgr | awk '/Kytuning/ {print $1}')

if [ -n "$boot_entries" ]; then
  # 删除每个引导项
  for entry in $boot_entries; do
    # 清理引导号中的无效字符*并去掉 "Boot" 字段
    clean_entry=$(echo "$entry" | tr -cd '[:alnum:]' | sed 's/Boot//')

    # 删除引导项
    sudo efibootmgr -b "$clean_entry" -B
    echo "已成功删除引导项 '$clean_entry'"
  done
fi