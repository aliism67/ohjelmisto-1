'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.'''

luku = int(input("Anna luku: "))
while luku != "":
    if luku == "":
        break
    luku = (input("Anna luku: "))
print(f"Isoin luku oli - ja pienin luku oli - .")


    

