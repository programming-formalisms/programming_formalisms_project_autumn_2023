import random

def coin_toss_alex():
    coin = random.randint(1, 2)
    if coin == 1:
        print("True")
        return True
    else:
        print(False)
        return False     

coin_toss_alex()
