import asyncio
import random
# async def my_coroutine():
#     print('it started')
#     await asyncio.sleep(2)
#     print('it ended')

# async def main():
#     await my_coroutine()

# asyncio.run(main())

# async def count_to_three():
#     for i in range(1,4):
#         print(f'count {i}')
#         await asyncio.sleep(1)

# async def hello():
#     await count_to_three()
#     print("hello victor")
# async def main():
#     task1 = asyncio.create_task(count_to_three())
#     task2 = asyncio.create_task(hello())
#     await task1
#     await task2
# asyncio.run(main())

async def get_random_number(delay):
    await asyncio.sleep(delay)
    return random.randint(1, 10)


async def main():
    number = await get_random_number(3)
    print(f'random number: {number}')
asyncio.run(main())