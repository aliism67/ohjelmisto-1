def muunna_litroiksi(gallons):
    return (gallons * 3.785)


litra = 0

while True:
    gallons = float(input("Anna gallonamäärä: "))

    if gallons < 0 :
        break

    litra = muunna_litroiksi(gallons)
    print(litra)
