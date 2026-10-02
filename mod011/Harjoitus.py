#Yliluokka
class Elain:

    elainten_lukumaara = 0

    def __init__(self, nimi, paino, syntyma_aika):
        self.nimi = nimi
        self.paino = paino
        self.syntyma_aika = syntyma_aika
        Elain.elainten_lukumaara += 1

    def liiku(self):
        print(f"{self.nimi} liikkuu jotenkin jonnekkin")

    def kaikki_tiedot(self):
        print(f"Nimi: {self.nimi}, paino: {self.paino/100} kg, syntymäaika: {self.syntyma_aika}")

uusi_elain = Elain("Joku eläin", 1500, 20250921)

class Peto():
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja

#Aliluokat
class Karhu(Elain, Peto):
    def __init__(self, nimi, paino, syntyma_aika, on_horroksessa, on_metsastaja):
        self.on_horroksessa = on_horroksessa
        super().__init__(nimi, paino, syntyma_aika)
        Peto.__init__(self, on_metsastaja)
        
    def karju(self):
        print(f"Karhu nimeltä {self.nimi} karjuu")

    def liiku(self):
        print(f"Karhu {self.nimi} möyrii eteenpäin")

    def kaikki_tiedot(self):
        print(f"\nKarhu on metsästäjä: {self.on_metsastaja}, on talvihorroksessa: {self.on_horroksessa}")
        super().kaikki_tiedot()

class Ilves(Elain):

    def kilju(self):
        print(f"Ilves {self.nimi} kiljuu")

    def kaikki_tiedot(self):
        print("\nIlves")
        super().kaikki_tiedot()

ilves1 = Ilves("Ilves nimeltä Iina", 6500, 20230621)
karhu1 = Karhu("Nalle", 155000, 20200814, False)

#ilves1.kilju()
#karhu1.karju()
#print(karhu1.on_horroksessa)
#karhu1.liiku()

kaikki_elaimet = [uusi_elain, ilves1, karhu1]
kaikki_elaimet.append(Karhu("Isonalle", 205000, 20210411, True, True))

for elain in kaikki_elaimet:
    elain.kaikki_tiedot()

print(f"Eläimiä luotu: {Elain.elainten_lukumaara}")