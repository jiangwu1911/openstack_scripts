#!/bin/sh

image_name=$1
if [ $# -lt 1 ]; then
    echo -e "Usage: $0 <image_dir>\n"
    exit 1
fi

for image in $(glance image-list | grep $image_name | awk '{print $2}'); do
    glance image-delete $image
    echo -e "Image $image deleted."
done
