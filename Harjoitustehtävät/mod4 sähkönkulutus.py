#Kirjoita ohjelma, joka kysyy käyttäjältä sähkönkulutusta kilowattitunteina (kWh). Ohjelman tulee laskea sähkölasku kolmen eri porrastetun hinnan mukaan ja tulostaa loppusumma.

#Ensimmäiset 50 kWh maksavat 10 senttiä/kWh. Seuraavat 150 kWh maksavat 8 senttiä/kWh. Yli 200 kWh menevä kulutus maksaa 6 senttiä/kWh.

kulutus = float(input("Paljonko on sähkönkulutuksesi kilowattitunteina?: "))

if kulutus <= 50:
    hinta = kulutus * 10

elif kulutus <= 200:
    hinta = 50 * 10 
    hinta = hinta + (kulutus - 50) * 8

else:
    hinta = 50 * 10
    hinta += 150 * 8
    hinta += (kulutus - 200) * 6

print(f"sähkönhinta on {hinta} senttiä")
    

