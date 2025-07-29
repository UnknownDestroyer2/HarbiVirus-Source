import ctypes
import random
import time
from ctypes import wintypes
from win32api import GetSystemMetrics
from win32gui import GetDC, ReleaseDC

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)

def crazy_step():
    dc = GetDC(0)
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        rw = random.randint(200, w)
        rh = random.randint(200, h)
        ctypes.windll.gdi32.BitBlt(dc, x, y, rw, rh, dc, 0, 0, 0x00CC0020)
    ReleaseDC(0, dc)

def rainbow_flood():
    dc = GetDC(0)
    for _ in range(20):
        color = random.randint(0, 0xFFFFFF)
        brush = ctypes.windll.gdi32.CreateSolidBrush(color)
        left   = random.randint(0, w)
        top    = random.randint(0, h)
        right  = random.randint(0, w)
        bottom = random.randint(0, h)
        rect = wintypes.RECT(left, top, right, bottom)
        ctypes.windll.user32.FillRect(dc, ctypes.byref(rect), brush)
        ctypes.windll.gdi32.DeleteObject(brush)
    ReleaseDC(0, dc)

def main():
    try:
        while True:
            crazy_step()
            rainbow_flood()
            time.sleep(0.02)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
