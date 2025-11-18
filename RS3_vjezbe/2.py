import asyncio

async def fetch_users():
    await asyncio.sleep(3)  # simulacija čekanja 3 sekunde
    return [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Marko"},
        {"id": 3, "name": "Iva"},
    ]

async def fetch_products():
    await asyncio.sleep(5)  # simulacija čekanja 5 sekundi
    return [
        {"id": 101, "product": "Laptop"},
        {"id": 102, "product": "Miš"},
        {"id": 103, "product": "Tipkovnica"},
    ]

async def main():
    users_data, products_data = await asyncio.gather(
        fetch_users(),
        fetch_products()
    )

    print("Korisnici:", users_data)
    print("Proizvodi:", products_data)

asyncio.run(main())
