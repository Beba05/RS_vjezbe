import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f"Dovršio sam s {param}.")
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))   # schedule
    task2 = asyncio.create_task(fetch_data(2))   # schedule

    # awaitamo SAMO task1
    result1 = await task1  # čeka samo task1, ali NE i task2
    print("Fetch 1 uspješno završen.")

    # ne awaitamo task2, ali ostavimo event-loop živim dovoljno dugo
    await asyncio.sleep(2.1)   # drži event loop aktivnim još ~2 sekunde, pa task2 dobiva vremena

    return [result1]


t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()

print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
