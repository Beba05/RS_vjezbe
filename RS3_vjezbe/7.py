import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

'''Event loop bira PENDING taskove redom kako su zakazani. 
Za svaki timer task, stanja idu ovim redoslijedom:
1. PENDING nakon asyncio.create_task(...). Spreman za izvršavanje čim loop dođe na red.
2. RUNNING kad event loop prvi put uđe u korutinu i dođe do prvog await asyncio.sleep.
3. WAITING kad korutina dođe do await asyncio.sleep(1) i preda kontrolu event loopu.
4. ponovno RUNNING kad istekne sleep i event loop vrati kontrolu korutini.
5. DONE nakon što korutina izađe iz funkcije (dođe do kraja).
Event loop: stalno traži READY/RUNNING taskove,
kad naiđe na await (npr. sleep), task pauzira i loop prelazi na idući,
time se postiže “konkurentnost” (interleaving ispisa za više timera).'''