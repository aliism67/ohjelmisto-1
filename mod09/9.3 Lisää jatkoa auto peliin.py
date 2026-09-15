class Car:
    def __init__(self, Rekisterinumero, Huippunopeus):
        self.Rekisterinumero = Rekisterinumero
        self.Huippunopeus = Huippunopeus
        self.Nopeus = 0
        self.Matka = 0


    def kiihdyta(self, muutos):
        self.Nopeus += muutos
        if self.Nopeus > self.Huippunopeus:
            self.Nopeus = self.Huippunopeus
            print("Nopeus ei voi olla isompi kuin huippunopeus")
        elif self.Nopeus < 0:
            self.Nopeus = 0
            print("Auto jarruttaa")

    def kulje(self, tunnit):
        self.Matka += self.Nopeus * tunnit
        

auto = Car("ABC-123", 142)

print(f"Uuden auton rekisterinumero on {auto.Rekisterinumero}, huippunopeus {auto.Huippunopeus} km/h, nopeus {auto.Nopeus} ja kuljettu matka {auto.Matka}")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

auto.kulje(1.5)
print(f"Kuljettu matka: {auto.Matka}")

print(f"Auton nopeus kiihdytyksen jälkeen jälkeen: {auto.Nopeus}")
auto.kiihdyta(-200)
print(f"Auton nopeus jarrutuksen jälkeen: {auto.Nopeus}")