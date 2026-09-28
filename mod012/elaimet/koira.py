class Koira:
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu

    def hauku(self):
        print(f"{self.nimi} Haukuu")

# Tarkistaa että luokka toimii, jos oliota haetaan muualta ei tätä suoriteta
if __name__ == "__main__":
    koira = Koira("TestiRekku", "labradorin noutaja")
    koira.hauku()
