# Author: ray.zhang

#函数嵌套调用：在调用一个函数的过程中，又调用了其他函数。

def bar():
    print("from bar")
def foo():
    print("from foo")
    bar()

foo()

print(max(max(1,5),max(6,7)))

#函数的嵌套定义：在一个函数的内部，又定义另外一个函数。

def f1():
    x = 1
    def f2():
        print("from f2")
    print(x)       # 变量值
    print(f2)      # 函数内存地址
    f2()           # 调用f2
f1()
#print(x)           #报错了。