import aiohttp
import asyncio
import time
import matplotlib.pyplot as plt




async def download_url(session, url):
    inicio=time.time()
    async with session.get(url) as response:
        content = await response.text()
        print(f"Downloaded {url}: {len(content)} bytes")
        print(f" {content[0:12]}")
        return time.time()-inicio

async def main():
    urls = ["https://example.com", "https://httpbin.org/get", "https://jsonplaceholder.typicode.com/posts"]
    tempos = []
    async with aiohttp.ClientSession() as session:
        tempos=await asyncio.gather(*(download_url(session, url) for url in urls))
        plot_this(urls, tempos)



def plot_this(concurrency_levels, times):
    plt.figure(figsize=(8, 5))
    plt.plot(concurrency_levels, times, marker='o', linestyle='-')
    plt.xlabel("Número de tarefas assíncronas (concorrência)")
    plt.ylabel("Tempo total (segundos)")
    plt.title("Impacto da concorrência no tempo de download")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    asyncio.run(main())
