import random
import time

while True:
    passwd = random.randint(1000, 999999)     
    
    print("\033[92mpassword: [\033[0m", passwd, "\033[92m]\033[0m")
    time.sleep(0.1)
