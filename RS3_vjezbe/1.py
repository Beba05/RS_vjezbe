import asyncio

# korutina koja simulira dohvaćanje podataka
async def dohvat_podataka():
    await asyncio.sleep(3)  # simulacija čekanja 3 sekunde
    podaci = [x for x in range(1, 11)]  # lista 1–10 comprehensionom
    print("Podaci dohvaćeni.")
    return podaci

# glavni dio programa
async def main():
    rezultat = await dohvat_podataka()  # poziv korutine
    print("Dohvaćeni podaci:", rezultat)

# pokretanje event loopa
asyncio.run(main())
