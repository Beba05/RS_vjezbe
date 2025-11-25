import aiohttp
import asyncio
import time


# Korutina za dohvaćanje korisnika
async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    response = await session.get(url)
    return await response.json()  # JSON -> Python list/dict


async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:

        # priprema se 5 korutina konkurentno 
        tasks = [fetch_users(session) for _ in range(5)]

        # dohvaćanje svih rezultata odjednom
        results = await asyncio.gather(*tasks)

    # uzima se samo prvi rezultat, jer svih 5 vraća iste korisnike
    users = results[0]

    # izdvajanje u liste 
    names = [u["name"] for u in users]
    emails = [u["email"] for u in users]
    usernames = [u["username"] for u in users]

    end = time.perf_counter()

    print("Imena korisnika:", names)
    print("Email adrese:", emails)
    print("Usernames:", usernames)
    print(f"\nVrijeme izvođenja programa: {end - start:.4f} sekundi")


# pokretanje
asyncio.run(main())

