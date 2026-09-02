luku = int(input("Anna kokonaisluku: "))

while luku > 0:
    if luku % 2 == 0:
        print("Luku on parillinen")
        luku = int(input("Anna uusi kokonaisluku: "))
    elif luku % 2 != 0:
        print("luku ei ole parillinen")
        luku = int(input("Anna uusi kokonaisluku: "))
else:
    print("Virhe")
