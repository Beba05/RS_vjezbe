import asyncio

async def secure_data(podaci: dict) -> dict:
    """Simulira enkripciju osjetljivih podataka (3 sekunde)."""
    await asyncio.sleep(3)  # simulacija enkripcije na poslužitelju

    prezime = podaci['prezime']
    broj_kartice = podaci['broj_kartice']
    cvv = podaci['CVV']

    # "Lažna" enkripcija korištenjem hash funkcije
    return {
        'prezime': prezime,
        'broj_kartice': hash(str(broj_kartice)),
        'CVV': hash(str(cvv))
    }

async def main():
    # 3 rječnika osjetljivih podataka
    osjetljivi_podaci = [
        {"prezime": "Horvat", "broj_kartice": "4567123412341234", "CVV": "321"},
        {"prezime": "Anić", "broj_kartice": "5500123412349876", "CVV": "987"},
        {"prezime": "Kovač", "broj_kartice": "4111222233334444", "CVV": "555"},
    ]

    # lista Task objekata koristeći list comprehension
    zadaci = [asyncio.create_task(secure_data(p)) for p in osjetljivi_podaci]

    # konkurentna enkripcija svih podataka
    rezultati = await asyncio.gather(*zadaci)

    # ispis rezultata
    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
