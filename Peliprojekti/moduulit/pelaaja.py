import json

class Player:
    def __init__(self, nimi, tavarat, energiapisteet, karmapisteet, sijainti):
        self.nimi = nimi
        self.tavarat = tavarat
        self.energiapisteet = energiapisteet
        self.karmapisteet = karmapisteet
        self.sijainti = sijainti

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

    def poista_inventorysta(self, esine):
        self.tavarat.remove(esine)
        print(f"{esine.nimi} poistettiin inventaariosta")

    def nayta_energy(self):
        print(f"Sinulla on: {self.energiapisteet} energiapistettä!\n")

    def nayta_karma(self):
        print(f"Sinulla on: {self.karmapisteet} karmapistettä")

    def liiku(self):
        if self.sijainti.eteen is not None:
            self.sijainti = self.sijainti.eteen

            if self.sijainti.nimi == "Vanha puu":   
                self.sijainti.omenapuu(self)
            elif self.sijainti.nimi == "Joki":
                self.sijainti.joki(self)
            elif self.sijainti.nimi == "Järven ranta":
                self.sijainti.jarven_ranta(self)
            elif self.sijainti.nimi == "Pelto":
                self.sijainti.pelto(self)
            elif self.sijainti.nimi == "Kallio":
                self.sijainti.kallio(self)
            elif self.sijainti.nimi == "Mänty metsä":
                self.sijainti.manty(self)
            elif self.sijainti.nimi == "Luola":
                self.sijainti.luola(self)
            elif self.sijainti.nimi == "Kuusi metsä":
                self.sijainti.kuusi(self)
            elif self.sijainti.nimi == "Kuusi metsän laita":
                return self.sijainti.paatos_huone(self)

    def syo(self):
        if len(self.tavarat) == 0:
            print("Sinulla ei ole mitään mukana.")
            return

        print("Mitä haluat syödä?")

        for numero, esine in enumerate(self.tavarat, 1):
            print(f"{numero}. {esine.nimi}")

        valitse = input("Valitse numero: ")

        if valitse.isdigit():
            valitse = int(valitse)
            if 1 <= valitse <= len(self.tavarat):
                esine = self.tavarat[valitse - 1]
                if esine.syotava:
                    print(f"Söit esineen {esine.nimi}.")

                    self.energiapisteet += 5
                    self.tavarat.remove(esine)

                    print(f"Sait 5 energiapistettä. Energiaa nyt: {self.energiapisteet}")
                else:
                    print(f"Et voi syödä esinettä {esine.nimi}.")
            else:
                print("Virheellinen valinta.")
        else:
            print("Anna numero.")
            
    def tallenna_peli(self):
        print("Tallennetaan peli.")
        try:
            with open("Peliprojekti/save.txt", "w") as file:
                pelaaja_tiedot = {"nimi": self.nimi, "tavarat": [esine.nimi for esine in self.tavarat], "sijainti": self.sijainti.nimi, "energiapisteet": self.energiapisteet, "karmapisteet": self.karmapisteet}
                json.dump(pelaaja_tiedot, file)
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

    def lataa_peli(self, huoneet, esineet):
        print("ladataan peli")
        try:
            with open("Peliprojekti/save.txt", "r") as file:
                pelaaja_tiedot = json.load(file)

            print("Tallennus löytyi!")
            print(pelaaja_tiedot)
            self.nimi = pelaaja_tiedot["nimi"]
            self.tavarat = pelaaja_tiedot["tavarat"]
            self.sijainti = pelaaja_tiedot["sijainti"]
            self.energiapisteet = pelaaja_tiedot["energiapisteet"]
            self.karmapisteet = pelaaja_tiedot["karmapisteet"]

            for huone in huoneet:
                if huone. nimi == pelaaja_tiedot["sijainti"]:
                    self.sijainti = huone
                    break
            for tallennettu_esine in pelaaja_tiedot["tavarat"]:
                for esine in esineet:
                    if esine.nimi == tallennettu_esine:
                        self.tavarat.append(esine)
                        break
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")