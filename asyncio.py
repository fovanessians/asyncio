import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def newF(secDel):
    await asyncio.sleep(secDel)
    print(time.time())

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello')) # not block here

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}") # time0
    
    await task1 # block here!
    await newF(20)
    
    print(f"finished at {time.strftime('%X')}") 

    await task2 # block here!

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
