# Author: ray.zhang

#列表 有序 可变数据类型
my_firends=['jack','eray','egon','chua','sfan','eray']
print(type(my_firends))

print(my_firends[2:5:2])         #切片

my_firends.append('swei')
my_firends.pop()    #默认从后面删除      pop删除
my_firends.pop(2)   #输入数字按索引删除
print(my_firends)

my_firends.remove('chua')    #remove删除  按值删除
print(my_firends)


print(my_firends.__len__())     #统计元素个数
print(len(my_firends))

print('eray' in my_firends)    #成员运算判断

l=my_firends.copy()        #copy用法
print(l)

print(my_firends.count('eray'))   #count用法

my_firends.extend(['aa','bb','bb'])   #extend用户
print(my_firends)

print(my_firends.index('eray'))     #index(self, value, start=None, stop=None):  从左到右，找到一个就完了。

my_firends.reverse()       #re反转verse 注意先反转后print
print(my_firends)

l = [3,-1,5,3]            #sort 排序，注意先排序后print
l.sort()
print(l)

my_firends.insert(1,'xye')    #insert插入
print(my_firends)



#example：
#有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
date=['eray',28,[1989,2,6]]
#print(date)
name,age,birth=date       #变量解压方式取
print(name)
print(age)
print(birth)

#队列   先进先出
fifo=[]
#入队
fifo.append('first')
fifo.append('second')
fifo.append('third')
print(fifo)
#出队
print(fifo.pop(0))
print(fifo.pop(0))
print(fifo.pop(0))
print(fifo)

#堆栈  先进后出
fifo.insert(0,'first')
fifo.insert(0,'serond')
fifo.insert(0,'third')
print(fifo)
print(fifo.pop())
print(fifo.pop())
print(fifo.pop())
print(fifo)


#example
#取出['third', 'serond', 'first']  列表中，每个元素。
print()            #打印个空行
l = ['third', 'serond', 'first']
for i in l:
    print(i)