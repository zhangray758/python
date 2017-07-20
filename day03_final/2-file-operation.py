# Author: ray.zhang

#文本模式下，指定数字读，读的是字符。
#为b bytes模式下时，指定数字读，读的是字节。

'''
一: read(3)：

　　1. 文件打开方式为文本模式时，代表读取3个字符
　　2. 文件打开方式为b模式时，代表读取3个字节
'''

with open('a.txt','r',encoding='utf-8') as f:
    print(f.read(4))                           #读了4个字符，因为空行还是一个字符\n

f = open('a.txt','r',encoding='utf-8')
print(f.read(4))

with open('a.txt','rb') as f:
    print(f.read(4).decode('utf-8'))                           #读了4个字节，因为空行还是一个字符\n

'''
二: 其余的文件内光标移动都是以字节为单位如seek，tell，truncate
注意：
　　1. seek有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的


'''
#seek 控制光标移动。  tell 光标所在的位置。
# 0 模式可以在文本模式或b模式下使用。
with open('a.txt','r',encoding='utf-8') as f:
    print(f.read())
    f.seek(0)                    #光标移到文件开头
    print(f.read())              #第二次没有内容，是因为第一次已经全部读完，所以中间用了seek，从头开始读出来。
    f.seek(4,0)                  #光标开头处作为参照物，往后移4个字节，开始读,   3个字节等于1个汉字
    print(f.tell())              #打印光标位置
    print(f.read())
f.close()

# 1，2模式必须在b模式下使用。
with open('a.txt','r',encoding='utf-8') as f:
    print(f.read(4))              #开头读4个字符
    print(f.tell())             #第10个字节处
#    f.seek(2,1)                 #1为模式， 1为当前位置，往后移2个字节处。但是报错了，因为1,2模式需要在b模式下才可以运行。


with open('a.txt','rb') as f:
    print(f.read(4))           #开头读4个字符
    print(f.tell())            #第10个字节处
    f.seek(3,1)                #以相对位置往后移3个字节
    print(f.read(7).decode('utf-8'))          # 读取后面的7个字节。并decode

# 2 模式直接跳转到末尾
with open('a.txt','rb') as f:
    f.seek(-5,2)                #2 模式直接跳转到末尾
    print(f.read())



#example
#基于seek 实现tail -f 功能：
#详见tail.py 文件内容   #这边联合一个打印单行内容的脚本，以验证tail.py 脚本、

with open('access.log','a+',encoding='utf-8') as f:
    f.write('111\n')
    #f.seek(0)
    print(f.read())

# truncate  截断，把文件内容截断。以b模式打开
# 只保留截断前面的内容，其他的都不要，并且文件会被修改成截断前的内容
#  truncate是截断文件，所以文件的打开方式必须可写，但是不能用w或w+等方式打开，因为那样直接清空文件了，
#  所以truncate要在r+或a或a+等模式下测试效果。

with open('truncate','a+',encoding='utf-8') as f:
    f.truncate(9)
    print(f.read())


