from PIL import Image, ImageDraw, ImageFont
import ctypes
import time
import subprocess

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

fnt = ImageFont.truetype('calibrii.ttf', size=200)

x: int = 80
while x != 0:
    time.sleep(1)
    img = Image.new(mode='1', size=screensize)
    drawObject = ImageDraw.Draw(img)
    drawObject.text(xy=(800, 0), text=str(x), fill=1, font=fnt)
    x -= 1
    img.save('Test.bmp')
    subprocess.call(
        'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d D:\Coding\DynamicWallpaper\Test.bmp /f',
        shell=True)
    output = subprocess.call('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters 1, True', shell=True)
