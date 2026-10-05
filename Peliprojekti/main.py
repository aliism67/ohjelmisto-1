from moduulit import Huone, Player, Esine, Funktiot

max_energiapisteet = 10
tavarat = []

omena = Esine("Omena", 5, True)
metsa_mansikka = Esine("Metsä mansikka", 5, True)
mustikka = Esine("Metsä mustikka", 3, True)
roska = Esine("Roska", 0, False)
roska2 = Esine("Roska", 0, False)
roska3 = Esine("Roska", 0, False)
roska4 = Esine("Roska", 0, False)
roska5 = Esine("Roska", 0, False)

esineet = [omena, metsa_mansikka, mustikka, roska, roska2, roska3, roska4, roska5]

omenapuu = Huone("Vanha puu", omena)
joki = Huone("Joki", roska3)
jarven_ranta = Huone("Järven ranta", roska)
pelto = Huone("Pelto", metsa_mansikka)
kallio = Huone("Kallio", roska2)
manty = Huone("Mänty metsä", roska4)
luola = Huone("Luola", mustikka)
kuusi = Huone("Kuusi metsä", roska5)
paatos_huone = Huone("Kuusi metsän laita", None)

huoneet = [omenapuu, joki, jarven_ranta, pelto, kallio, manty, luola, kuusi, paatos_huone]

omenapuu.eteen = joki
joki.eteen = jarven_ranta
jarven_ranta.eteen = pelto
pelto.eteen = kallio
kallio.eteen = manty
manty.eteen = luola
luola.eteen = kuusi
kuusi.eteen = paatos_huone

with open("Peliprojekti/Intro_ja_ohjeet.txt", "r") as tiedosto:
    ohjeet = tiedosto.readlines()
    print(ohjeet)

print("Tervetuloa pelaamaan Metsä seikkailua!")
try:
    p_nimi = input("Mikä on nimesi?: ")
    ika = int(input("Kuinka vanha olet?: "))
except:
    ValueError
    print("Et antanut numero arvoa. Yritä uudellen")
    ika = int(input("Kuinka vanha olet?: "))

pelaaja = Player(p_nimi, tavarat, 5, 0, omenapuu)

if ika < 12:
    print(f"Olet liian nuori, peli sulkeutuu.")

else:
    print(f"Hei {pelaaja.nimi}, olet {ika} vuotias!")
    Funktiot.aloitus(pelaaja, omenapuu, huoneet, esineet)

print("Lopetetaan peli")