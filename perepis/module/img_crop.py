from PIL import Image

def crop_img_to_review(path):
    # Создаем объект изобажения
    img = Image.open(path)
    # Проверяем его чтобы не был слишком мал
    if img.height > 88 or img.width > 77:
        # Обрезаем его так чтобы одна из сторон была не больше 100
        output_size = (100,100)
        img.thumbnail(output_size)
        # Вырезаем центр чтобы поместился в окошко
        new_img = img.crop(((img.width- 77) // 2,(img.height - 88) // 2,(img.width + 77) // 2,(img.height + 88) // 2))
        # Сохраняем изображение
        new_img.save(path, quality=95)