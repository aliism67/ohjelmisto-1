k1_rotu = "Mastiffi"
k1_nimi = "Gabe"
k1_syntymävuosi = 2026

k2_rotu = "Kultainen noutaja"
k2_nimi = "Loki"
k2_syntymävuosi = 2023

k3_rotu = "Labradori"
k3_nimi = "Malla"
k3_syntymävuosi = 2018


class Koira:
    pass

#Luokka on kuin suunnitelma ja olio on sen perusteella rakenettu yksilö

koira = Koira()
koira2 = Koira()

koira.nimi = "Gabe"
koira.rotu = "mastiffi"

koira2.nimi = "Loki"
koira2.rotu = "Kultainen noutaja"

print(F"Ensimmäisen koiran nimi {koira.nimi}")

print(f"Toisen koiran nimi on {koira2.nimi}")

class Kissa:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

kissa = Kissa("Panda", 2019)
kissa2 = Kissa("Lilli", 2024)

print(f"Kissan nimi ja syntymävuosi {kissa.nimi}, {kissa.syntymävuosi}")
