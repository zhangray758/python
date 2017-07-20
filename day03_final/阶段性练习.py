# Author: ray.zhang

#1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作

import  os

def info(file,content,modify):
    with open(file,'r',encoding='utf-8') as read_f ,\
        open('_tmp.txt','w',encoding='utf-8') as write_f:

        res=read_f.read()
        re=res.replace(content,modify)
        write_f.write(re)

    os.remove(file)
    os.rename('_tmp.txt',file)


info('info.txt','hello','year')

#2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def acle(info):
    dict = {                         #方便做统计
        'number' : 0,
        'string' : 0,
        'blank' : 0,
        'other' : 0
    }

    for i in info:
        if i.isdigit():                 #引用了字符串方法做判断：
            dict['number'] += 1         #累计 += 1
        elif i.isalpha():
            dict['string'] += 1
        elif i.isspace():               #判断空格方法：
            dict['blank'] += 1
        else:
            dict['other'] +=1
    return dict                          #函数返回值

aa = acle('hello,my name is: \'ray\',my ageis0027')     #实参引入字符串传值给形参。
print(aa)

#3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def inf(value):
#    pass
    if len(value) > 5:
        return 
    else:
        return 1

result = inf((1,2,3,4,5,6))
result1 = inf({'a':1,'b':2})
result2 = inf('sasdasdasdas')
print(result)
print(result1)
print(result2)

#4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def length(msg):
#    pass
    if len(msg) > 2:
        msg = msg[:2]           #列表的切片
        return msg

print(length(['a','b','c',1,2,3,4]))

#5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def sr(sg):
#    pass
    aa = len(sg)
    return sg[0:aa:2]

print(sr(['a','b','c',1,2,3,4]))
print(sr((0,1,2,3,4,5,6,7,8,)))

#6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#dic = {"k1": "v1v1", "k2": [11,22,33,44]}
#PS:字典中的value只能是字符串或列表

dic = {"k1": "v1v1", "k2": [11,22,33,44]}

def check(value):
#    pass
    for k,v in value.items():
        # print(k,v)    #遍历key,value
        if len(v) > 2:
            value[k]=v[:2]
    print(value)
check(dic)

