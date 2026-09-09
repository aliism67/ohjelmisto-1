def nayta_inventory(lista):
        if len(lista) == 0:
            print("Sinulla ei ole vielä mitään mukana :(\n")
        else:
            for i in lista:
                print("Sinulla on mukana seuraavat esineet: ")
                print(i)

def lisaa_kapy_inventoryyn(lista, kapy):
    kapy = input("Otetaanko käpy mukaan? Kyllä vai ei?: ")
    if kapy == "Kyllä":
        lista.append("Käpy")
        print("Käpy lisätty inventaarioon")

def lisaa_omena_inventoryyn(lista, omena):
    omena = input("Otetaanko omena mukaan? Kyllä vai ei?: ")
    if omena == "Kyllä":
        lista.append("Omena")
        print("Omena lisätty inventaarioon")

def nayta_energy(energiapisteet):
    print(f"Sinulla on {energiapisteet} energiapistettä!\n")

## Ensimmäinen tehtävä
def aloita_peli():
    print("Aloitetaan peli!\n")
    print("Edessäsi on risteys. Voit kääntyä (A) vasemmalle tai (D) oikealle.\n")
    valinta = input("valitse A tai D: ")
    if valinta == "A":
        print("Käännyit vasemmalle ja löysit kävyn!")
        lisaa_kapy_inventoryyn(lista, "Käpy")
    elif valinta == "D":
        print("Käännyit oikealle ja löysin omenan!")
        lisaa_omena_inventoryyn(lista, "Omena")

# def seuraava_vaihe():


max_energiapisteet = 10
energiapisteet = 10
lista = []

## Ensimmäinen printti
nimi = input("Mikä on nimesi?: ")
ika = int(input("Kuinka vanha olet?: "))


if ika < 12:
    print(f"Olet liian nuori, peli sulkeutuu.")

else:
    print(f"Terve {nimi}! Olet {ika} vuotias.\n")

    ## Aloitus valikko
    valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa energiapisteet\n"))

    while valikko != "Lopeta":
        if valikko == "B":
            ## Näytä inventaario eli tavara lista funktiota käyttäen
            nayta_inventory(lista)
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa energiapisteet\n"))

        elif valikko == "C":
            ## Näytä elämäpisteet eli health funktiota käyttäen
            nayta_energy(energiapisteet)
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa energiapisteet\n"))

        elif valikko == "A":
            aloita_peli()
            ## Tästä alkaa virallinen peli

        else:
            print("Virheellinen syöte, yritä uudelleen\n")
            valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa energiapisteet\n"))
    
    print("Lopetetaan peli.")
        