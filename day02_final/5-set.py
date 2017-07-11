# Author: ray.zhang


course=['linux','python','perl','go','ruby']         #取重实例
title=['python','go','java','c++']
li=[]

for i in course:
    if i in title:
        li.append(i)

print(li)

#集合 set
#作用：
# 去重，每个元素必须是不可变类型,即可hash 关系运算
# 集合内的元素唯一，默认会去重。
# 集合是无序的

#定义集合
s = {1,}
print(type(s))

s1=set('heello')    #字符去重了。
print(s1)

print('l' in s1)    #成员运算判断

#集合关系运算实例  和内置方法
s1 = {1,10,11,22}
s2 = {1,22,33}

#如下的方法记住符号既可以，
print(s1 & s2)    #取交集
print(s1.intersection(s2))
print(s1 | s2)    #取并集, 默认会去重
print(s1.union(s2))
print(s1 ^ s2)    #对称差集
print(s1.symmetric_difference(s2))
print(s1 - s2)    #求差集
print(s1.difference(s2))
print(s2 - s1)    #求差集
print(s2.difference(s1))
s1.remove(10)        #根据元素删除，值如果不存在，会报错
print(s1)
s1.discard('aaaaaa')     #根据元素删除，值如果不存在，不会报错，返回原来的值。
print(s1)

print(s1.pop())    #删除,由于无序，随机删除

#求父集
s1 = {1,2,3,4}
s2 = {1,2}
print(s1 > s2)   #判断父子集 True 和False


#explame
'''
　一.关系运算
　　有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
　　pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
　　linuxs={'wupeiqi','oldboy','gangdan'}
　　1. 求出即报名python又报名linux课程的学员名字集合
　　2. 求出所有报名的学生名字集合
　　3. 求出只报名python课程的学员名字
　　4. 求出没有同时这两门课程的学员名字集合
'''
pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
linuxs={'wupeiqi','oldboy','gangdan'}
print(pythons & linuxs)
print(pythons | linuxs)
print(pythons - linuxs)
print(pythons ^ linuxs)


#二.去重

#　　 1. 有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序

l = ['a','b',1,'a','a']

s = set(l)                 #列表转集合，集合再转列表，中间去重无序
l1 = list(s)
print(l1)

#　　 2.在上题的基础上，保存列表原来的顺序，有序
l=['a','b',1,'a','a']
l1 = []
for a in l:
    if a  not in l1:
        l1.append(a)
    elif a  in l1:
        continue
print(l1)

l=['a','b',1,'a','a']
l1=[]
se = set()             #定义空集合，注意这个定义用法
for a in l:
    if a not in se:
        se.add(a)        #这里加的会是无序，所以借助了列表的append
        l1.append(a)
print(l1)

#　　 3.去除文件中重复的行，肯定要保持文件内容的顺序不变


#　　 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序

l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]

#sss = set(l)         #因为这个列表里的元素是字典，字典是可变类型，所以不能转set
#两种方法：一：   好实现

s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)

#两种方法：二：    换另一种难的方法
#分析，因为此列表里的元素是字典，字典里的key都一样，所以只去重value就行。
ab = []
s = set()
for b in l:
    var = (b['name'],b['age'],b['sex'])

    #print(var)
    if var not in s:               #这个例子比较value即可，如果value不在的 追加列表中的某一整个元素就可以，
        s.add(var)
        ab.append(b)
print(s)
print(ab)


