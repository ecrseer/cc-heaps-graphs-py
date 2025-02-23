import asyncio
import time

from PIL import Image, ImageFilter
import os
import matplotlib.pyplot as plt


async def process_image(image_path, output_dir, imagens_filtradas, index_atual):
    inicio_segs = time.time()
    img = Image.open(image_path)
    img = img.filter(ImageFilter.CONTOUR)
    salvar_em = os.path.join(output_dir, os.path.basename(image_path))
    img.save(salvar_em)

    name = os.path.basename(image_path)
    kbytes=os.path.getsize(image_path) / 1000

    imagens_filtradas[f'{name}-{kbytes}KByt'] = {
        'tempo': time.time() - inicio_segs,
        'index': index_atual
    }


async def main_image_processing():
    images_horarios = {}

    input_dir = "input_images"
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)

    images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]


    threads_tarefas = [process_image(img, output_dir, images_horarios, index) for index, img in enumerate(images)]
    await asyncio.gather(*threads_tarefas)

    imagens=[img for img in images_horarios]
    tempos= [images_horarios[img]['tempo'] for img in images_horarios]
    print(f'imagens:{imagens}')
    print(f'tempos:{tempos}')
    plot_this(imagens, tempos)




def plot_this(concurrency_levels, times):
    plt.figure(figsize=(18, 5))
    plt.plot(concurrency_levels, times, marker='o', linestyle='-')
    plt.xlabel("nome imagem")
    plt.ylabel("Tempo total (segundos)")
    plt.title("Filtro em imagens")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    asyncio.run(main_image_processing())
