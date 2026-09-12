import time

tries = 0

print("hello!!")
time.sleep(1)

while True:
    while tries < 3:
        p = input("put your password: ")

        if p == "0000":
            while True:
                input("no comands> ")
        else:
            tries = tries + 1
            print(f"wrong.{3 - tries} tries left")
    else:
        print("wait 60 seconds")
        time.sleep(60)
        tries = 0

                