'''def inventory(tavarat):

def health(elamapisteet):


max_elamapisteet = 10
tavarat = []'''

nimi = input("Mikä on nimesi?: ")
ika = int(input("Kuinka vanha olet?: "))


if ika < 12:
    print(f"Olet liian nuori, peli sulkeutuu.")

else:
    print(f"Terve {nimi}! Olet {ika} vuotias.\n")

    valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))
    while valikko != "Lopeta":
        if valikko == "B":
            ## Näytä inventaario eli tavara lista funktiota käyttäen
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))

        elif valikko == "C":
            ## Näytä elämäpisteet eli health funktiota käyttäen
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))

        elif valikko == "A":
            print("Aloitetaan peli!\n")
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) kääntyä vasemmalle\n(D) kääntyä oikealle\n(W) Jatkaa suoraan\n"))
            ## Tästä alkaa virallinen peli

        else:
            print("Virheellinen syöte, yritä uudelleen\n")
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))
    
    print("Lopetetaan peli.")
        