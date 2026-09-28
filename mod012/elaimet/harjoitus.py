class Koira:
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu

    def hauku(self):
        print(f" {self.nimi} Haukuu")

class Kissa:
    def __init__(self, nimi, vari):
        self.nimi = nimi
        self.vari = vari

    def miu(self):
        print(f"{self.nimi} maukuu")

class Ihminen:
    def __init__(self, nimi, kotimaa):
        self.nimi = nimi
        self.kotimaa = kotimaa

    def hauku(self):
        print("Oot tyhäm")

koira1 = Koira("Rekku", "Labradori")
kissa1 = Kissa("Misu", "Musta")
ihminen1 = Ihminen("Joa", "suomalainen")
ihminen2 = Ihminen("Jada", "suomalainen")
