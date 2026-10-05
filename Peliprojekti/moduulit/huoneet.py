class Huone:
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine
        self.eteen = None

    def omenapuu(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt vanhan omenapuun luona.")
        print("Puusta tippuu omena ja päätät pomia sen mukaan.")
        while True:
            omppu = input("Paina A näppäintä ottaaksesi omenan mukaan: ")
            if omppu == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                break
            elif omppu != "A":
                print("Virheellinen syöte. Yritä uudelleen")


    def joki(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt joen rannalla.")
        print("Joesta löytyy roska ja päätät poimia sen mukaan.")
        while True:
            roska3 = input("Paina A näppäintä ottaaksesi roskan mukaan tai paina Enter, jos et halua ottaa roskaa mukaan: ")
            if roska3 == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                pelaaja.karmapisteet += 2
                print(f"Kiitos, kun välität luonnosta! Sait 2 karmapistettä.")
                break
            elif roska3 == "":
                print("Et ottanut roskaa mukaan, etkä saanut karmapisteitä")
                break
            elif roska3 != "A":
                print("Virheellinen syöte. Yritä uudelleen")


    def jarven_ranta(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt järven rannalla.")
        print("Rannalta löytyy roska ja päätät poimia sen mukaan.")
        while True:
            roska = input("Paina A näppäintä ottaaksesi roskan mukaan tai paina Enter, jos et halua ottaa roskaa mukaan: ")
            if roska == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                pelaaja.karmapisteet += 2
                print(f"Kiitos, kun välität luonnosta! Sait 2 karmapistettä.")
                break
            elif roska == "":
                print("Et ottanut roskaa mukaan, etkä saanut karmapisteitä")
                break
            elif roska != "A":
                print("Virheellinen syöte. Yritä uudelleen")

    def pelto(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt pellolla.")
        print("Pellolta löytyy metsä mansikka ja päätät poimia sen mukaan.")
        metsa_mansikka = input("Paina A näppäintä ottaaksesi metsä mansikan mukaan tai paina Enter, jos et halua otaa metsä mansikkaa mukaan: ")
        while True:
            if metsa_mansikka == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                break
            elif metsa_mansikka == "":
                print("Et ottanut metsä mansikkaa mukaan")
                break
            elif metsa_mansikka != "A":
                print("Virheellinen syöte. Yritä uudelleen")

    def kallio(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt kallion luona.")
        print("Kalliolta löytyy roska ja päätät poimia sen mukaan.")
        while True:
            roska2 = input("Paina A näppäintä ottaaksesi roskan mukaan tai paina Enter, jos et halua ottaa roskaa mukaan: ")
            if roska2 == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                pelaaja.karmapisteet += 2
                print(f"Kiitos, kun välität luonnosta! Sait 2 karmapistettä.")
                break
            elif roska2 == "":
                print("Et ottanut roskaa mukaan, etkä saanut karmapisteitä")
                break
            elif roska2 != "A":
                print("Virheellinen syöte. Yritä uudelleen")

    def manty(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt mänty metsässä.")
        print("Mänty metsästä löytyy roska ja päätät poimia sen mukaan.")
        while True:
            roska4 = input("Paina A näppäintä ottaaksesi roskan mukaan tai paina Enter, jos et halua ottaa roskaa mukaan: ")
            if roska4 == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                pelaaja.karmapisteet += 2
                print(f"Kiitos, kun välität luonnosta! Sait 2 karmapistettä.")
                break
            elif roska4 == "":
                print("Et ottanut roskaa mukaan, etkä saanut karmapisteitä")
                break
            elif roska4 != "A":
                print("Virheellinen syöte. Yritä uudelleen")

    def luola(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt luolan suulla.")
        print("Luolan edestä löytyy mustikka ja päätät poimia sen mukaan.")
        while True:
            mustikka = input("Paina A näppäintä ottaaksesi mustikan mukaan tai paina enter, jos et halua ottaa mustikkaa mukaan: ")
            if mustikka == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                break
            elif mustikka == "":
                print("Et ottanut mustikkaa mukaan")
                break
            elif mustikka != "A":
                print("Virheellinen syöte. Yritä uudelleen")

    def kuusi(self, pelaaja):

        pelaaja.energiapisteet -= 1
        print("----------------------------------------------------")
        print(f"matkustaminen vie sinulta yhden energiapisteen.")
        print("Olet nyt kuusi metsässä.")
        print("Kuusi metsästä löytyy roska ja päätät poimia sen mukaan.")
        while True:
            roska5 = input("Paina A näppäintä ottaaksesi roskan mukaan tai paina Enter, jos et halua ottaa roskaa mukaan: ")
            if roska5 == "A":
                pelaaja.lisaa_inventoryyn(self.esine)
                pelaaja.karmapisteet += 2
                print(f"Kiitos, kun välität luonnosta! Sait 2 karmapistettä.")
                break
            elif roska5 == "":
                print("Et ottanut roskaa mukaan, etkä saanut karmapisteitä")
                break
            elif roska5 != "A":
                print("Virheellinen syöte. Yritä uudelleen")

    def paatos_huone(self, pelaaja):
        print("----------------------------------------------------")
        print("Olet seikkaillut jo pitkään ja tapaat mystisen hahmon kuusi metsän laidalla")
        print("Hahmo kertoo olevansa metsänhenki")
        if pelaaja.karmapisteet < 2:
            print("Metsänhenki: Olen pettynyt kuinka et ole pitänyt huolta luonnosta. Et ole poistanut luonnosta yhtäkään roskaa")
            return True
        elif pelaaja.karmapisteet == 2:
            print("Metsänhenki: Luonnon puhdistaminen alkaa pienellä teolla. Olet kerännyt yhden roskan, mutta toivon, että jatkossa pystyisit keräämään enemmänkin.")
            return True
        elif pelaaja.karmapisteet == 4:
            print("Metsänhenki: Näen, että haluat ylläpitää luonnon puhtautta. Olet kerännyt kaksi roskaa. Kannustan sinua puhdistamaan luontoa vielä vähän ahkerammin.")
            return True
        elif pelaaja.karmapisteet == 6:
            print("Metsänhenki: Olet jo hyvässä vauhdissa. kolme kerättyä roskaa on jo hyvä suoritus.")
            return True
        elif pelaaja.karmapisteet == 8:
            print("Metsänhenki: Olen ylpeä sinusta, kuinka haluat pitää luonnon hyvässä kunnossa. Olet kerännyt neljä roskaa")
            return True
        elif pelaaja.karmapisteet == 10:
            print("Metsänhenki: Olen tarkkaillut sinua. Kuinka olet ystävällisesti puhdistanut luontoa. Olen varsin kiitollinen kaikkien viiden roskan kerämisestä.")
            return True