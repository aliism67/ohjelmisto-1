def kokonaisluvut(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    return summa

lista = [3 ,91 , 27, 84]
summa = kokonaisluvut(lista)
print(f"Summa on {summa}")