import random
import time

r = input("what number do you want to be your password? 4-6: ")

while True:
    if r == "4":
        passwd = random.randint(1000, 9999)
        print("password:")
        print(passwd)
        r = input("anything else ? 4-6: ")
    elif r == "5": 
        passwd = random.randint(10000, 99999)
        print("password:")
        print(passwd)
        r = input("anything else ? 4-6: ")
    elif r == "6": 
        passwd = random.randint(100000, 999999)
        print("password:")
        print(passwd)
        r = input("anything else ? 4-6: ") 
    else:
        print("nothing")	
        r = input("anything else ? 4-6: ") 

