import ctypes
import time
import datetime

from PIL import Image, ImageDraw, ImageFont

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

fnt300 = ImageFont.truetype('Fonts/GreycliffCF-DemiBold.ttf', size=300)
fnt100 = ImageFont.truetype('Fonts/GreycliffCF-Regular.ttf', size=100)

SECONDSINDAY = 24 * 3600

while True:
    currentDT = datetime.datetime.now()
    tot_seconds = currentDT.hour * 3600 + currentDT.minute * 60 + currentDT.second
    x = SECONDSINDAY - tot_seconds
    time.sleep(1)
    img = Image.new(mode='RGB', size=screensize, color=(0, 0, 0))
    draw_object = ImageDraw.Draw(img)
    draw_object.text(xy=(600, 50), text="You have", fill=(255, 255, 255), font=fnt100)
    draw_object.text(xy=(420, 150), text=str(x), fill=(255, 255, 255), font=fnt300)
    draw_object.text(xy=(400, 500), text="seconds left today", fill=(255, 255, 255), font=fnt100)
    img.save('Image\\Test.bmp')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\\Coding\\DynamicWallpaper\\Image\\Test.bmp", 0)