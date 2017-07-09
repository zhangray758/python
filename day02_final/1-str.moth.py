# Author: ray.zhang

#主要掌握的方法
#strip用法：   语法：strip(self, chars=None):
name = input("what's your name:").strip()   #移除两边空格
print(name)

name = "****ray.zhang****"
print(name.strip("*"))

#split 切成列表、 语法：split(self, sep=None, maxsplit=-1
user_info="root:*:0:0::/root:/bin/bash".split(":")[-2]    #取6段
print(user_info)

ngx_log="|static2.ivwen.com|GET /music/Summer.m4a HTTP/1.1|200|"   #取出状态码
status = ngx_log.split("|")[-2]
print(status)
print (ngx_log.split("|",2))     #2 代表切两次

browser="IExplorer Safri Chrome        hotfox".split()        #默认以一个或多个空格作为分隔符
print(browser)


#len 长度   语法：len(*args, **kwargs):
user = "ray.zhang"
print(len(user))      #统计长度，左边两种方法一样。
print (user.__len__())

#切片
user = "ray.zhang"
print(user[1:7:2])         #按2步长取，包含1

#replace   语法：replace(self, old, new, count=None)
print(user.replace("ay",'om'))
print(user.replace("a",'o',2))     #replace换2次

#format   语法：format(self, *args, **kwargs):
print('fruit:{}，count:{},slaes:{}'.format("apple",5,"bana"))
print('fruit:{0}，count:{1},slaes:{0}'.format("apple",5))
print('fruit:{fru}，count:{cou},slaes:{fru}'.format(fru="apple",cou=5))

#isdigit   语法isdigit(self):
mum='2356'.isdigit()    #判断整数
print(mum)
d=b'4'
print(type(d))              #为bytes类型
print(d.isdigit())          #结果为true

#join方法：join(self, iterable)
l=['egon','eray','jack','bike']              #注：列表内容必须都是字符串。比如数字是不可以的。
print(':'.join(l))           #把字符串已 : 号分割拼接到一起
print('\n'.join(l))          #把字符串已\n 分割拼接到一起



#主要熟悉方法：
user = "ray.Zhang234"
print(user.endswith('ng'))
print(user.startswith('a'))

#lower upper方法  语法：lower(self)   upper(self)
print(user.lower())        #改为小写
print(user.upper())        #改为大写

#find方法：find(self, sub, start=None, end=None)
print(user.find("a"))     #没有找到元素，结果为 -1
#index 方法： index(self, sub, start=None, end=None)
print(user.index('a'))    #没有找到元素，结果报错。

#count方法：count(self, sub, start=None, end=None):
print(user.count("a",2))    #2为位置

#center  语法：center(self, width, fillchar=None)
print(user.center(30,"#"))
#ljust   rjust用法
print(user.ljust(30,"#"))
print(user.rjust(30,"#"))
#zfill用法
print(user.zfill(30))

#expandtabs用法,语法：expandtabs(self, tabsize=8):
uu="eray\tjack"
print(uu.expandtabs(1))  #执行tab几个空格，默认是4个

#其他熟悉方法
print(user.capitalize())    #首字母大写
print(user.swapcase())       #大小写反转
print(user.title())          #每个单词的首字母大写
print(user.isalnum())        #字符串由字母和数字组成
print(user.isalpha())        #字符串只由字母组成

#其他方法：



























