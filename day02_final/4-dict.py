# Author: ray.zhang

#字典  无序，可变数据类型，但key必须是不可变类型 不可变类型也称为hash类型。
#因为不可变类型为key，所以元组也可以当做字典的key，如：
aa={'(a,b)':'c',(1,2):'d','e':'f'}            #元组作为key
print(aa['(a,b)'])
print(aa[(1,2)])

info={'name':'eray','age':18,'sex':'male','fav':'basketball'}
info['heighit'] = 170      #增加个key:value
print(info)
info['name']='erav'     #修改key对应的value
print(info)

#删除 pop   语法： pop(self, k: _KT) 两个参数
info.pop('age')
print(info)
print(info.pop('asdasdasdasdasd','None'))      #如果要删除的key参数不存在,返回None

del info['fav']    #删除元素。
print(info)

#get  get(self, k: _KT)
print(info.get('name'))

print(info.get('asdasdasdasdadsd'))    #如果要获取的key参数不存在,返回None
print(info.get('asdasdasdasdadsd','not key'))    #如果要获取的key参数不存在,返回自定义
#print(info['asasdasdasd'])       #跟上面两种不存在的key参数对比下效果。这个会报错。


#popitem
print(info.popitem())   #无序随机删除一对键值对，并打印出来要删除的键值对,而且返回的是元组类型
print(info)

# 打印字典里的所有keys  或 所有values
print(info.keys(),type(info.keys()))         #可以看下type类型
print(info.values(),type(info.values()))     #可以看下type类型
for value in info.values():        #遍历字典里的value
    print(value)

#item  语法：items(self)
print(info.items())       #生成 包含多个元组(key,value)的列表
for key,value in info.items():       #取出key，value
    print(key,value)

#再如例子，通过item直接取出key，value
msg_dic={
    'apple':10,
    'tesla':100000,
    'mac':3000,
    'lenovo':30000,
    'chicken':10
}

for x,y in msg_dic.items():
    print(x,y)

info.clear()    #清空字典
print(info)

#fromkeys用法：语法：fromkeys(seq,value):
info_dic={}.fromkeys(['name','age','sex'],'eray')    #快速创建一个字典，注意每个key对应的value都一样。不能对应多个值
print(info_dic)

dic=dict(name='eray',age=18,sex='male')     #在创建一个字典。
print(dic)

print(dict([('name','eray'),('age',18),('sex','male')]))     #创建字典。需要在熟悉，注意语法。


#update  语法：update(self, E=None, **F):
dic_update={'fav':'basketball','sex':'fomale','height':185}
dic.update(dic_update)
print(dic)                        #update直接更新 原dic的内容 和补充原dic内容


#setdefault
d={}
print(d)
d["name"] = 'eray'
d['age'] = 18
d['sex'] = 'male'
d['fav'] = []                  #字典里定义个列表，然后append追加进去。
#d['fav'].append('play  basketball')
#d['fav'].append('play football')
#print(d)

d.setdefault('fav',[]).append('play football')        #可以对比下上面的方法，效果是一样的。
d.setdefault('fav',[]).append('play basketball')
print(d)

#删除字典
del d
#print(d)            #打印后就报错了。

#example
#1、字典的格式化操作：
phonebook = {'james':'1234',"jason":'6789'}
print("james's phone numbers is %(james)s" % phonebook)       #注意%s的用法。

#2、有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中.
#即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
list=[11,22,33,44,55,66,77,88,99,90]
d={}.fromkeys(['k1','k2'],'')          #采用fromkey先创建字典，
print(d)
d['k1']=[]                             #然后定义字典的key对应是个列表
d['k2']=[]

for i in list:
    if i > 66:
        d.setdefault('k1',[]).append(i)      #通过列表方法append追加。
    if i < 66:
        d.setdefault('k2',[]).append(i)

print(d)


list=[11,22,33,44,55,66,77,88,99,90]
dic={"k1":[],"k2":[]}                   #预先定义列表，然后通过列表方法append匹配追加
for item in list:
    if item > 66:
        dic['k1'].append(item)
    elif item < 66:
        dic['k2'].append(item)

print(dic)

#3、统计s='hello alex alex say hello sb sb'中每个单词的个数
#结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
s='hello alex alex say hello sb sb'

s1=s.split()
print(s1)
l={}

for word in s1:
    if word not in l:
        l[word] = 1
    elif word in l:
        l[word] += 1

print(l)













