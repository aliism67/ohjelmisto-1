import json

#virheidenkäsittely

class Player:
    def __init__(self, ika):
        self.age = ika
        self.pisteet = 0
    def go_forward(self):
        self.pisteet += 1




#Pelitilanteen lataus ja tallennus
def save_game():
    try:
        with open ("mod013/save.txt", "w") as file:
            data = {player.ika, player.pisteet}
            json.dump(data, file)
    except FileNotFoundError:
        print("H")
    except IOError:
        print("joo")
        


def load_game():
    pass


#main loop
def start_game():
    game_running = True
    while game_running:
        tehdaan = input("Mitä tehdään: ")
        if tehdaan == "tallenna":
            save_game()
        elif tehdaan == "lataa":
            load_game()
        elif tehdaan == "Etene":
            player.go_forward()
        elif tehdaan == "lopeta":
            game_running = False
        else:
            print("virheellinen komento")


print("Peli alkaa")
ika = 0

while True:
    try:
        ika = int(input("Anna pelaajan ikä: "))
        break
    except ValueError:
        print("Virhe: ei ole kokonaisluku.")



print(f"Pelaajan ikä on {ika}")

if ika > 11:
    player = Player(11)
    start_game()
else:
    print("Pelaaja liian nuori")
