class Radnik: # Radnik ima atribute ime, pozicija, placa i metodu work() koja ispisuje poziciju
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")


class Manager(Radnik): # Manager nasljeđuje klasu Radnik i dodaje atribut department
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa) # super().__init__() poziva konstruktor nadklase Radnik
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"{radnik.ime} je dobio povišicu od {povecanje} €.")
        print(f"Nova plaća: {radnik.placa} €.")


# Primjer korištenja:

radnik1 = Radnik("Ivan", "Programer", 1200) # instanca klase Radnik
manager1 = Manager("Ana", "Voditelj tima", 2000, "IT") # instanca klase Manager

radnik1.work() # poziv metode work iz klase Radnik
manager1.work() # poziv metode work iz klase Manager

# Manager daje povišicu radniku
manager1.give_raise(radnik1, 300)
