# # Zadanie 10.1
# from PIL import Image
#
# img = Image.open("postcards/otkritka_kotik_dr.jpg")
# width, height = img.size
#
# print(f"Размер картинки: {width} x {height}")
#
# left = 0
# top = 225
# right = width
# bottom = height
#
# cropped = img.crop((left, top, right, bottom))
#
# cropped.save("postcards/otkritka_kotik_dr_cropped.jpg")
#
# print(f" Обрезано! Новый размер: {cropped.size[0]} x {cropped.size[1]}")
# cropped.show()



# # Zadanie 10.2
# from PIL import Image
# import os
#
# cards = {
#     "1": ("8 Марта", "postcards/s_8_marta.jpg"),
#     "2": ("День матери", "postcards/s_dnem_materi.jpg"),
#     "3": ("День влюбленных", "postcards/s_dnem_vlublennih.jpg"),
#     "4": ("День рождения", "postcards/s_dr.jpg"),
#     "5": ("Новый год", "postcards/s_novim_godom.jpg")
# }
#
# print("\nОТКРЫТКИ ПО ПРАЗДНИКАМ \n")
#
# for key, (name, path) in cards.items():
#     if os.path.exists(path):
#         print(f"{key}. {name}")
#     else:
#         print(f"{key}. {name} (файл отсутствует)")
#
# choice = input("\nВведите номер праздника: ")
#
# if choice in cards:
#     name, path = cards[choice]
#     if os.path.exists(path):
#         img = Image.open(path)
#         print(f"\nОткрываю открытку: {name}")
#         img.show()




# Zadanie 10.3
from PIL import Image, ImageDraw, ImageFont
import os

image_path = "postcards/s_dr.jpg"
name = input("Кого поздравляем? ")

img = Image.open(image_path).convert("RGBA")
width, height = img.size

text_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(text_layer)

text = f"{name}, поздравляю!"

font_size = height // 12

try:
    font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", font_size)
except:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (width - text_width) // 2
y = 12

draw.text((x, y), text, fill=(255, 0, 0, 255), font=font)

result = Image.alpha_composite(img, text_layer)
output_filename = f"postcards/greeting_{name}.png"
result.convert("RGB").save(output_filename)

print(f" Открытка сохранена: {output_filename}")
result.show()








