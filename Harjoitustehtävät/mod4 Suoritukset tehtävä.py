'''Kirjoita ohjelma, joka kysyy käyttäjältä hänen suorituksensa kolmella eri osa-alueella: fysiikasta, matematiikasta ja kemiasta. Ohjelman tulee kertoa, saiko käyttäjä stipendin.

Stipendi myönnetään, jos:

käyttäjän tulos on yli 90 sekä fysiikassa että matematiikassa tai

käyttäjän tulos on yli 95 kemiassa.

Lisäksi ohjelman on ilmoitettava, jos tulos jossain aineessa on alle 50. Tällöin käyttäjä ei voi saada stipendiä, vaikka muut ehdot täyttyisivätkin.'''

matematiikka = int(input("Anna matematiikan pistemäärä: "))
fysiikka = int(input("Anna fysiikan pistemäärä: "))
kemia = int(input("Anna kemian pistemäärä: "))

if matematiikka < 50 and fysiikka < 50 or kemia < 50:
    print("Et voi saada stipendiä, koska tulos on jossain aineessa liian pieni")
elif matematiikka > 90 and fysiikka > 90 or kemia > 95:
    print("Saat stipendin")