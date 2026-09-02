nimi = input("Mikä on nimesi?: ")
ika = int(input("Kuinka vanha olet?: "))


if ika < 12:
    print(f"Olet liian nuori, peli sulkeutuu.")

else:
    print(f"Terve {nimi}! Olet {ika} vuotias.\n")

    valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) kääntyä vasemmalle\n(D) kääntyä oikealle.\n"))
    while valikko != "Lopeta":
        if valikko == "A":
            print("Käännyit vasemmalle ja löysit miekan!\n")
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) kääntyä vasemmalle\n(D) kääntyä oikealle.\n"))

        elif valikko == "D":
            print("Käännyit oikealle ja löysit avaimen!\n")
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) kääntyä vasemmalle\n(D) kääntyä oikealle.\n"))
    
    print("Lopetetaan peli.")
        