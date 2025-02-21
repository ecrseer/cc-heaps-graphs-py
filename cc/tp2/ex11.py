import aiohttp
import asyncio
import time
import matplotlib.pyplot as plt


async def download_url(session, url):
    inicio = time.time()
    async with session.get(url) as response:
        content = await response.text()
        print(f"Downloaded {url}: {len(content)} bytes")
        print(f" {content[0:12]}")
        return time.time() - inicio


async def main():
    urls = ["https://g1.globo.com/rj/rio-de-janeiro", "https://pt.wikipedia.org/wiki/Teoria_dos_grafos",
            "https://www.themoviedb.org/collection/52749-the-butterfly-effect-collection?language=pt-BR"]
    tempos = []
    async with aiohttp.ClientSession() as session:
        tempos = await asyncio.gather(*(download_url(session, url) for url in urls))
        plot_this(urls, tempos)


def plot_this(concurrency_levels, times):
    plt.figure(figsize=(8, 5))
    plt.plot(concurrency_levels, times, marker='o', linestyle='-')
    plt.xlabel("site")
    plt.ylabel("Tempo total (segundos)")
    plt.title("Carregamento de sites")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    asyncio.run(main())
