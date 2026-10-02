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

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        for i in range(osallistujat):
            uusi_auto = Car(f"Rekisterinumero {i+1}", huippu)
            uusi_auto = Car(rekisteritunnus, huippu)
            self.autot.append(uusi_auto)


    def tunti_kuluu(self):
        muutos = random.randint(-10, 15)
        while self.Matka < self.pituus:
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        for self in autot:
            print("Auton", self.Rekisterinumero,"huippunopeus on:",self.Huippunopeus, "ja nopeus on:",self.Nopeus,"ja kuljettu matka:", self.Matka)

    def kilpailu_ohi(self):
        if self.Matka <= self.pituus:
            True
            while True:
                auto_kilpailu.tunti_kuluu()
        else:
            False



autot = []
tunnit = 0
huippu = random.randint(100, 200)

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippu = random.randint(100, 200)
    auto = Car(rekisteritunnus, huippu)
    autot.append(auto)

auto_kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
#auto_kilpailu.tulosta_tilanne()


