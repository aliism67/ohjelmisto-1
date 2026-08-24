leiviskät = float(input("Anna leiviskät:\n"))
naulat = float(input("Anna naulat:\n"))
luodit = float(input("Anna luodit:\n"))

massa = luodit * 13.3 + ((32 * 13.3)*naulat) + ((32 * 20 * 13.3)*leiviskät)

#kilot = massa / 1000
#grammat = massa % 1000

kilot = massa // 1000
grammat = massa % 1000

print(f"Massa nykymittojen mukaan: {int(kilot)} kilogrammaa ja {float(grammat):.2f} grammaa")