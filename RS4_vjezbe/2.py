import aiohttp
import asyncio
import time


# 1) Dohvaćanje jedne činjenice o mačkama (Korutina get_cat_fact — šalje GET zahtjev na adresu)
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    response = await session.get(url)
    data = await response.json()
    return data["fact"]   # vraća samo tekst činjenice


# 2) Filtriranje činjenica – bez HTTP poziva (Korutina filter_cat_facts - prima listu stringova i vraća samo one koje sadrže “cat” ili “cats”)
async def filter_cat_facts(facts):
    filtered = [fact for fact in facts 
                if "cat" in fact.lower() or "cats" in fact.lower()]
    return filtered


async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        # Izrada 20 taskova
        tasks = [
            asyncio.create_task(get_cat_fact(session))
            for _ in range(20)
        ]

        # Konkurentno izvršavanje i dohvaćanje svih rezultata odjednom
        cat_facts = await asyncio.gather(*tasks)

    # Filtriranje činjenica
    filtered_facts = await filter_cat_facts(cat_facts)

    # Ispis rezultata
    print("Filtrirane činjenice o mačkama:")
    for fact in filtered_facts:
        print("-", fact)

    end = time.perf_counter()
    print(f"\nVrijeme izvođenja programa: {end - start:.4f} sekundi")


# Pokretanje programa
asyncio.run(main())
