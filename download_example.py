import asyncio
import platform
from time import time
from pathlib import Path
import aiohttp

Path('files').mkdir(parents=True, exist_ok=True)
if platform.system() == 'Windows': asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def write_image(data):
    filename = 'files\\file_{}.jpg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
    write_image(data)


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main2())
