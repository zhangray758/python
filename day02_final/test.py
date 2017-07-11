# Author: ray.zhang

info_dic={}.fromkeys(['name','age','sex'],'eray')
print(info_dic)

aa=dict(name='aa',age=18,fav='bask')
print(aa)

bb={'a':1,'b':2,'fav':'shuai'}
aa.update(bb)
print(aa)


x={}
y={}

#1
x['name'] = "eray"
y = x
x={}
print(x)
print(y)                  #使用x={}置空后y的值还存在{'key':'value'}

#2
x['name'] = "eray"
y = x
x=x.clear()
print(x)
print(y)                 #使用x.clear后，y的值也被清空了。
