class Huone:
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine

    def omenapuu(self, pelaaja):
        print("Olet Nyt vanhan omenapuun luona.")
        print("Puusta tippuu omena ja päätät pomia sen mukaan.")
        omppu = input("Paina A näppäintä ottaaksesi omenan mukaan: ")
        if omppu == "A":
            pelaaja.lisaa_inventoryyn(self.esine)
    
