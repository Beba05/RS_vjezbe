import asyncio


# simulirani pad servisa nakon 3 sekunde
async def autentifikacija(username, password):
    print(f"Autentificiram {username} ...")
    await asyncio.sleep(3)     # servis čeka pred dugo
    raise TimeoutError("Autentifikacijski servis ne odgovara.")


async def main():
    tasks = [
        asyncio.wait_for(autentifikacija("kor1", "pass"), timeout=2),
        asyncio.wait_for(autentifikacija("kor2", "pass"), timeout=2),
        asyncio.wait_for(autentifikacija("kor3", "pass"), timeout=2),
        asyncio.wait_for(autentifikacija("kor4", "pass"), timeout=2),
        asyncio.wait_for(autentifikacija("kor5", "pass"), timeout=2),
    ]

    print("\n--- Testiranje timeout scenarija ---")
    try:
        results = await asyncio.gather(*tasks)
    except Exception as e:
        print("\nDOGODIO SE IZUZETAK:")
        print("Tip:", type(e).__name__)
        print("Poruka:", e)


asyncio.run(main())
