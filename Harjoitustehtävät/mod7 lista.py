def lista(tavarat):
    uusi = []
    for i in tavarat:
        if len(i) > 5:
            uusi.append(i)
    return uusi



tavarat = ["kahvi", "kala", "tietokone", "partaterä", "huulirasva"]
muut = lista(tavarat)
print("Alkuperäinen lista:", tavarat)
print("Uusi lista:", muut)
