import asyncio

async def task1():
    print("start task1")
    await asyncio.sleep(2)
    print("end task1")

async def task2():
    print("start task2")
    await asyncio.sleep(1)
    print("end task2")


async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
