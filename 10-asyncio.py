
# Asynchroniczność przy użyciu AsyncIO

import asyncio
import time

async def count(delay):
    print(f"start coroutine - {delay}")
    await asyncio.sleep(delay)
    print(f"end coroutine - {delay}")
    return delay

# async def main(): # synchroniczne wywołanie 2 funkcji zdefiniowych jako asynchroniczne
#     await count(5)
#     await count(3)

# # współbieżne uruchomienie
# # 2 funkcji zdefiniowych jako asynchroniczne i oczekiwanie na zakończenie zadań
# async def main():
#     task1 = asyncio.create_task(count(5))
#     task2 = asyncio.create_task(count(3))
#     result1 = await task1
#     result2 = await task2
#     print(result1, result2)

# async def main(): # zbieranie coroutines i oczkiwanie na zakonczenie
#     result = await asyncio.gather(count(5), count(3), count(7))
#     print(result)

# async def main(): # kto pierwszy, ten lepszy
#     tasks = [count(5), count(3), count(7)]
#     done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
#     print(done)
#     print(pending)

async def main():
    try:
        result = await asyncio.wait_for(
            asyncio.gather(count(5), count(3), count(7)),
            timeout=5
        )
        print(result)
    except asyncio.TimeoutError as exc:
        print(exc)


if __name__ == "__main__":
    asyncio.run(main())