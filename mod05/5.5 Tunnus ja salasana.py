max_yritykset = 5
yritykset = 0

while yritykset < max_yritykset:
    kayttaja = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttaja == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    elif kayttaja != "python" or salasana != "rules":
        print("Väärä käyttäjätunnus tai salasana, yritä uudelleen.")
        yritykset += 1
else:
    print("Pääsy evätty")
    


    
