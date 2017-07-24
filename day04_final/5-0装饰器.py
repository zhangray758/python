# Author: ray.zhang

# 装饰器：
# 装饰器本身可以使任意可调用对象，被装饰的对象本身也可以是任意可调用对象。

# 1、开放封闭原则：对扩展是开放的，对修改是封闭的。

# 2、装饰它人的工具，装饰器目的是为其他人添加新功能。
#2、1 装饰器的遵循的原则：1、不修改被装饰对象的源代码， 2、不修改被调用对象的调用方式 ----重要
#2、2 装饰器的目的是：在遵循1和2原则的前提下，为其他函数添加新功能。

import  time

def index ():
    time.sleep(2)
    print("welcome to index")


index()

# 要求： 统计上面函数的运行时间。
# 第一种方法，原基础上修改。
import  time

def index ():
    start=time.time()
    time.sleep(2)
    print("welcome to index")
    stop=time.time()
    print("run time is %s" %(stop-start))


index()
# 第二种方法，使用闭包函数的方式。但是调用不符合装饰器的原则
import time

def index ():
    time.sleep(2)
    print("welcome to index")

def timmer():
    func=index
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        print("run time is %s" % (stop - start))
    return wrapper

wrapper=timmer()
wrapper()

#第三种方法，使用装饰器的方式。

def index ():
    time.sleep(2)
    print("welcome to index")

import time

def timmer():
    func=index
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        print("run time is %s" % (stop - start))
    return wrapper

index=timmer()                        #调用方式没变。
index()

#上述装饰器可以实现功能，但是我如果另外在加 home函数的运行时间呢，比如，下片。

