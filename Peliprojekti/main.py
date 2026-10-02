from moduulit import Huone, Player, Esine

energiapisteet = 10
tavarat = []

omena = Esine("Omena", 5)
metsa_mansikka = Esine("Metsä mansikka", 2)
roska = Esine("Roska", 0)
lusikka = Esine("Kiiltävä lusikka", 0)
roskis = Esine("Roskakori", 0)
kapy = Esine("Männyn käpy", 0)

omenapuu = Huone("Vanha puu", omena)
jarven_ranta = Huone("Järven ranta", roska)
joki = Huone("Joki", lusikka)
pelto = Huone("Pelto", metsa_mansikka)
kallio = Huone("Kallio", roskis)
manty = Huone("Mänty metsä", kapy)




print("Tervetuloa pelaamaan Metsä seikkailua!")

p_nimi = input("Mikä on nimesi?: ")
ika = int(input("Kuinka vanha olet?: "))

pelaaja = Player(p_nimi, tavarat, 0, 10, 10)

kaynnissa = True

while kaynnissa:
    if ika < 12:
        print(f"Olet liian nuori, peli sulkeutuu.")
        break

    else:
        print(f"Terve {p_nimi}! Olet {ika} vuotias.\n")

    paa_valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(1) Aloittaa pelin\n(2) Katsoa inventaariota\n(3) Katsoa energiapisteet\n(4) Katsoa karmapisteet\nLopeta peli (lopeta)"))

    while paa_valikko != "lopeta":
        if paa_valikko == "2":
            pelaaja.nayta_inventory(tavarat)       

        elif paa_valikko == "3":
            pelaaja.nayta_energy(energiapisteet)

        elif paa_valikko == "1":
            omenapuu.iso_puu(pelaaja)

        elif paa_valikko == "4":
            pelaaja.nayta_karma()

        else:
            print("Virheellinen syöte, yritä uudelleen\n")
        paa_valikko = (input("----VALIKKO----\nMitä haluat tehdä?\n(1) Aloittaa pelin\n(2) Katsoa inventaariota\n(3) Katsoa energiapisteet\n(4) Katsoa karmapisteet\nLopeta peli (lopeta)"))
    
    
    print("Lopetetaan peli.")