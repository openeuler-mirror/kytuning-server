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
#GRUB_MENU_NAME="Kylin-Server-10"
GRUB_MENU_NAME="UnionTechOS"

# 网卡名称
#NETWORK_CARD="enp125s0f0"
NETWORK_CARD=$(ip link show | awk -F ': ' '/state UP/ {print $2; exit}')
# 系统安装盘
#SYSTEM_DISK='sdb'
SYSTEM_DISK=$(df -lh | grep /boot/efi | awk '{print substr($1,6,3)}')
# 所需要制作成启动盘的盘符
#STARTUP_DISK="sda"
STARTUP_DISK=$(ls /dev/sd[^"${SYSTEM_DISK: -1}"]* | head -n 1 | awk -F'/' '{print $3}')

init_file() {
  # 判断MOUNT_PATH是否挂载
  if [ -d "$MOUNT_PATH" ]; then
    mount_status=$(df -h | grep "$MOUNT_PATH" | wc -l)
    if [ "$mount_status" -gt 0 ]; then
      echo "======MOUNT_PATH被挂载，umount $MOUNT_PATH======"
      umount "$MOUNT_PATH"
    fi
    rm -r $MOUNT_PATH
  fi
  # 判断ISO_PATH是否挂载
  iso_mount_status=$(df -h | grep "$ISO_PATH" | wc -l)
  if [ "$iso_mount_status" -gt 0 ]; then
    echo "======ISO_PATH被挂载，umount /dev/$STARTUP_DISK 1======"
    umount /dev/$STARTUP_DISK"1"
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
  boot_entries=$(sudo efibootmgr | awk '/Kytuning/ {print $1}')
  clean_entry=$(echo "$boot_entries" | tr -cd '[:alnum:]' | sed 's/Boot//')
  efibootmgr -n $clean_entry
}
new_vfat_part(){
  [ x"$1" == x"" ] && exit

  CHK=$(lsblk /dev/$1 -o +fstype|grep ^$1|awk '{print $NF}')
  [ x"$CHK" == x"iso9660" ] && dd if=/dev/zero of=/dev/$1 bs=512 count=1024

  parted -s /dev/$1 mklabel gpt
  parted -s /dev/$1 mkpart primary 1049kb 10G
  partprobe
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
mkfs.vfat -n Kytuning /dev/$STARTUP_DISK"1"
mount $ISO_NAME $MOUNT_PATH
mount /dev/$STARTUP_DISK"1" $ISO_PATH
cp -ar $MOUNT_PATH/. $ISO_PATH
# 修改grub.cfg文件
update_grub_cfg
# 替换网卡信息
cp $KS_FILE_NAME $ISO_PATH
sed -i "s/NETWORK_CARD/$NETWORK_CARD/g; s/NETWORK_IP/$NETWORK_IP/g" "$ISO_PATH/$KS_FILE_NAME"
# 替换ks文件中安装操作系统盘
sed -i "s/SYSTEM_DISK/$SYSTEM_DISK/g" "$ISO_PATH/$KS_FILE_NAME"
clear_kytuning_efibootmgr
cp clear_kytuning_efibootmgr.sh $ISO_PATH
efibootmgr --create --disk /dev/$STARTUP_DISK --part 1 --loader $BOOT_EFI --label "Kytuning"
# 使用efibootmgr -n 命令指定下次启动项
update_efi_bootorder
sync
#reboot