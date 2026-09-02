luvut = []

luku = input("Anna kokonaisluku: ")

'''while luku != "":
    luku = (input("Anna kokonaisluku: "))

    for luku in luvut:
        if luku > 100:
            luvut.append(luku)
            print(luku)'''


while luku != "":
    luku = int(luku)
    if luku in luvut:
        print("oli jo")
    elif luku not in luvut:
        luvut.append(luku)
    else:
        ("virhe")
    luku = input("Anna kokonaisluku: ")

for luku in luvut:
    if luku > 100:
        print(luku)
