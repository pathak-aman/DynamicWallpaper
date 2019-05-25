from PIL import Image, ImageDraw, ImageFont

import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

img = Image.new(mode='RGB', size=screensize, color=(10, 10, 10))
drawObject = ImageDraw.Draw(img)
fnt = ImageFont.truetype('calibrii.ttf', size=200)
img.show(img)
