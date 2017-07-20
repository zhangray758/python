# Author: ray.zhang

#有参函数：传参   先定义后调用
def my_max(x,y):
    if x > y:
        print(x)
    elif x  < y:
        print(y)

my_max(2,3)           #直接打印结果
res=my_max(2,3)       #先执行my_max 打印操作出结果，后赋值。
print(res)            # 没有return，结果为NONE，等同于return None

#因此怎么样能够拿到函数的结果呢？用return，上面的可以改写为：
def m_max(x,y):
    if x > y:
        return x
    elif x < y:
        return y

m_max(4,5)          #这个是没有结果的。
res=m_max(4,5)
print(res)          #这样子结果就可以正确打印了。

#通常情况下，有参函数都要有个返回值，return。
#加上return语法，return为函数的结果。比如：
def foo():
    print('++++++++')
    return 123              #函数内部可以有多个，但只能执行一次return，整个函数就结束了。
    print('++++++++')
    return 456
    print('+++++++=')

foo()            #到这的话只返回return前面的结果
result = foo()    #如果给函数结果赋值的话,那么return返回的内容会赋值给变量result
print(result)     #运行看结果。

#return的返回值没有类型限制，可以返回列表、字典、字符串等。
#如： return value1,value2,vlues3
#结果为元组： (value1,value2,value3)

#空函数
def bar():
    pass            #占位 定义函数的方法 先空位，定义结构。然后理清思路填充代码。

#函数调用的多种表达形式：
m_max(11,22)        #调用函数的语句形式
result=m_max(11,22)  #调用函数的语句形式
print(result)
res=m_max(33,44)*10      #调用函数的表达式语句
print(res)
max=m_max(m_max(33,44),55)        #函数调用可以当做另外一个函数的参数。
print(max)