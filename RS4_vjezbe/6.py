import asyncio
import random
import time


# 1) Mikroservis - simulacija vremenske stanice
async def fetch_weather_data(station_id: int):
    # nasumično kašnjenje između 1 i 5 sekundi
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)

    # generira se temperatura između 20 i 25 °C
    temp = random.uniform(20, 25)
    print(f"Stanica {station_id}: temperatura = {temp:.2f} °C (kašnjenje {delay:.2f}s)")
    return temp


async def main():
    start = time.perf_counter()

    tasks = []
    for station_id in range(1, 10 + 1):
        # svaki zadatak ograničava se timeoutom od 2 sekunde
        task = asyncio.wait_for(fetch_weather_data(station_id), timeout=2)
        tasks.append(task)

    print("Pokrećem paralelno dohvaćanje podataka...\n")

    results = []
    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            results.append(result)
        except asyncio.TimeoutError:
            print("Jedna vremenska stanica nije odgovorila na vrijeme (timeout).")
            results.append(None)

    # filtriranje stanica koje nisu dale rezultat
    valid_temperatures = [temp for temp in results if temp is not None]

    if valid_temperatures:
        prosjek = sum(valid_temperatures) / len(valid_temperatures)
        print(f"\nProsječna temperatura svih funkcionalnih stanica: {prosjek:.2f} °C")
    else:
        print("\nNema dostupnih podataka. Sve stanice su zakazale.")

    end = time.perf_counter()
    print(f"\nVrijeme izvođenja: {end - start:.2f} sekundi")


asyncio.run(main())
