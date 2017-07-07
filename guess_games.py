#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Author: Zhang Lei

count = 0
user = "eray"

while count < 3:
    name = input("Plz guess name: ")
    if user == name:
        print("Contratulations. You got it.")
        break
    elif count == 2:
        guess = input("Do you want to guess again?\nplz input y/n\n")
        if guess == "Y" or guess == "y":
            print ("Let's go run...")    
            count = 0
            continue
        elif guess == "N" or guess =='n':
            print("Sorry,Your guess is stoped.")
            break
        else:
            print("you input error.")
            break
    else:
        print ("Sorry,You guess error.") 
    count += 1
