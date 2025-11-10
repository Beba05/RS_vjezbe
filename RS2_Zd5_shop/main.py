from shop import proizvodi, narudzbe

# Dodavanje novih proizvoda
proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

# Dodavanje proizvoda u skladište pomoću funkcije iz modula proizvodi
for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

# Ispis stanja skladišta (6 proizvoda)
print(" STANJE SKLADIŠTA:")
for p in proizvodi.skladiste:
    p.ispis()

# Napravi narudžbu pomoću funkcije iz modula narudzbe
naruceni = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

nova_narudzba = narudzbe.napravi_narudzbu(naruceni)

# Ako je narudžba uspješno napravljena, ispiši detalje
if nova_narudzba:
    print("\n PODACI O NARUDŽBI:")
    nova_narudzba.ispis_narudzbe()
