class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja on: {self.paatoimittaja}\n")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja on: {self.kirjoittaja}, ja sivuja on: {self.sivumaara}\n")

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja(f"Hytti n:o 6", "Rosa Liksom", 200)

lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()
