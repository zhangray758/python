#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Author: Zhang Lei

count = 0
user = "eray"
tag = True

while tag:
    name = input("Plz guess name: ")
    if user == name:
        print("Contratulations. You got it.")
        tag = False
    elif count == 2:
        guess = input("Do you want to guess again?\nplz input y/n\n")
        while tag:
            if guess == "Y" or guess == "y":
                print ("Let's go run...")
                count = 0
                break
            elif guess == "N" or guess =='n':
                print("Sorry,Your guess is stoped.")
                tag = False
            else:
               print("you input error.")
               tag = False
    else:
        print ("Sorry,You guess error.")
        count += 1
