def kokonaisluvut(lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

lista = [28, 37, 60, 5, 30]
luvut = kokonaisluvut(lista)
print(luvut)

