# Author: ray.zhang

#可变长参数：指的是实参的个数可变，不固定；
#实参无非位置参数和关键字参数两种；
#形参必须要两种机制来分别处理按照位置定义的实参溢出的情况 *
#跟按照关键字定义的实参溢出的情况  **
def foo(x,y,*args):           #args=(3, 4, 5, 6, 7)
    print(x)
    print(y)
    print(args)         #元组

foo(1,2,3,4,5,6,7)     #按位置多出来的位置参数存成元组的形式，赋值给args。
foo(1,2)               #如果只有2个的话 那args为空元组

#扩展用法：
def foo(x,y=1,*args):           #
    print(x)
    print(y)
    print(args)

foo(1,*(3,4,5,6,7))       #在实参里只要碰到* 先打散。可以拆成 foo(1,2,3,4,5,6,7),所以y为3，后面的为args 元组


def var(x,y,**kwargs):          #kwargs={'c': 3, 'd': 4, 'e': 5, 'f': 6}
    print(x)
    print(y)
    print(kwargs)       #字典

var(1,2,c=3,d=4,e=5,f=6)       #按关键字多出来的实参数会存成字典的形式，赋值给kwargs。

#扩展用法：
def var(x,y,**kwargs):
    print(x)
    print(y)
    print(kwargs)

var(1,**{'f':6,'y':5,'c':3,'d':5})     #在实参级别，可以先把** 打散，拆成var(1,2,c=3,d=4,y=5,f=6) ，后调用。
var(**{'x':1,'y':2})             #先拆开打散 后对应的值 var(x=1,y=2) 所以可变长参数就为空字典了 {}


def main(x,*args,**kwargs):      #形参也应该是先位置，后关键字。
    print(x)
    print(args)
    print(kwargs)

main(1,2,3,4,5,b=6,c=7)       # x对应1，    2，3，4，5对应args  b=6,c=7对应kwargs



#命名关键字参数：必须是被以关键字实参的形式传递。
def foo(*args,x):
    print(x)
    print(args)

foo(1,2,3,4,5,6,x=111)      #注意语法，关键字参数要放到位置参数后面。



