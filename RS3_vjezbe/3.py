import asyncio

# baze podataka
baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_iz_baze, unesena_lozinka):
    '''Simulira autorizaciju korisnika (2 sekunde)'''
    await asyncio.sleep(2)

    # pronađi lozinku iz baze
    lozinka_iz_baze = next(
        (e['lozinka'] for e in baza_lozinka if e['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']),
        None
    )

    if lozinka_iz_baze is None:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Lozinka nije pronađena u bazi."

    # provjera lozinke (simulacija dekripcije)
    if unesena_lozinka == lozinka_iz_baze:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    '''Simulira autentifikaciju korisnika (3 sekunde)'''
    print("Pokrećem autentifikaciju...")
    await asyncio.sleep(3)

    korisnicko_ime = korisnik['korisnicko_ime']
    email = korisnik['email']
    lozinka = korisnik['lozinka']

    # provjera korisnika u bazi
    korisnik_iz_baze = next(
        (e for e in baza_korisnika if e['korisnicko_ime'] == korisnicko_ime and e['email'] == email),
        None
    )

    if korisnik_iz_baze is None:
        return f"Korisnik {korisnicko_ime} nije pronađen."

    # ako korisnik postoji → autorizacija
    rezultat = await autorizacija(korisnik_iz_baze, lozinka)
    return rezultat


async def main():
    # proizvoljan korisnik
    korisnik = {
        "korisnicko_ime": "ana_anic",
        "email": "aanic@gmail.com",
        "lozinka": "super_teska_lozinka"
    }

    rezultat = await autentifikacija(korisnik)
    print(rezultat)


asyncio.run(main())
