'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.'''

luku = input("Anna luku: ")

if luku != "":
    luku = int(luku)
    pienin = luku
    suurin = luku

    while True:
        luku = input("Anna luku: ")

        if luku == "":
            break

        luku = int(luku)

        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

    print(f"Isoin luku oli {suurin} ja pienin luku oli {pienin}.")