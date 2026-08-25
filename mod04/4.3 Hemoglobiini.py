a = input("Mikä on biologinen sukupuolesi?: ")

if a == "Nainen":
    b = float(input("Anna hemoglobiiniarvosi: "))
    if b < 117:
        print("Hemoglobiinisi on liian alhainen.")
    elif b > 175:
        print("Hemoglobiinisi on liian korkea.")
    else:
        print("Hemoglobiinisi on normaali.")
        
if a == "Mies":
    b = float(input("Anna hemoglobiiniarvosi: "))
    if b < 134:
        print("Hemoglobiinisi on liian alhainen.")
    elif b > 195:
        print("Hemoglobiinisi on liian korkea.")
    else:
        print("Hemoglobiinisi on normaali.")