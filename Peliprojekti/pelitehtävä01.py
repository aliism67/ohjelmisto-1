class Player:
    sijainti = Huone
    def __init__(self, nimi, tavarat, sijainti, energiapisteet, karmapisteet):
        self.nimi = nimi
        self.tavarat = tavarat
        self.sijainti = sijainti
        self.energiapisteet = energiapisteet
        self.karmapisteet = karmapisteet

    def nayta_inventory(self, tavarat):
        if len(tavarat) == 0:
            print("Sinulla ei ole vielä mitään mukana :(\n")
        else:
            print("Sinulla on mukana seuraavat esineet: ")
            for i in tavarat:
                print(f"-{i.nimi}")

    def lisaa_inventoryyn(self, esine):
        self.tavarat.append(esine)
        print(f"{esine.nimi} lisättiin inventaarioon")

    def nayta_energy(self, energiapisteet):
        print(f"Sinulla on: {energiapisteet} energiapistettä!\n")

    def nayta_karma(self, karmapisteet):
        print(f"Sinulla on: {karmapisteet} karmapistettä")

class Esine:
    def __init__(self, nimi, esine_energia):
        self.nimi = nimi
        self.esine_energia = esine_energia

class Huone:
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine

    def iso_puu(self, pelaaja):
        print("Olet Nyt vanhan omenapuun luona.\nPuusta tippuu omena ja päätät pomia sen mukaan.")
        omppu = input("Paina A näppäintä ottaaksesi omenan mukaan: ")
        if omppu == "A":
            pelaaja.lisaa_inventoryyn(omena)

energiapisteet = 10
tavarat = []

omena = Esine("Omena", 2)

aloitus_huone = Huone("Vanha puu", omena)

## Pelaajan luominen

p_nimi = input("Mikä on nimesi?: ")
ika = int(input("Kuinka vanha olet?: "))

pelaaja = Player(p_nimi, tavarat, 0, 10, 10)

if ika < 12:
    print(f"Olet liian nuori, peli sulkeutuu.")

else:
    print(f"Terve {p_nimi}! Olet {ika} vuotias.\n")

    ## Aloitus valikko
    valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa energiapisteet\n"))

    while valikko != "Lopeta":
        if valikko == "B":
            ## Näytä inventaario eli tavara lista funktiota käyttäen
            pelaaja.nayta_inventory(tavarat)       

        elif valikko == "C":
            ## Näytä elämäpisteet eli health funktiota käyttäen
            pelaaja.nayta_energy(energiapisteet)

        elif valikko == "A":
            aloitus_huone.iso_puu()
            ## Tästä alkaa virallinen peli

        else:
            print("Virheellinen syöte, yritä uudelleen\n")
        valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(A) Aloittaa pelin\n(B) Katsoa inventaariota\n(C) Katsoa energiapisteet\n"))
    
    print("Lopetetaan peli.")
        