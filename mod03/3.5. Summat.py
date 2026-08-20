leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

massa = luodit * 13.3 + ((32 * 13.3)*naulat) + ((32 * 20 * 13.3)*leiviskät)

kilot = massa / 1000
grammat = massa % 1000

print("Massa nykymittojen mukaan:", int(kilot), "kilogrammaa ja", int(grammat), "grammaa")