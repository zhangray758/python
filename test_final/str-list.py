# Author: ray.zhang

number = 32
list=["jack",[11,22,number],'bike']    #引用变量
print(list)

list[1][1]=list[2]        #改变赋值
print(list)
print(list * 3)             #列表 * 3

print(list + ["aa","bb","cc"])        #填充列表 加到列表里
print(list , ["aa","bb","cc"])        #列表与列表用 ，号隔开;结果应该不是列表了。那是什么呢？

num=[10,9,8,7,6,5]
num[0] = num[1] - 3       #计算并赋值
print(num)

index = 3
num.insert(index,"aa")    #insert方法插入，位置用变量方式。
print (num)

for i in range(5):    #打印每个数字
    print(i)

for i in range(0,5,2):    #每隔2 打印个数字，结果包含0.
    print(i)

#numbers = list(range(5))    #py3这么生成列表有问题。
#print(numbers)

print (range(20) ==range(0,20))    #两个是一样的
True

#如下是将列表中的每个元素取出来。
world = ["hello","world","jack","bike"]
count = 0
max_index = len(world) -1    #len长度-1

while count <= max_index:
    print(world[count] + "!")
    count += 1
print()                   #打印空行
for n in world:
    print(n + "!")
