import random

luku =  (random.randint(1, 10))

arvaus = int(input("Arvaa luku väliltä 1 - 10: "))

while arvaus != luku:
    if arvaus == luku:
        break
    elif arvaus > luku:
        print("Luku on liian suuri, arvaa uudelleen")
        arvaus = int(input("Arvaa luku väliltä 1 - 10: "))
    elif arvaus < luku:
        print("Luku on liian pieni, arvaa uudelleen")
        arvaus = int(input("Arvaa luku väliltä 1 - 10: "))

else:
    print("Arvasit oikein!")
