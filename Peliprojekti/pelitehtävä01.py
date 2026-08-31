nimi = input("Mikä on nimesi?: ")
ika = int(input("Kuinka vanha olet?: "))


while ika < 12:
    print(f"Olet liian nuori, peli sulkeutuu.")
    break

else:
    print(f"Terve {nimi}! Olet {ika} vuotias.\n")

    valikko = (input("Mitä haluat tehdä? (A) kääntyä vasemmalle tai (D) kääntyä oikealle. "))
    while valikko != "Lopeta":
        if valikko == A:
            print("Jee! Aloitetaan peli.\n")
            print(f"Päävalikko:\n""A - Aloita peli!\n""B - Asetukset.\n")
            
        elif valikko == 2:
            print("Avataan asetukset.\n")
            print(f"Päävalikko:\n""A - Aloita peli!\n""B - Asetukset.\n")
    else:
        print("Lopetetaan.")
        