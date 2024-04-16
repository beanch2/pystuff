import win32gui
import win32con
import win32api
import win32com.client
import math
import time
import random
import ctypes
import subprocess
def sines():
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    angle = 0

    while True:
        hdc = win32gui.GetWindowDC(desktop)
        for i in range(int(sw + sh)):
            a = int(math.sin(angle) * 220)
            win32gui.BitBlt(hdc, 1 + 1, 1 + 1, sw, i, hdc, a, i, win32con.SRCCOPY)
            win32gui.BitBlt(hdc, 1 + 1, 1 + 131, sw, i, hdc, a, i + 92, win32con.SRCCOPY)
            angle += math.pi / 1 + 11
        win32gui.ReleaseDC(desktop, hdc)
        time.sleep(0)
        if time.time() - start_time >= 30:
            break

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 

start_time = time.time()
sines()

while True:
    if time.time() - start_time >= 50:
        break
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
while True:
    hdc = win32gui.GetDC(0)
    color = (random.randint(0, 123422), random.randint(0, 4302343), random.randint(0, 310))
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 12430), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 12340), sw, sh, hdc, 0, 0, win32con.PATINVERT)
while True:
    if time.time() - start_time >= 30:
        break
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
dx = dy = 1
angle = 0
size = 1
speed = 500
while True:
    
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
    dx = math.ceil(math.sin(angle) * size * 10)
    dy = math.ceil(math.cos(angle) * size * 110)
    angle += speed / 10
    if angle > math.pi :
        angle = math.pi * -1
