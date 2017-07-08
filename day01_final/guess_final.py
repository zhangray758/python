#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Zhang Lei

from random import randint   #from 模块 import 方法名

count = randint(5,10)        #随机整数
print(count)
print(type(count))    #打印为int类型
name = input("Plz input your name: ")
print("Your name is: %s:" % name)

time  = 0

while time < 3:

    num = int(input("Plz guess a num: "))
    if  num > count:
        print ("You guess too big...")

    elif num < count:
        print ("You guess too small...")

    else:
        print ("Yes, you get it...")
        break
    time += 1
