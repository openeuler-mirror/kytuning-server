"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 10:00:37 2024 +0800
"""
#!/bin/bash

# 制作启动盘的路径
ISO_PATH="iso"
# 原始mount路径
MOUNT_PATH="/mnt/kylin-iso"
# ks文件名称
KS_FILE_NAME="kytuning-ks.cfg"
# 指定grub.cfg文件的路径
GRUB_CFG_PATH="$ISO_PATH/EFI/BOOT/grub.cfg"
# iso的下载路径
HTTP_ISO_PATH="http://localhost:9000/tools/Kylin-Server-V10-SP4-General-alpha-06-20231020-x86_64.iso"
# iso的名称
ISO_NAME=$(basename "$HTTP_ISO_PATH")
# efibootmgr对应的文件
BOOT_EFI="/EFI/BOOT/BOOTX64.EFI"
# BOOT_EFI="/EFI/BOOT/BOOTAA64.EFI"
# grub.cfg文件中原始的菜单名称
GRUB_MENU_NAME="Kylin-Server-10"
# 网卡名称
NETWORK_CARD="p17p2"
# 静态IP地址
NETWORK_IP="127.0.0.1"
# 所需要制作成启动盘的盘符
STARTUP_DISK="/dev/sda"
# 系统安装盘
SYSTEM_DISK='sdb'

init_file() {
  # 判断MOUNT_PATH是否挂载
  if [ -d "$MOUNT_PATH" ]; then
    mount_status=$(df -h | grep "$MOUNT_PATH" | wc -l)
    if [ "$mount_status" -gt 0 ]; then
      echo "======MOUNT_PATH被挂载，umount $MOUNT_PATH======"
      umount "$MOUNT_PATH"
    fi
    rm -r "$MOUNT_PATH"
  fi
  # 判断ISO_PATH是否挂载
  iso_mount_status=$(df -h | grep "$ISO_PATH" | wc -l)
  if [ "$iso_mount_status" -gt 0 ]; then
    echo "======ISO_PATH被挂载，umount $STARTUP_DISK======"
    umount "$STARTUP_DISK"
  fi

  mkdir -p $MOUNT_PATH
  mkdir -p $ISO_PATH
}

update_grub_cfg(){
  sed -i "s/$GRUB_MENU_NAME/Kytuning/g" $GRUB_CFG_PATH
  # 查找第一个menuentry所在的行号
  menuentry_line_number=$(grep -n -m 1 "menuentry" "$GRUB_CFG_PATH" | cut -d ":" -f 1)

  # 确保找到了menuentry
  if [ -n "$menuentry_line_number" ]; then
    # 在下一行增加inst.ks
    menuentry_line_number=$((menuentry_line_number + 1))
    # todo测试时先注销掉。
    sed -i "${menuentry_line_number}s/$/ inst.ks=hd:LABEL=Kytuning:\/$KS_FILE_NAME inst.repo=hd:LABEL=Kytuning/" "$GRUB_CFG_PATH"
    echo "======在第 ${menuentry_line_number} 行添加了 inst.ks信息======"
  else
    echo "======未找到menuentry======"
  fi
}

update_efi_bootorder(){
  # 获取当前 EFI 启动项列表
  boot_order=$(efibootmgr | grep BootOrder | awk -F': ' '{print $2}')
  # 将 EFI 启动项列表转换为数组
  IFS=',' read -ra boot_order_array <<< "$boot_order"
  # 将第一个启动项移到列表的最后
  first_boot_entry="${boot_order_array[0]}"
  boot_order_array=("${boot_order_array[@]:1}" "$first_boot_entry")
  # 将数组重新转换为逗号分隔的字符串
  new_boot_order=$(IFS=, ; echo "${boot_order_array[*]}")
  # 使用 efibootmgr 更新 EFI 启动项顺序
  efibootmgr -o "$new_boot_order"
}
new_vfat_part(){
  [ x"$1" == x"" ] && exit
  fdisk $1 << EOF
g
n
1
2048
+10G
w
EOF
}

clear_kytuning_efibootmgr(){
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
}

# 初始化文件夹
init_file "$MOUNT_PATH"

if [ ! -f "$ISO_NAME" ]; then
  # 如果文件不存在，则进行下载
  wget $HTTP_ISO_PATH
fi
new_vfat_part $STARTUP_DISK
mkfs.vfat -n Kytuning $STARTUP_DISK"1"
mount $ISO_NAME $MOUNT_PATH
mount $STARTUP_DISK"1" $ISO_PATH
cp -ar $MOUNT_PATH/. $ISO_PATH
#修改grub.cfg文件
update_grub_cfg
# 替换网卡信息
cp $KS_FILE_NAME $ISO_PATH
sed -i "s/NETWORK_CARD/$NETWORK_CARD/g; s/NETWORK_IP/$NETWORK_IP/g" "$ISO_PATH/$KS_FILE_NAME"
# 替换ks文件中安装操作系统盘
sed -i "s/SYSTEM_DISK/$SYSTEM_DISK/g" "$ISO_PATH/$KS_FILE_NAME"
clear_kytuning_efibootmgr
efibootmgr --create --disk $STARTUP_DISK --part 1 --loader $BOOT_EFI --label "Kytuning"
# update_efi_bootorder
sync
#reboot