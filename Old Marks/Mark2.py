import ctypes
import time

from PIL import Image, ImageDraw, ImageFont

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

fnt = ImageFont.truetype('calibrii.ttf', size=200)

x: int = 80
while x != 0:
    time.sleep(1)
    img = Image.new(mode='1', size=screensize)
    drawObject = ImageDraw.Draw(img)
    drawObject.text(xy=(400, 100), text="You have", fill=1, font=fnt)
    drawObject.text(xy=(400, 300), text=str(x) + " seconds", fill=1, font=fnt)
    drawObject.text(xy=(400, 500), text="remaining", fill=1, font=fnt)
    x -= 1
    img.save('Test.bmp')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\Coding\DynamicWallpaper\Test.bmp', 0)
