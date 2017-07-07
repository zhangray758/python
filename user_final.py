#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: Zhang Lei

userdict = {"enven":111,"jack":222,"eray":333,"bike":444}
count = 0 
num = 0


while count < 3:
    username = input("What's your name? ")
    f = open("name.txt")
    date = f.readlines()
    date = ''.join(date).strip('\n')
    f.close()

    if username in date:
        print ("sorry,your account is blocked.")
        break
    else:
        if username not in userdict:
            print("no,you guess error...") 
            count += 1
            continue
        elif username in userdict:
            print("year,input success...")
       
            while num < 3: 
                passwd = input("plz input your passwd:")
                if passwd == str(userdict[username]):
                    print("Yes, congratulations to you...")
                    break
                elif num == 2:
                    print("You are locked:", username) 
                    f = open('name.txt','a+')
                    f.write(username +'\n')
                    f.close
                    break
                else:
                    print("plz input your passwd again:")
                    num += 1

            break
