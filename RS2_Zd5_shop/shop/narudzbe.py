from .proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        """Ispisuje naručene proizvode, količine i ukupnu cijenu."""
        naruceni = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {naruceni}, Ukupna cijena: {self.ukupna_cijena} EUR")


# Lista svih narudžbi
narudzbe = []


def napravi_narudzbu(naruceni_proizvodi):
    """Stvara novu narudžbu ako su svi proizvodi dostupni i argumenti ispravni."""

    # 1. Provjere argumenata
    if not isinstance(naruceni_proizvodi, list):
        print("Greška: Argument mora biti lista.")
        return None
    if not naruceni_proizvodi:
        print("Greška: Lista naručenih proizvoda ne smije biti prazna.")
        return None
    for p in naruceni_proizvodi:
        if not isinstance(p, dict):
            print("Greška: Svaki element mora biti rječnik.")
            return None
        for kljuc in ["naziv", "cijena", "narucena_kolicina"]:
            if kljuc not in p:
                print(f"Greška: Nedostaje ključ '{kljuc}' u {p}")
                return None

    # 2. Provjera dostupnosti proizvoda
    for p in naruceni_proizvodi:
        pronadjen = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not pronadjen or pronadjen.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None

    # 3. Izračun ukupne cijene (jedna linija)
    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in naruceni_proizvodi)

    # 4. Stvaranje narudžbe
    nova_narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append({"narudzba": nova_narudzba})
    return nova_narudzba
