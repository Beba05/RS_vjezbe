import random

# Program nasumično bira broj između 1 i 100
# random.randint(1, 100) bira nasumičan broj iz raspona 1–100.
tajni_broj = random.randint(1, 100)
# Varijabla broj_je_pogoden kontrolira trajanje igre.
broj_je_pogoden = False
broj_pokusaja = 0

print("Pogodi broj između 1 i 100!")

# Petlja traje dok korisnik ne pogodi broj
# while not broj_je_pogoden: omogućava da se igra nastavlja sve dok korisnik ne pogodi broj.
while not broj_je_pogoden:
    # Unos korisnika
    try:
        unos = int(input("Unesi svoj pokušaj: "))
    except ValueError:
        print("Molim te, unesi cijeli broj!")
        continue

# Broj pokušaja se broji pomoću broj_pokusaja += 1.
    broj_pokusaja += 1

    # Provjera unosa
    if unos < tajni_broj:
        print("Traženi broj je VEĆI od tvog unosa.")
    elif unos > tajni_broj:
        print("Traženi broj je MANJI od tvog unosa.")
    else:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")