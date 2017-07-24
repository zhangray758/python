# Author: ray.zhang

#名称空间：存放名字的地方，准确的说名称空间是存放名字与变量值绑定关系的地方。
# 分为三种：
#内置名称空间：在python解释器启动时产生,存放一些python内置的名字。
# 如：len max print sum
#全局名称空间：在执行文件时产生，存放文件级别定义的名字。
#如：
'''
x = 2
def func():
    y = 2
class Foo:
    pass
if x == 1:
    z = 3
    '''


#局部名称空间：在执行文件的过程中，如果调用了函数，则会产生该函数的局部名称空间，一个函数会产生一个局部空间。
#用来存放该函数内定义的名字。该名字在函数调用时生效，在函数调用结束后失效。


#加载顺序： 内置------->全局--------->局部
#查找顺讯： 局部------->全局--------->内置
'''
max = 1
def foo():
    max = 2
    print(max)
foo()                  #结果：打印2，局部优先级高
'''

'''
max = 1
def foo():
    #max = 2          #结果：打印1，局部没有向上，全局
    print(max)
foo()
'''

'''
#max = 1
def foo():
    #max = 2          #结果：打印<built-in function max>，内置
    print(max)
foo()
'''

x=0
def f1():
   # x = 1
    def f2():
     #   x = 2
        def f3():
         #   x = 3
            def f4():
          #      x = 4
                print(x)
            f4()
        f3()
    f2()

f1()                        #该嵌套函数执行后结果为 0

def f1():
    print("hello")

def f1():
    print("world")
f1()                       #结果为world
