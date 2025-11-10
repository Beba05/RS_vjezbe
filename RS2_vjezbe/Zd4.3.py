class Student:
    def __init__(self, ime, prezime, godine, ocjene): # __init__ postavlja atribute svakog studenta
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self): # prosjek() računa prosječnu ocjenu studenta
        return sum(self.ocjene) / len(self.ocjene)


# Polazni podaci:
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

# Stvaranje liste objekata klase Student pomoću list comprehensiona: svaki rječnik pretvaramo u objekt klase Student
studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

# Pronalaženje studenta s najvećim prosjekom u jednoj liniji:
najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())

# Ispis rezultata:
print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}")
print(f"Prosjek ocjena: {najbolji_student.prosjek():.2f}")
