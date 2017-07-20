# Author: ray.zhang

#文件操作：

f = open('a.txt','r',encoding='utf-8')    #不写默认就是读文件 , 默认du的时候是按操作系统的编码读的，可以指定编码。
res = f.read()          #从头读到尾
print(res)
f.close()                        #每次要记住close

f = open('a.txt','r',encoding='utf-8')
print(f.readline())
print(f.readline(),end='')                        #一次读一行，因为有换行符，所以可以加个end
f.close()

f = open('a.txt','r',encoding='utf-8')
print(f.readlines())                         #把文件所有的行读出来，组成一个列表
f.close()

#另外一种方法：打开文件后自动关
with open('a.txt','r',encoding='utf-8') as f:
    rev=f.read()
    print(rev)

# 同时也可以open多个文件，如:
with open('a.txt','r',encoding='utf-8') as f,open('b.txt') as f1:
    pass

#文件写操作
f = open('b.txt','w',encoding='utf-8')    # w 的意思会直接覆盖掉原文件内容，如果文件不存在，也会创建。
f.write('11111\n22222\n333333333')
f.write('\nabc\ndef')
f.close()

f = open('b.txt','w',encoding='utf-8')
f.writelines(['a\n','b','c'])                 #也可以用wirtelines 里面列表写
f.close()


#example
#学完文件操作用py写一个tail这个命令

#将aa.txt里的ray替换成erav
# review前可以先把erav改回成ray。因为文件的修改，实际上就是重新覆盖文件。
import  os

with open('aa.txt','r',encoding='utf-8') as read_f ,\
    open('_aa.txt','w',encoding='utf-8') as write_f:
    rev = read_f.read()
    rev = rev.replace('ray','erav')                  #利用字符串的替换操作
    #print(rev)
    write_f.write(rev)             #将rev的内容写入到_aa.txt

os.remove('aa.txt')                #将原文件删掉
os.rename('_aa.txt','aa.txt')      #重命名文件到原文件，

#

