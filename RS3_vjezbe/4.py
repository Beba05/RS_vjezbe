import asyncio
import random

async def provjeri_parnost(broj: int) -> str:
    """Simulira super zahtjevnu provjeru parnosti (API poziv od 2 sekunde)."""
    await asyncio.sleep(2)  # simulacija čekanja vanjskog API-ja
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

async def main():
    # 10 nasumičnih brojeva od 1 do 100 (uključivo), kroz list comprehension
    brojevi = [random.randint(1, 100) for _ in range(10)]
    print("Generirani brojevi:", brojevi)

    # lista Task objekata koji pozivaju provjeri_parnost za svaki broj
    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]

    # konkurentno izvršavanje svih korutina
    rezultati = await asyncio.gather(*zadaci)

    # ispis rezultata
    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
