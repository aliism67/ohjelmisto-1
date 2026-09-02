luku = int(input("Anna kokonaisluku: "))

if luku <= 0:
    print("Virheellinen luku!")
else:
    for i in range(0, luku + 1, 2):
        print(i)