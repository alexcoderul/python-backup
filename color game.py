import time

color = input("what color you like ? green, red, yellow, or blue ?: ")

while True:
    if color == "green":
        print("\033[H\033[J ", end="")
        color = input("\033[92mgreen choosen, anything else ?: \033[0m")
    elif color == "red":
        print("\033[H\033[J ", end="")
        color = input("\033[91mred choosen, anything else ?: \033[0m")
    elif color == "yellow":
        print("\033[H\033[J ", end="")
        color = input("\033[93myellow choosen, anything else ?: \033[0m")
    elif color == "blue":
        print("\033[H\033[J ", end="")
        color = input("\033[94mblue choosen, anything else ?: \033[0m")
    elif color == "exit":
        print("\033[H\033[J ", end="")
        print("goodbye")
        time.sleep(5)
        break
    else:
        print("\033[H\033[J ", end="")
        color = input("this color those not exist in the game, anything else?: ")
