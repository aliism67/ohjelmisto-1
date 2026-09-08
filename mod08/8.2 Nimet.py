nimet = set()

nimi = input("Anna nimi: ")

while nimi != "":
    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
    else:
        print("Aijemmin syötetty nimi")

    nimi = input("Anna nimi: ")

for i in nimet:
    print(i)

        
