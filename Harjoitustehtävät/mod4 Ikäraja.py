ika = int(input("Kuinka vanha olet?: "))

if ika < 18:
    print(f"Sinulla on vielä {18 - ika} vuotta täysi-ikäisyyteen ja äänestysoikeuteen")
else:
    print("Saat äänestää vaaleissa")