class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        """Ispisuje sve atribute proizvoda."""
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} EUR, Dostupna količina: {self.dostupna_kolicina}")


# Inicijalno stanje skladišta (2 proizvoda)
skladiste = [
    Proizvod("Televizor", 3000, 5),
    Proizvod("Mobitel", 1500, 15)
]


def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    """Dodaje novi proizvod u listu skladiste."""
    novi_proizvod = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi_proizvod)
