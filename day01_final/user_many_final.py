#!/usr/bin/env python3

dict = {
    'jack':{'pass':123,'count':0},
    'eray':{'pass':456,'count':0},
    'bike':{'pass':789,'count':0}
}


name = input ("plz input your name: ")
print (dict[name]['pass'])

if name not in dict:
    print ("Sorry,you input error.")
    exit()
elif name in dict :
    print ("Ok,you input success.")

    while dict[name]['count'] < 3: 

        pas = int(input("plz input your passwd: "))

        if pas == dict[name]['pass']:
            print ("Congratulation to you.")
            dict[name]['count'] = 3 
        else:
            dict[name]['count'] += 1
