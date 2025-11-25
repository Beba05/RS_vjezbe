import aiohttp
import asyncio
import time


# Asinkrona korutina za dohvat sadržaja URL-a
async def fetch_url(session, url: str) -> str:
    async with session.get(url, timeout=5) as response:
        return await response.text()


async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        # stvaranje korutine za sve URL-ove
        tasks = [fetch_url(session, url) for url in urls]

        # izvršava se konkurentno uz gather
        results = await asyncio.gather(*tasks)

    # ispis rezultata
    for url, content in zip(urls, results):
        print(f"Fetched {len(content)} characters from {url}")

    end = time.perf_counter()
    print(f"\nVrijeme izvođenja: {end - start:.4f} sekundi")


if __name__ == "__main__":
    asyncio.run(main())

