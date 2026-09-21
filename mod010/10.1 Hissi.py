class Hissi:
    def __init__(self, ylin, alin):
        self.nykyinen = alin
        self.ylin = ylin
        self.alin = alin


    def siirry_kerrokseen(self, kerros):
        while self.nykyinen < kerros:
            self.liiku_ylös()

        while self.nykyinen > kerros:
            self.liiku_alas()


    def liiku_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def liiku_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")
              
hissi1 = Hissi(10, 1)

hissi1.siirry_kerrokseen(8)
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(10)
hissi1.siirry_kerrokseen(1)