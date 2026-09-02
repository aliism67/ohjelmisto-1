import random

def nopanheitto():
    return random.randint(1, 6)

luku = 0
    
while luku < 6:
        luku = nopanheitto()
        print(luku)