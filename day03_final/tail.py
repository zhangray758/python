# Author: ray.zhang

import sys
import time

if len(sys.argv) <3:
    print("Usage: python3 tail.py -f access.log")
    exit()

with open(r'%s'%sys.argv[2],'rb') as f:          #使用seek 必须是b模式
    f.seek(0,2)                             #跳到最后面
    while True:
        line = f.readline()
        if line:                           #自带布尔值
            print(line.decode('utf-8'),end='')        #注意end的含义
        else:
            time.sleep(0.2)
