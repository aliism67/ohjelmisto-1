import math

def pizza(funktion_sisainen_halkaisija, funktion_sisainen_hinta):
    sade = funktion_sisainen_halkaisija / (2 * 100)
    pinta_ala = math.pi * (sade**2)
    yksikkohinta = funktion_sisainen_hinta / pinta_ala
    return yksikkohinta


funktiolle_annettava_halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
funktiolle_annettava_hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
tulos1 = pizza(funktiolle_annettava_halkaisija1, funktiolle_annettava_hinta1)

funktiolle_annettava_halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
funktiolle_annettava_hinta2 = float(input("Anna toisen pizzan hinta euroina: "))
tulos2 = pizza(funktiolle_annettava_halkaisija2, funktiolle_annettava_hinta2)

if tulos1 < tulos2:
    print(f"Ensimmäinen pizza on halvempi ja hinta on {tulos1:.2f} e/m2")
elif tulos1 > tulos2:
    print(f"Toinen pizza on halvempi ja hinta on {tulos2:.2f} e/m2")