import random

'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''

def nopanheitto(tahkot):
    return random.randint(1, tahkot)

luku = 0
max_luku = int(input("Mikä on noppien maksimisilmäluku: "))

while luku < max_luku:
        luku = nopanheitto(max_luku)
        print(luku)
    