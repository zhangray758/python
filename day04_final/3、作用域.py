# Author: ray.zhang

#作用域：作用的范围，分为两种
#全局作用域： 全局存活，全局有效，  名字定义完了之后在任何位置都能访问的到。flobals()  查看全局作用域的名字
#如：内置 和全局
x=1
def f1():
    def f2():
        def f3():
            def f4():
                print(x)
                print(max)         #这里的x max就是全局范围的名字，包含在了内置 和全局的名称空间里。
            f4()
        f3()
    f2()
f1()
#局部作用域：临时存活，只在局部有效。如函数内。 局部有效：locals()  查看局部作用域的名字
def x1():
    def x2():pass
    x=2
    print(x)            # 这里的x 就是局部范围的名字。
    print(locals())     # 答案有x=2 和x2()
    print(globals())    # 在局部可以查看到全局的名字。
    x2()
x1()
print(locals() is globals())         #答案为True: 在外部全局看的话，全局的局部仍然是全局。


print(globals()['__builtins__'])   #查看内置作用域的名字 __builtins__
print(dir(globals()['__builtins__']))   # dir查看某一对象下面都有哪些内置的方法。


#global nonlocal   掌握，实际中尽量不要这么用。

x=1
def f1():
    x=2
f1()         #调用完了就结束了。
print(x)     #答案是1

x=1
def f1():
    global x      #明确的声明 x为全局的变量，不管多少层。
    x=2           #针对全局的不可变类型，直接修改，不会生效。
    def f2():
        x=3
    f2()
f1()
print(x)     #答案是2

l = []
def f2():
    l.append('f2')        #针对全局的可变类型，可直接修改，会生效
f2()
print(l)

x=0
def f1():
    x=1
    def f2():
        x=2
        def f3():
            global x          #x 全局声明变量 修改了全局
            x=3
        f3()
        print(x)             #x优先从当前位置找，所以答案是2
    f2()
f1()

def f1():
    x=1
    def f2():
        x=2
        def f3():
            nonlocal x          #nonlocal改的是函数内部正上方的那一层，只在函数内部有效，所以答案为3
            x=3
        f3()
        print(x)
    f2()
f1()

def f1():
    x=1
    def f2():
        #x=2
        def f3():
            nonlocal x          #nonlocal改的是函数内部正上方的那一层，由于正上方一层没有定义x，所以在上上一层作用，只在函数内部有效，所以答案为3
            x=3
        f3()
        #print(x)
    f2()
    print(x)
f1()

'''
x=0
def f1():
    #x=1
    def f2():
        #x=2
        def f3():
            nonlocal x          #nonlocal 只在函数内部有效，所以答案报错了。
            x=3
        f3()
        #print(x)
    f2()

f1()
print(x)
'''

#必须掌握：作用域关系，在函数定义时就已经固定，于调用位置无关。
x =1
def f1():
    def f2():
        print(x)
    return f2
func=f1()
x = 100000          #当调用f1()后直接返回了f2函数名，在当调用func()实际调用f2()时 找全局空间的x之前就已经被改了。
func()              #所以答案是100000


