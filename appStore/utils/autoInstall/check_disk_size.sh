#!/bin/bash
disk_name=/dev/$(df -lh | grep /boot/efi | awk '{print substr($1,6,3)}')
sizes=()

# 获取所有设备的大小
for i in $disk_name*; do
  size=$(lsblk -b -o SIZE -n -d $i)
  sizes+=($size)
done

# 计算第一个数据减去剩下所有数据的总和
first_size=${sizes[0]}
sum=0
for ((i=1; i<${#sizes[@]}; i++)); do
  ((sum += sizes[i]))
done
result=$((first_size - sum))

result=$(expr $result / 1024 / 1024 / 1024)
echo $result
