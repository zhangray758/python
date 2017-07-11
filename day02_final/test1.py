# Author: ray.zhang

d={}
d['name'] = 'jaso'
d['age'] = 42
print(d)

r=d.clear()
print(d)
print(r)





#集合add方法
s=set()
print(type(s))
s.add(123)
print(s)


#set 和list 互转
l = ['a','b',1,'a','a']

s = set(l)
l1 = list(s)
print(l1)
