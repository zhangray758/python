# Author: ray.zhang

#装饰器，
import time

def index():
    time.sleep(2)
    print("welcome to index")

def home():
    print("welcomt to home page")

def timmer(func):
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        print("run time is %s" % (stop - start))
    return wrapper

index=timmer(index)                        #调用方式没变。
home=timmer(home)

index()
home()

#另外一种写法： 遵循自上而下，先定义后调用的方式。
# @装饰器名，必须写在被装饰对象的正上方，并且是单独一行。
import time

def timmer(func):
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        print("run time is %s" % (stop - start))
    return wrapper

@timmer            #简单写法，相当于 index=timmer(index)
def index():                   #称为被装饰的对象，同时为无参函数。
    time.sleep(2)
    print("welcome to index")
@timmer            #简单写法，相当于 home=timmer(home)
def home():
    print("welcomt to home page")

index()                #这样可直接调用。
home()

#如果被装饰的对象时有参的呢， 详见下片。
