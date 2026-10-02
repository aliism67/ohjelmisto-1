import json

class Player:
    def __init__(self, nimi, tavarat, sijainti, energiapisteet, karmapisteet):
        self.nimi = nimi
        self.tavarat = tavarat
        self.sijainti = sijainti
        self.energiapisteet = energiapisteet
        self.karmapisteet = karmapisteet

    def nayta_inventory(self):
        if len(self.tavarat) == 0:
            print("Sinulla ei ole vielä mitään mukana :(\n")
        else:
            print("Sinulla on mukana seuraavat esineet: ")
            for i in self.tavarat:
                print(f"-{i.nimi}")

    def lisaa_inventoryyn(self, esine):
        self.tavarat.append(esine)
        print(f"{esine.nimi} lisättiin inventaarioon")
    def poista_inventory(self, esine):
        self.tavarat.remove(esine)
        print(f"{esine.nimi} poistettiin inventaariosta")

    def nayta_energy(self):
        print(f"Sinulla on: {self.energiapisteet} energiapistettä!\n")

    def nayta_karma(self):
        print(f"Sinulla on: {self.karmapisteet} karmapistettä")

    def tallenna_peli(self):
        print("Tallennetaan peli.")
        try:
            with open("mod13/save.txt", "w") as file:
                pelaaja_tiedot = {"nimi:": self.nimi, "tavarat": [esine.nimi for esine in self.tavarat], "sijainti": self.sijainti, "energiapisteet": self.energiapisteet, "karmapisteet": self.karmapisteet}
                json.dump(pelaaja_tiedot, file)
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

    def lataa_peli(self):
        try:
            with open("mod13/save.txt", "r") as file:
                pelaaja_tiedot = json.load(file)
                #print("Ladattu tallennusdata:", data)
                self.nimi = pelaaja_tiedot["nimi"]
                self.tavarat = pelaaja_tiedot["tavarat"]
                self.sijainti = pelaaja_tiedot["sijainti"]
                self.energiapisteet = pelaaja_tiedot["energiapisteet"]
                self.karmapisteet = pelaaja_tiedot["karmapisteet"]
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

        

