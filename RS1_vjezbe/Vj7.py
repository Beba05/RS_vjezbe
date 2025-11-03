def provjera_lozinke(lozinka):
    # 1. Provjera duljine
    # len(lozinka) — provjerava duljinu stringa
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
        return

    # 2. Provjera barem jednog velikog slova i jednog broja
    # any(znak.isupper() for znak in lozinka) — traži barem jedno veliko slovo
    ima_veliko = any(znak.isupper() for znak in lozinka)
    # any(znak.isdigit() for znak in lozinka) — traži barem jedan broj
    ima_broj = any(znak.isdigit() for znak in lozinka)
    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
        return

    # 3. Provjera zabranjenih riječi "password" ili "lozinka"
    # lozinka.lower() — normalizira unos na mala slova da se provjera "password" i "lozinka" ne ovisi o veličini slova
    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
        return

    # Ako su svi uvjeti zadovoljeni
    print("Lozinka je jaka!")


# --- Glavni dio programa ---
unos = input("Unesi lozinku za provjeru: ")
provjera_lozinke(unos)