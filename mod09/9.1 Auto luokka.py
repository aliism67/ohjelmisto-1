class Car:
    def __init__(self, Rekisterinumero, Huippunopeus, Nopeus = 0, Matka = 0):
        self.Rekisterinumero = Rekisterinumero
        self.Huippunopeus = Huippunopeus
        self.Nopeus = Nopeus
        self.Matka = Matka

auto = Car("ABC-123", "142 km/h" )

print(f"Uuden auton rekisterinumero on {auto.Rekisterinumero}, huippunopeus {auto.Huippunopeus}, hetkellinen nopeus {auto.Nopeus} ja kuljettu matka {auto.Matka}")
