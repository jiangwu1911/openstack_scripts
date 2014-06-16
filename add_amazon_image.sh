#!/bin/sh

image_dir=$1
if [ $# -lt 1 ]; then
    echo -e "Usage: $0 <image_dir>\n"
    exit 1
fi

image_file=$(ls $image_dir/*.img 2>/dev/null)
ramdisk_file=$(ls $image_dir/*initrd 2>/dev/null)
kernel_file=$(ls $image_dir/*kernel 2>/dev/null)

if [ -z "$image_file" ]; then
    echo -e "Cannot find image file, quit.\n"
    exit 2
fi
if [ -z "$ramdisk_file" ]; then
    echo -e "Cannot find ramdisk file, quit.\n"
    exit 2
fi
if [ -z "$kernel_file" ]; then
    echo -e "Cannot find kernel file, quit.\n"
    exit 2
fi

ramdisk_id=$(glance add name="${image_dir}_ramdisk" is_public=true container_format=ari disk_format=ari < $ramdisk_file | cut -d: -f 2 | sed 's/^ \+//')
kernel_id=$(glance add name="${image_dir}_kernel" is_public=true container_format=aki disk_format=aki < $kernel_file | cut -d: -f 2 | sed 's/^ \+//')
glance add name="${image_dir}_image" is_public=true container_format=ami disk_format=ami kernel_id=$kernel_id ramdisk_id=$ramdisk_id < $image_file
