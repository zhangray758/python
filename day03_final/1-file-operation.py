# Author: ray.zhang

# 如下文本模式 使用 r+ w+ a+ 可以在读或写或追加的时候 可以在写，在读或追加的时候读
# r+ 读文本模式，文件不存在，则报错；
f = open('a.txt','r+',encoding='utf-8')
#print(f.readlines())         # readlines 以列表的方式读出，结果为列表。
print(f.read())              #两种打印方式。直接print
date = f.read()
print(date)
print(f.readable())          #判断是否可读，结果是True 或False

f.close()
#为什么结果只打印了一个呢。
# 因为文件read 读直接读全部内容，读完后就结束了。

# w+ 写文本模式，文件不存在会新建；文件存在 清空，直接覆盖文件内容。
f = open('a.txt','w+',encoding='utf-8')
date = '''
你好啊，hello.
my name is ray,
I like study
so ...
'''
f.write(date)                 #变量方式写入文件内容。
print(f.writable())      #判断是否可写，结果是True 或False
f.writelines(['111\n','2222\n'])           # writelines 以列表的方式写入。
f.close()


# a+ 追加文本模式，文件不存在会新建，文件存在光标跳到文件末尾会追加。
f = open('a.txt','a+',encoding='utf-8')

f.write('i like python,\n and i will study be harder\n')
print(f.read())
f.close()

#如下是bytes模式。
# rb bytes模式，以bytes类型读取，这样是不需要指定字符编码的，因为读取到的是bytes模式，所以需要decode下。
# 通常 这种方式可用于拷贝 图片 音频 类的文件
f = open('a.txt','rb')
#print(f.read())
print(f.read().decode('utf-8'))         #为bytes类型。在decode转一下就ok。
f.close()

# wb 模式，以bytes类型写入，由于写入的是汉字，存在硬盘是bytes模式，所以需要encode下，
ff = open('aa.txt','wb')
ff.write('你好啊'.encode('utf-8'))
ff.close()

#example
#将 a.jpeg 图片 拷贝一份 为b.jpeg    #这个有个缺陷是，如果文件比较大，会比较耗内存。
with open('a.jpeg','rb') as a, \
    open('b.jpeg','wb') as b:
    b.write(a.read())

#优化方法： 可以考虑一行一行的方法：
with open('a.jpeg','rb') as c \
    ,open('c.jpeg','wb') as d:
    for line in c:
        d.write(line)

#需要实现的执行方式是： python3 copy.py a.jpeg b.jpeg  ,使用参数的方式，需要用到函数
# 执行方式： python3 test.py a.jpeg b.jpeg，详见test.py 脚本。
# import sys
#
# print(sys.argv)         #包含了文件名本身。
#
# print(sys.argv[1])
# print(sys.argv[2])
# with open(sys.argv[1],'rb') as c \
#     ,open(sys.argv[2],'wb') as d:
#     for line in c:
#         d.write(line)







