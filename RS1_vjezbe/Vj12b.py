# kraća verzija pomoću dictionary comprehensiona

def obrni_rjecnik(rjecnik):
    return {vrijednost: kljuc for kljuc, vrijednost in rjecnik.items()}

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))