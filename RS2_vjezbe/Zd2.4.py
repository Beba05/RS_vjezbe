studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

# map() prolazi kroz sve studente i vraća True ili False za svakog, ovisno o tome ima li 18 ili više godina.
# all() vraća True samo ako su svi elementi u mapi True
svi_punoljetni = all(map(lambda s: s["godine"] >= 18, studenti))

print(svi_punoljetni)  # False (Budući da Petra (13) i Iva (17) nisu punoljetne, rezultat je False)
