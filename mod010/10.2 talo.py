class Hissi:
    def __init__(self, nimi, alin, ylin):
        self.nykyinen = alin
        self.ylin = ylin
        self.alin = alin
        self.nimi = nimi


    def siirry_kerrokseen(self, kerros):
        print(f"Siirrytään kerrokseen {kerros}")
        while self.nykyinen < kerros:
            self.liiku_ylös()

        while self.nykyinen > kerros:
            self.liiku_alas()


    def liiku_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen}")

    def liiku_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen}")

class Talo:
    def __init__(self, alin, ylin, hissien_lukumäärä):
        self.hissit = []
        for i in range(hissien_lukumäärä):
            uusi_hissi = Hissi(f"numero {i+1}", alin, ylin,)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, numero, kerros):
        self.hissit[numero - 1].siirry_kerrokseen(kerros)


talo = Talo(2, 12, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(1, 7)
talo.aja_hissia(2, 9)
talo.aja_hissia(3, 8)