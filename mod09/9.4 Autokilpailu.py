import random

class Car:
    def __init__(self, Rekisterinumero, Huippunopeus):
        self.Rekisterinumero = Rekisterinumero
        self.Huippunopeus = Huippunopeus
        self.Nopeus = 0
        self.Matka = 0

    def kiihdyta(self, muutos):
        self.Nopeus += muutos
        if self.Nopeus < 0:
            self.Nopeus = 0
        if self.Nopeus > self.Huippunopeus:
            self.Nopeus = self.Huippunopeus

    def kulje(self, tunnit):
        self.Matka += self.Nopeus * tunnit


autot = []
tunnit = 0

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippu = random.randint(100, 200)
    auto = Car(rekisteritunnus, huippu)
    autot.append(auto)

kilpailu = True

while kilpailu:
    tunnit += 1
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.Matka >= 10000:
            kilpailu = False

for auto in autot:
    print("Auton", auto.Rekisterinumero,"huippunopeus on:",auto.Huippunopeus, "ja nopeus on:",auto.Nopeus,"ja kuljettu matka:", auto.Matka)