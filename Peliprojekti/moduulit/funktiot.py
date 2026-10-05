class Funktiot:
    @staticmethod  #Luokka ei tarvitse self-parametriä tai mitään muitakaan tietoja
    def tulosta_valikko(pelaaja, huoneet, esineet):

        while True:

            print("----VALIKKO----")
            print("Mitä haluat tehdä?")
            print("1. Jatkaa matkaa")
            print("2. Katsoa inventaariota")
            print("3. Katsoa energiapisteet")
            print("4. Katsoa karmapisteet")
            print("5. Syö")
            print("6. Tallenna peli")
            print("7. Lataa peli")
            print("8. Lopeta peli")

            paa_valikko = input("Mitä haluat tehdä?: ")

            if paa_valikko == "1":
                peli_loppui = pelaaja.liiku()
                if peli_loppui:
                    print("Kiitos Metsä Seikkailu pelin pelaamisesta!")
                    break
            elif paa_valikko == "2":
                pelaaja.nayta_inventory()
            elif paa_valikko == "3":
                pelaaja.nayta_energy()
            elif paa_valikko == "4":
                pelaaja.nayta_karma()
            elif paa_valikko == "5":
                pelaaja.syo()
            elif paa_valikko == "6":
                pelaaja.tallenna_peli()
            elif paa_valikko == "7":
                pelaaja.lataa_peli(huoneet, esineet)
            elif paa_valikko == "8":
                print("Peli lopetetaan.")
                break



    @staticmethod
    def aloitus(pelaaja, huone, huoneet, esineet):

        while True:

            print("\n---- VALIKKO ----")
            print("1. Aloita peli")
            print("2. Katso inventaariota")
            print("3. Katso energiapisteet")
            print("4. Katso karmapisteet")
            print("5. Lataa peli")
            print("6. Tallenna peli")
            print("7. Lopeta peli")

            valinta = input("Mitä tehdään?: ")

            if valinta == "1":
                huone.omenapuu(pelaaja)
                break

            elif valinta == "2":
                pelaaja.nayta_inventory()

            elif valinta == "3":
                pelaaja.nayta_energy()

            elif valinta == "4":
                pelaaja.nayta_karma()

            elif valinta == "5":
                pelaaja.lataa_peli(huoneet, esineet)
                break

            elif valinta == "6":
                pelaaja.tallenna_peli()

            elif valinta == "7":
                print("Kiitos pelaamisesta!")
                break

            else:
                print("Virheellinen syöte, yritä uudelleen.")
        