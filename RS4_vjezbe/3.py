import aiohttp
import asyncio
import time


# Helper funkcija za retry logiku
async def fetch_with_retry(session, url, extract_fn, retries=3):
    for attempt in range(retries):
        response = await session.get(url)

        if response.status == 200:
            data = await response.json()
            return extract_fn(data)

        # Ako je API rate-limited (429), čekamo i probamo ponovo
        if response.status == 429:
            await asyncio.sleep(1)
            continue

        # Ostale greške — odmah vraćamo fallback
        return f"Fact unavailable (status {response.status})"

    # Ako ni nakon retry ne uspije
    return "Fact unavailable after retries"


# 1) Dohvat dog facta
async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"

    def extract(data):
        try:
            return data["data"][0]["attributes"]["body"]
        except:
            return "Dog fact unavailable (invalid JSON format)"

    return await fetch_with_retry(session, url, extract)


# 2) Dohvat cat facta
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"

    def extract(data):
        return data.get("fact", "Cat fact unavailable (no fact key)")

    return await fetch_with_retry(session, url, extract)


# 3) Mix funkcija
async def mix_facts(dog_facts, cat_facts):
    mixed = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed.append(dog_fact)
        else:
            mixed.append(cat_fact)
    return mixed


async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:

        # 5 dog taskova
        dog_tasks = [
            asyncio.create_task(get_dog_fact(session))
            for _ in range(5)
        ]

        # 5 cat taskova
        cat_tasks = [
            asyncio.create_task(get_cat_fact(session))
            for _ in range(5)
        ]

        # gather uvijek vraća redoslijedom kreiranja taskova
        all_facts = await asyncio.gather(*dog_tasks, *cat_tasks)

    # slicing
    dog_facts = all_facts[:5]
    cat_facts = all_facts[5:]

    # mix
    mixed_facts = await mix_facts(dog_facts, cat_facts)

    # ispis
    print("Mixane činjenice o psima i mačkama:")
    for fact in mixed_facts:
        print(fact)

    end = time.perf_counter()
    print(f"\nVrijeme izvođenja programa: {end - start:.4f} sekundi")


asyncio.run(main())

