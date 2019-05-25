from PIL import Image, ImageDraw
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

img = Image.new(mode= '1', size = screensize)
img.show(img)
