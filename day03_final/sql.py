# Author: ray.zhang
# -*- coding:utf-8 -*-

'''
有以下员工信息表

1,ray zhang,22,13651054608,IT,2013-04-01
2,jack,23,13333333333,HR,2017-06-10
3,bike Li,10,13651054608,Sale,2014-05-20
4,erav,47,13444444444,IT,2012-01-12
5,egon,33,13567890123,HR,2016-11-22

当然此表你在文件存储时可以这样表示
现需要对这个员工信息文件，实现增删改查操作

可进行模糊查询，语法至少支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数 
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
'''


def mysql_input(inf):
    info_action=inf.split(' ')[0]

    act_moth = {
        'select':mysql_select,
        'insert':mysql_insert,
        'delete':mysql_delete,
        'update':mysql_update
    }
    if info_action in act_moth:
        action = act_moth[info_action](inf.split(' '))
    else:
        print("input act_moth error!!plz input try!!!")
    pass


def mysql_select(action):
    #print("action: %s" %action)            #打印格式化后的列表。

    d = {
        'select':[],
        'from':[],
        'where':[],
        'limit':[]
    }
    for item in action:
        if item in d:
            key = item
        elif item not in d:
            d[key].append(item)
    #print("new dict: %s" %d)                 #打印最新生成的字典，带列表
    #print(d['where'])                        #列表要格式化 ['id', '>3', 'and', 'id', '<', '8']
    chars = ''
    d1=[]
    if d.get('where'):                 #['id', '>3', 'and', 'id', '<', '8'] ---->['id>3', 'and', 'id<8']
        for i in d['where']:
            if len(i) == 0:
                continue
            if i == 'and':
                if len(chars) != 0:
                    d1.append(chars)
                    d1.append(i)
                    chars = ''
            else:
                chars += i
               # print(chars)
        else:
            d1.append(chars)                #把最后的chars append进去列表里
    d['where'] = d1
    print("new full dict: %s" % d)                  #整合成全新的字典 包含了列表。
    #['id>3', 'and', 'id<8']  ------> ['id','>',3', 'and', 'id','<',8']
    
    pass

    pass
def mysql_insert(action):
    print(action)
    pass
def mysql_delete(action):
    print(action)
    pass
def mysql_update(action):
    print(action)
    pass

def mysql_action(moth):
    pass

while True:
    info = input("Plz input sql >>:").strip()
    if info.__len__() == 0:
        continue
    elif info == 'exit' or info == 'quit':
        break
    else:
        sql_input = mysql_input(info)
        #mysql_action(info)