from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza): # __init__ je konstruktor koji postavlja atribute objekta
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):  # ispis() ispisuje sve atribute automobila
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def starost(self): # starost() računa starost automobila tako da oduzme godinu proizvodnje od trenutne godine pomoću datetime.now().year
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")


# Primjer korištenja:
auto1 = Automobil("BMW", "340i", 2020, 73500)

auto1.ispis()
auto1.starost()
