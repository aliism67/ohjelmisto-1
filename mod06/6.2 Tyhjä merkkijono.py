numerot = []


while True:
    luku = input("Anna luku: ")
    if luku == "":
        break

    numerot.append(int(luku))
numerot.sort(reverse=True)

for num in range(5):
    print(numerot[num])

