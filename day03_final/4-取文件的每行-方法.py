# Author: ray.zhang

with open('a.txt','r',encoding='utf-8') as f:
    l = f.readlines()
    print(l)
    for line in l:
        print(line,end='')
#  以上方式是文件所有的内容一次性都读到内存里放到一个列表里去了，在每行读取，文件大的话 会把内存撑爆


with open('a.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)

#以上方式好处是： 同一时间内存里只有文件的一行，是一行一行遍历。


l = [1,2,3,4,5]
for index in range(len(l)):
    #print(index)
    print(l[index])
#依赖下标遍历列表。


for item in l:
    print(item)

#直接遍历列表。不依赖于索引。