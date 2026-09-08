lentoasemat = {}

syote = int(input("Haluatko syöttää (1) uuden lentoaseman, (2) hakea jo syötetyn lentoaseman vai (3) lopettaa?: "))

while syote != 3:
    if syote == 1:
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
        syote = int(input("Haluatko syöttää (1) uuden lentoaseman, (2) hakea jo syötetyn lentoaseman vai (3) lopettaa?: "))
    elif syote == 2:
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        if koodi in lentoasemat:
            print(f"Koodin {koodi} lentoaseman nimi on {lentoasemat[koodi]}")
            syote = int(input("Haluatko syöttää (1) uuden lentoaseman, (2) hakea jo syötetyn lentoaseman vai (3) lopettaa?: "))

    
