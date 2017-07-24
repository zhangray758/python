# Author: ray.zhang

#需求是：有的被装饰对象是有参数的，有的是不需要参数的。
#解决方法是：让闭包函数里的参数可接受任意长度，任意格式的参数。
import time

def timmer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        stop=time.time()
        print("run time is %s" % (stop - start))
    return wrapper

@timmer            #简单写法，相当于 index=timmer(index)
def index():                   #称为被装饰的对象，同时为无参函数。
    time.sleep(2)
    print("welcome to index")
@timmer            #简单写法，相当于 home=timmer(home)
def home(name):
    print("welcomt to home page: %s"%name)

index()                #这样可直接调用。
home('erav')
