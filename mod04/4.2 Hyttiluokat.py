hytti = (input("Anna hyttiluokka A, B, C tai LUX: "))


if hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

elif hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")

else:
    print("Virheellinen hyttiluokka.")