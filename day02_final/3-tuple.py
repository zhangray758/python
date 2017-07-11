# Author: ray.zhang

#元组不可变，主要用来读

fruits=('apple','orange','banane','pear','orange')      #定义tuple
print(type(fruits))

fruits.add('apple')

print(fruits[1:4:2])    #切片后 也为元组

print('pear' in fruits)   #成员

print(fruits.index('banane'))   #index

num=fruits.count('orange')       #count
print(num)

print(len(fruits))          #len 长度
print(fruits.__len__())


#example
#实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　

msg_dic={
    'apple':10,
    'tesla':100000,
    'mac':3000,
    'lenovo':30000,
    'chicken':10
}
cars=[]
print(msg_dic)        #打印字典
for key in msg_dic:
    print('\033[32mname:{name}\t\tprice；{price}\033[0m'.format(name=key,price=msg_dic[key]))

while True:
    things = input("Plz input your things >> : ").strip()
    print(things)
    if len(things) == 0 or things not in msg_dic:
        continue
    elif things in msg_dic:
        count = input("plz input things's counts again >>:")
        if count.isdigit():
            count = int(count)
            price = count * msg_dic[things]
            cars.append((things,count,price))           #往列表里追加元组
            break
print('\033[31mYear!You are going to buy something: \033[0m\033[33m%s\033[0m'% cars)

