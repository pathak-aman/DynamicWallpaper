# reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d E:\photos\image1.bmp /f
# RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters


import subprocess
subprocess.call('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d D:\Coding\DynamicWallpaper\Test.bmp /f',shell=True)
subprocess.call('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters', shell=True)