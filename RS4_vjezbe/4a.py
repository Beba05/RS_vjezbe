import asyncio

# baza korisnika
korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

# normalna autentifikacija
async def autentifikacija(username, password):
    print(f"Autentificiram {username} ...")
    await asyncio.sleep(2)   # simulacija sporog I/O

    if username in korisnici and korisnici[username] == password:
        return True
    
    # pogrešni podaci
    raise ValueError(f"Neuspješna autentifikacija za korisnika {username}")



async def main():
    # kreira se 5 konkurentnih poziva, neki s krivim podacima
    tasks = [
        autentifikacija("korisnik1", "lozinka1"),  # OK
        autentifikacija("korisnik2", "pogresno"),  # greška
        autentifikacija("korisnik3", "lozinka3"),  # OK
        autentifikacija("nepoznat", "xxx"),        # greška
        autentifikacija("korisnik1", "krivo"),     # greška
    ]

    print("\n--- Testiranje autentifikacije ---")
    try:
        results = await asyncio.gather(*tasks)
    except Exception as e:
        print("\nDOGODILA SE IZUZETAK u jednoj od korutina!")
        print("Tip iznimke:", type(e).__name__)
        print("Poruka:", e)


asyncio.run(main())

