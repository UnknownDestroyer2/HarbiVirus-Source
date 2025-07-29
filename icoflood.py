import ctypes
import random
import time
import threading
from ctypes import wintypes
from win32api import GetSystemMetrics
import winsound

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)

error_sounds = [
    "SystemHand",
    "SystemExclamation",
    "SystemAsterisk",
    "SystemQuestion",
    "SystemDefault"
]

def invert_colors():
    dc = user32.GetDC(0)
    while True:
        # NULL rect means whole DC
        res = user32.InvertRect(dc, None)
        time.sleep(0.1)
    user32.ReleaseDC(0, dc)

def play_random_error_sound():
    while True:
        sound = random.choice(error_sounds)
        winsound.PlaySound(sound, winsound.SND_ALIAS | winsound.SND_ASYNC)
        time.sleep(random.uniform(0.5, 2.0))

def spawn_random_icons():
    dc = user32.GetDC(0)
    icons = [
        32512,  # IDI_APPLICATION
        32513,  # IDI_HAND
        32514,  # IDI_QUESTION
        32515,  # IDI_EXCLAMATION
        32516,  # IDI_ASTERISK
        32518,  # IDI_SHIELD
    ]
    while True:
        icon_id = random.choice(icons)
        hicon = user32.LoadIconW(None, icon_id)
        if hicon:
            x = random.randint(0, w - 32)
            y = random.randint(0, h - 32)
            user32.DrawIconEx(dc, x, y, hicon, 32, 32, 0, 0, 0x0003)
        time.sleep(0.001)
    user32.ReleaseDC(0, dc)

def draw_invert_shapes():
    dc = user32.GetDC(0)
    while True:
        left = random.randint(0, w-200)
        top = random.randint(0, h-200)
        right = left + random.randint(50, 200)
        bottom = top + random.randint(50, 200)
        
        rect = wintypes.RECT(left, top, right, bottom)
        
        # invertrect user32’de
        user32.InvertRect(dc, ctypes.byref(rect))

        # Ekstra şekil çizmek için mesela çerçeve
        pen = gdi32.CreatePen(0, 3, 0xFFFFFF)
        old_pen = gdi32.SelectObject(dc, pen)
        gdi32.MoveToEx(dc, left, top, None)
        gdi32.LineTo(dc, right, top)
        gdi32.LineTo(dc, right, bottom)
        gdi32.LineTo(dc, left, bottom)
        gdi32.LineTo(dc, left, top)
        gdi32.SelectObject(dc, old_pen)
        gdi32.DeleteObject(pen)

        time.sleep(0.0001)
    user32.ReleaseDC(0, dc)

def main():
    t1 = threading.Thread(target=invert_colors, daemon=True)
    t2 = threading.Thread(target=play_random_error_sound, daemon=True)
    t3 = threading.Thread(target=spawn_random_icons, daemon=True)
    t4 = threading.Thread(target=draw_invert_shapes, daemon=True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
