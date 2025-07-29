import ctypes
import random
import time
from win32api import GetSystemMetrics
from win32gui import GetDC, ReleaseDC
from ctypes import windll, Structure, c_long

# Ekran genişliği ve yüksekliği al
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# POINT yapısını tanımla
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

# Rastgele renk üret
def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Rastgele kavisli çizgi çiz
def draw_random_curve(hdc):
    # Rastgele koordinatlar al
    x1, y1 = random.randint(0, screen_width), random.randint(0, screen_height)
    x2, y2 = random.randint(0, screen_width), random.randint(0, screen_height)
    x3, y3 = random.randint(0, screen_width), random.randint(0, screen_height)
    x4, y4 = random.randint(0, screen_width), random.randint(0, screen_height)

    # Renkleri ayarla
    r, g, b = random_color()
    pen_color = windll.gdi32.CreatePen(0, 2, (b << 16) | (g << 8) | r)
    old_pen = windll.gdi32.SelectObject(hdc, pen_color)
    
    # Kavisli çizgiyi çiz
    windll.gdi32.MoveToEx(hdc, x1, y1, None)

    # POINT dizisini oluştur
    points = (POINT(x2, y2), POINT(x3, y3), POINT(x4, y4))
    point_array = (POINT * 3)(*points)  # POINT dizisini ctypes ile oluştur
    windll.gdi32.PolyBezierTo(hdc, point_array, 3)

    # Kalemi serbest bırak
    windll.gdi32.SelectObject(hdc, old_pen)
    windll.gdi32.DeleteObject(pen_color)

# Çizim işlemi
def start_drawing():
    # Ekran DC'sini al
    hdc = GetDC(None)
    
    start_time = time.time()
    while time.time() - start_time < 98457894579845798457982374598374589234589723458728934578924753:
        draw_random_curve(hdc)
        time.sleep(0.1)  # 0.1 saniye bekle
    
    # Ekran DC'sini serbest bırak
    ReleaseDC(None, hdc)

# Çizimi başlat
start_drawing()
