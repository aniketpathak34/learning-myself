import asyncio
import time

async def main():
    await asyncio.gather(task("A"), task("B"))

async def task(name):
    start = time.perf_counter()
    print(f"start {name}")
    await asyncio.sleep(2)
    print(f"done {name}")
    end = time.perf_counter()
    print(end - start)

start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print(end - start)
