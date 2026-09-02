import random

#π≈4n/N

N = 10
n = 0
laskuri = 0

while laskuri < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    laskuri += 1
    print(f"{laskuri}. Arvotun pisteen koordinaatit, x: {x}, y: {y}")
    if x**2 + y**2 < 1:
        n += 1
        print("Piste on ympyrän sisällä")
print(f"{N} pisteestä {n} on ympyrän sisällä")