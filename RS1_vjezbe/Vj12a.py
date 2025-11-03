def obrni_rjecnik(rjecnik):
    novi_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():  # rjecnik.items() vraća parove (ključ, vrijednost)
        novi_rjecnik[vrijednost] = kljuc       # svaki par zamijenimo tako da nova vrijednost postane ključ, a stari ključ postane vrijednost
    return novi_rjecnik                        # novi rječnik novi_rjecnik se vraća kao rezultat


# Primjer upotrebe:
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))
