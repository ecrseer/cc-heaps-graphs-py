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
    urls = [
        "https://g1.globo.com/rj/rio-de-janeiro",
        "https://pt.wikipedia.org/wiki/Teoria_dos_grafos",
        "https://www.themoviedb.org/collection/52749-the-butterfly-effect-collection?language=pt-BR",
        "https://www.correios.com.br/",
        "https://www.uol.com.br/",
        "https://www.terra.com.br/",
        "https://www.folha.uol.com.br/",
        "https://www.estadao.com.br/",
        "https://www.bbc.com/portuguese",
        "https://www.reclameaqui.com.br/",
        "https://www.mercadolivre.com.br/",
        "https://www.gov.br/",
        "https://www.infomoney.com.br/",
        "https://www.olx.com.br/",
        "https://lms.infnet.edu.br/moodle",
        "https://g1.globo.com/"
    ]

    tempo_testes = []
    async with aiohttp.ClientSession() as session:
        testes = [16, 8, 4, 2]
        for qtd_threads in testes:
            inicio = time.time()
            requisicoes = urls[0:qtd_threads]
            downloads_gnrs = (download_url(session, url) for url in requisicoes)
            await asyncio.gather(*downloads_gnrs)
            duracao = time.time() - inicio
            tempo_testes.append(duracao)

        plot_this(testes, tempo_testes)


def plot_this(concurrency_levels, times):
    plt.figure(figsize=(18, 5))
    plt.plot(concurrency_levels, times, marker='o', linestyle='-')
    plt.xlabel("Quantidade sites(threads)")
    plt.ylabel("Tempo total (milissegundos)")
    plt.title("Carregamento de sites simultaneos")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    asyncio.run(main())
