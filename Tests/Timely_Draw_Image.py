from PIL import Image, ImageDraw, ImageFont
import ctypes
import time

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

fnt = ImageFont.truetype('calibrii.ttf', size=200)

x: int = 8000
while x >7999:
    img = Image.new(mode='1', size=screensize)
    drawObject = ImageDraw.Draw(img)
    time.sleep(1)
    drawObject.text(xy=(0, 0), text=str(x), fill=1, font=fnt)
    x -= 1
    img.save('Test.bmp')



