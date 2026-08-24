import math

nimi = input("Mikä on nimesi? ")
print(f"Terve, {nimi}!")

#kompleksi = -4 + 2j
#print(kompleksi.real)
#print(kompleksi.imag)

print(f"{"Vakio":6s}: {"arvo":6s}")
print(f"{"pii":6s}: {math.pi:<6.2f}")

tuloste = '''
Laskutoimituksia ovat yhteenlasku (+), vähennyslasku (-), 
kertolasku (*) jakolasku (/) 
Jakojäännösoperaatio (%), 
pelkän kokonaisosan palauttava jakolasku (//)
potenssiinkorotus (**).
'''