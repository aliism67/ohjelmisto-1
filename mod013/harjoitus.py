
#tiedon tallentaminen
with open("mod013/data.txt", "a") as data_tiedosto:
    data_tiedosto.write("Moi\n")

#Datan lukeminen

with open("mod013/data.txt", "r") as mun_data_tiedosto:
    mun_data = mun_data_tiedosto.readline()
    print(mun_data)
    mun_data = mun_data_tiedosto.readline()
    mun_data = mun_data_tiedosto.readline()
    mun_data = mun_data_tiedosto.readlines()
    print(mun_data)

with open("mod013/intro.txt") as intro_file:
    print(intro_file.read())


#pelaajan tallennus suoraan materiaalista

import json

pelaajan_tiedot = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}
with open("mod013/save.json", "w") as tiedosto:
    json.dump(pelaajan_tiedot, tiedosto)

with open("mod013/save.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")

#
