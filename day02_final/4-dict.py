# Author: ray.zhang

#字典  无序，可变数据类型，但key必须是不可变类型 不可变类型也称为hash类型。
#因为不可变类型为key，所以元组也可以当做字典的key，如：
aa={'(a,b)':'c',(1,2):'d','e':'f'}            #元组作为key
print(aa['(a,b)'])
print(aa[(1,2)])

info={'name':'eray','age':18,'sex':'male'}
info['heighit'] = 170      #增加个key:value
print(info)
info['name']='erav'     #修改key对应的value
print(info)

#删除 pop   语法： pop(self, k: _KT) 两个参数
info.pop('age')
print(info)
print(info.pop('asdasdasdasdasd','None'))      #如果要删除的key参数不存在,返回None

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

print(dict([('name','eray'),('age',18),('sex','male')]))     #创建字典。


#update


#setdefault



