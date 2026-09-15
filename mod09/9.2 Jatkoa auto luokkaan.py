class Car:
    def __init__(self, Rekisterinumero, Huippunopeus, Nopeus = 0, Matka = 0):
        self.Rekisterinumero = Rekisterinumero
        self.Huippunopeus = Huippunopeus
        self.Nopeus = Nopeus
        self.Matka = Matka

    def kiihdyta(self, muutos):
            if muutos > 0:
                print("Auto kiihdyttää")
            elif muutos < 0:
                 print("Auto jarruttaa")
            elif muutos > auto.Huippunopeus:
                 print("Nopeus ei voi olla isompi kuin huippunopeus")


auto = Car("ABC-123", "142 km/h",)

print(f"Uuden auton rekisterinumero on {auto.Rekisterinumero}, huippunopeus {auto.Huippunopeus}, hetkellinen nopeus {auto.Nopeus} ja kuljettu matka {auto.Matka}")

auto.kiihdyta(150)