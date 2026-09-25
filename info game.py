import time

name = input("name: ")
OS = input("OS: ")

info = {
    "name": name,
    "os": OS
}

if OS == "" and name == "":
    print("how you dont have a name. and how you do your play without an OS???")
elif name == "":
    print("your name is... um ,and you have", info["os"])
elif OS == "":
    print("your name is", info["name"], "and how you playing this game?")
else:
    print("you name is", info["name"], "and you have", info["os"])
    


 




    






