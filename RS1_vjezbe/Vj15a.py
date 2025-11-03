# Petljom prolazimo kroz svaki znak u stringu tekst.
# Ako je znak u vowels → povećavamo broj samoglasnika.
# Ako je znak u consonants → povećavamo broj suglasnika.
# Interpunkcija, razmaci i brojevi se preskaču (nisu ni jedno ni drugo).
# Na kraju funkcija vraća rječnik s rezultatima

def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    rezultat = {'samoglasnici': 0, 'suglasnici': 0}

    for znak in tekst:
        if znak in vowels:
            rezultat['samoglasnici'] += 1
        elif znak in consonants:
            rezultat['suglasnici'] += 1

    return rezultat


# Primjer upotrebe:
tekst = "Python je zabavan programski jezik!"
print(count_vowels_consonants(tekst))
