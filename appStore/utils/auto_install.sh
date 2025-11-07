#!/bin/bash

# 制作启动盘的路径
ISO_PATH="kytuning-iso"
# 原始mount路径
MOUNT_PATH="/mnt/kytuning-iso"
KS_FILE_NAME=''
# 指定grub.cfg文件的路径
GRUB_CFG_PATH="$ISO_PATH/EFI/BOOT/grub.cfg"
# iso的下载路径
HTTP_ISO_PATH=""
# iso的名称
ISO_NAME=$(basename "$HTTP_ISO_PATH")
# 静态IP地址
NETWORK_IP=""
# efibootmgr对应的文件
BOOT_EFI=""
# 磁盘个数
DISK_COUNT=$(lsblk -d -o NAME | grep -c '^sd')
# 系统安装盘
SYSTEM_DISK=$(df -lh | grep /boot/efi | awk '{print substr($1,6,3)}')
# 所需要制作成启动盘的盘符
STARTUP_DISK=$(ls /dev/sd[^"${SYSTEM_DISK: -1}"]* | head -n 1 | awk -F'/' '{print $3}')
# ks文件中的加密密码
PASSWORD=''
LOG_FILE='/var/log/kytuning-auto-install.log'

init_file() {
  umount "/mnt"
  umount "$MOUNT_PATH"
  umount /dev/$STARTUP_DISK*
  rm -r $MOUNT_PATH
  rm -r $ISO_PATH
  mkdir -p $MOUNT_PATH
  mkdir -p $ISO_PATH
  echo '[info]:初始化ISO挂载镜像文件夹完成' | tee -a "$LOG_FILE"
}

update_grub_cfg(){
  # 设置安装系统启动项（openEuler默认是1）。
  sed -i 's/set default="1"/set default="0"/g' $GRUB_CFG_PATH
  # grub.cfg文件中原始的菜单名称
  GRUB_MENU_NAME=$(grep -oP "LABEL=\K[^ ]+" $MOUNT_PATH/EFI/BOOT/grub.cfg | head -n 1)
  sed -i "s/$GRUB_MENU_NAME/Kytuning/g" $GRUB_CFG_PATH
  # 查找第一个menuentry所在的行号
  menuentry_line_number=$(grep -n -m 1 "menuentry" "$GRUB_CFG_PATH" | cut -d ":" -f 1)
  if [ -n "$menuentry_line_number" ]; then
    # 在下一行增加inst.ks
    menuentry_line_number=$((menuentry_line_number + 1))
    sed -i "${menuentry_line_number}s/$/ inst.ks=hd:LABEL=Kytuning:\/$KS_FILE_NAME inst.repo=hd:LABEL=Kytuning/" "$GRUB_CFG_PATH"
    echo '[info]:修改grub配置文件内容完成' | tee -a "$LOG_FILE"
  else
    echo '[error]:未找到menuentry' | tee -a "$LOG_FILE"
    exit 0
  fi
}

update_efi_bootorder(){
  boot_entries=$(sudo efibootmgr | awk '/Kytuning/ {print $1}')
  clean_entry=$(echo "$boot_entries" | tr -cd '[:alnum:]' | sed 's/Boot//')
  efibootmgr -n $clean_entry
  echo '[info]:设置下次启动引导项为kytuning完成' | tee -a "$LOG_FILE"
}
new_vfat_part(){
  [ x"$1" == x"" ] && exit
  CHK=$(lsblk /dev/$1 -o +fstype|grep ^$1|awk '{print $NF}')
  [ x"$CHK" == x"iso9660" ] && dd if=/dev/zero of=/dev/$1 bs=512 count=1024
  parted -s /dev/$1 mklabel gpt
  parted -s /dev/$1 mkpart primary 1049kb 10G
  partprobe
  echo '[info]:格式化启动盘完成' | tee -a "$LOG_FILE"
}

clear_kytuning_efibootmgr(){
  # 获取所有包含 "Kytuning" 的引导项的引导号
  boot_entries=$(sudo efibootmgr | awk '/Kytuning/ {print $1}')
  if [ -n "$boot_entries" ]; then
    for entry in $boot_entries; do
      # 清理引导号中的无效字符*并去掉 "Boot" 字段
      clean_entry=$(echo "$entry" | tr -cd '[:alnum:]' | sed 's/Boot//')
      # 删除kytuning引导项
      sudo efibootmgr -b "$clean_entry" -B
    done
  fi
  echo '[info]:删除kytuning引导项完成' | tee -a "$LOG_FILE"
}

main(){
  echo '===============[info]:自动安装脚本运行开始，开始时间：'$(date) | tee "$LOG_FILE"
  if [ $DISK_COUNT -lt 2 ]; then
    echo '[error]:当前系统只有一个盘不支持安装' | tee -a "$LOG_FILE"
    exit 1
  fi
  if [ -z "$SYSTEM_DISK" ]; then
    echo '[error]: 未自动识别到系统盘，请排查lsblk中是否有/boot/efi分区' | tee -a "$LOG_FILE"
    exit 1
  fi
  init_file "$MOUNT_PATH"
  if [ ! -f "$ISO_NAME" ]; then
    echo '[info]:当前系统安装的iso为：'$ISO_NAME | tee -a "$LOG_FILE"
    wget $HTTP_ISO_PATH
    if [ $? -ne 0 ]; then
      echo '[error]:下载镜像失败，请检查网络和下载地址是否正确' | tee -a "$LOG_FILE"
      exit 1
    fi
  fi
  new_vfat_part $STARTUP_DISK
  mkfs.vfat -n Kytuning /dev/$STARTUP_DISK"1"
  mount $ISO_NAME $MOUNT_PATH
  mount /dev/$STARTUP_DISK"1" $ISO_PATH
  cp -ar $MOUNT_PATH/. $ISO_PATH
  cp $KS_FILE_NAME $ISO_PATH
  # 修改grub.cfg文件
  update_grub_cfg
  # 替换IP信息
  sed -i "s/NETWORK_IP/$NETWORK_IP/g" "$ISO_PATH/$KS_FILE_NAME"
  # 替换ks文件中安装操作系统盘
  sed -i "s/SYSTEM_DISK/$SYSTEM_DISK/g" "$ISO_PATH/$KS_FILE_NAME"
  # 增加用户密码传输
  sed -i "s/PASSWORD/$PASSWORD/g" "$ISO_PATH/$KS_FILE_NAME"
  clear_kytuning_efibootmgr
  cp clear_kytuning_efibootmgr.sh $ISO_PATH
  # 有ifcfg-enP1p3s0f0文件才会复制
  if [ -e "ifcfg-enP1p3s0f0" ]; then
      cp ifcfg-enP1p3s0f0 "$ISO_PATH"
      sed -i "s/NETWORK_IP/$NETWORK_IP/g" "$ISO_PATH/ifcfg-enP1p3s0f0"
  fi
  # 创建efi引导向
  efibootmgr --create --disk /dev/$STARTUP_DISK --part 1 --loader $BOOT_EFI --label "Kytuning"
  # 使用efibootmgr -n 命令指定下次启动项
  update_efi_bootorder
  sync
  echo '---------->[info]:查看启动盘内容为：' | tee -a "$LOG_FILE"
  ls $ISO_PATH | tee -a "$LOG_FILE"
  echo '<----------' | tee -a "$LOG_FILE"
  # todo 调试保留处，正式部署后删除。
#  reboot
  echo '===============[info]:自动安装脚本运行结束，结束时间：'$(date) | tee -a "$LOG_FILE"
}

main