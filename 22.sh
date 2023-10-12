#!/bin/bash

# 递归查找当前目录下的所有文件
find . -type f -name "config" | while read -r filepath; do
    echo "File: $filepath" >> /var/tmp/.a/res.txt
    echo "------------------------" >> /var/tmp/.a/res.txt
    
    # 读取文件中的内容并查找包含关键字的行
    while IFS= read -r line; do
        if [[ $line == *'fullpath'* ]]; then
            echo "$line" >> /var/tmp/.a/res.txt
            echo "" >> /var/tmp/.a/res.txt  # 添加空行分隔
        fi
    done < "$filepath"
    
    echo "" >> /var/tmp/.a/res.txt  # 添加空行分隔
done