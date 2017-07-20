# Author: ray.zhang
# 执行方式： python3 test.py a.jpeg b.jpeg

import sys

print(sys.argv)         #包含了文件名本身。



if len(sys.argv) < 3:
    print("Usage: python3 test.py source.file target.file")
    exit()

print(sys.argv[1])
print(sys.argv[2])

with open(r'%s' %sys.argv[1],'rb') as c \
    ,open(r'%s' %sys.argv[2],'wb') as d:       #这里的 r 表示原生字符串。
    for line in c:
        d.write(line)