def nayta_inventory(lista):
    for i in lista:
        print(i)

def lisaa_inventoryyn(lista, esine):
    lisaa = input("Kyllä vai ei?: ")
    if lisaa == "Kyllä":
        lista.append(esine)
        print("Miekka lisätty inventaarioon")

def nayta_health(elamapisteet):
    print(elamapisteet)

def aloita_peli():
    print("Aloitetaan peli!\n")
    print("Edessäsi on risteys. Voit kääntyä (A) vasemmalle tai (D) oikealle.\n")
    valinta = input("valitse A tai D: ")
    if valinta == "A":
        print("Käännyit vasemmalle ja löysit miekan! Otetaanko miekka mukaan?")
        lisaa_inventoryyn(lista)
    elif valinta == "D":
        print("Käännyit oikealle ja löysin omenan! Otetaanko omena mukaan? ")

max_elamapisteet = 10
elamapisteet = 10
lista = []

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
            nayta_inventory(lista)
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))

        elif valikko == "C":
            ## Näytä elämäpisteet eli health funktiota käyttäen
            nayta_health(elamapisteet)
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))

        elif valikko == "A":
            aloita_peli()
            ## Tästä alkaa virallinen peli

        else:
            print("Virheellinen syöte, yritä uudelleen\n")
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa elämäpisteet\n"))
    
    print("Lopetetaan peli.")
        