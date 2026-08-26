luku = float(input("Anna tuumat: "))

while luku >= 0:
    if luku < 0:
        break
    print(f"{luku} tuumaa on {luku * 2.54} senttimetriä")
    luku = float(input("Anna tuumat: "))