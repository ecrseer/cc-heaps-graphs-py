import asyncio
import time

from PIL import Image, ImageFilter
import os


async def process_image(image_path, output_dir, imagens_filtradas, index_atual):
    img = Image.open(image_path)
    img = img.filter(ImageFilter.CONTOUR)
    salvar_em = os.path.join(output_dir, os.path.basename(image_path))
    img.save(salvar_em)

    imagens_filtradas[f'{image_path}'] = {
        'tempo': time.time(),
        'index': index_atual
    }


async def main_image_processing():
    images_horarios = {'inicio': {
        'tempo': time.time()
    }}

    input_dir = "input_images"
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)

    images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]


    threads_tarefas = [process_image(img, output_dir, images_horarios, index) for index, img in enumerate(images)]
    await asyncio.gather(*threads_tarefas)


    for image in images_horarios:
        if(image == 'inicio'):
            continue
        images_horarios[image]['tempo'] = images_horarios[image]['tempo'] - images_horarios['inicio']['tempo']
        images_horarios[image]['tempo'] = round(images_horarios[image]['tempo'], 4)

    print(f'gab: {images_horarios}')


if __name__ == '__main__':
    asyncio.run(main_image_processing())
