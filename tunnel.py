import ctypes
from ctypes import wintypes
import time
import random
import threading


user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32  = ctypes.WinDLL('gdi32',  use_last_error=True)


SRCCOPY       = 0x00CC0020
MB_OK         = 0x00000000
MB_ICONERROR  = 0x00000010
MB_ICONWARNING= 0x00000030


user32.GetDC.argtypes    = [wintypes.HWND]
user32.GetDC.restype     = wintypes.HDC
user32.ReleaseDC.argtypes= [wintypes.HWND, wintypes.HDC]
user32.ReleaseDC.restype = ctypes.c_int
user32.GetSystemMetrics.argtypes = [ctypes.c_int]
user32.GetSystemMetrics.restype  = ctypes.c_int
gdi32.StretchBlt.argtypes = [
    wintypes.HDC, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    wintypes.HDC, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    wintypes.DWORD
]
gdi32.StretchBlt.restype = wintypes.BOOL
user32.MessageBoxW.argtypes = [wintypes.HWND, wintypes.LPCWSTR, wintypes.LPCWSTR, ctypes.c_uint]
user32.MessageBoxW.restype  = ctypes.c_int

def tunnel_forever(offset=8, delay=0.02):
   
    hdc = user32.GetDC(None)
    w = user32.GetSystemMetrics(0)
    h = user32.GetSystemMetrics(1)
    try:
        while True:
            la
            gdi32.StretchBlt(
                hdc,
                offset, offset,
                w - 2*offset, h - 2*offset,
                hdc,
                0, 0,
                w, h,
                SRCCOPY
            )
            time.sleep(delay)
    finally:
        user32.ReleaseDC(None, hdc)

def random_msgbox_loop():
    titles = ["Sistem Hatası", "Uyarı", "Critical Error", "Dikkat!"]
    errors = ["Bilinmeyen hata oluştu.", "Veri bozulması tespit edildi.", 
              "Bellek taşması!", "Erişim reddedildi."]
    warns  = ["Disk dolmak üzere!", "Bağlantı kopabilir.", 
              "Güncelleme önerisi.", "Düşük pil seviyesi."]
    while True:
        time.sleep(random.uniform(5, 15))  
        if random.random() < 0.5:
        
            user32.MessageBoxW(None,
                                random.choice(errors),
                                random.choice(titles),
                                MB_OK | MB_ICONERROR)
        else:
           
            user32.MessageBoxW(None,
                                random.choice(warns),
                                random.choice(titles),
                                MB_OK | MB_ICONWARNING)

if __name__ == "__main__":
   
    threading.Thread(target=random_msgbox_loop, daemon=True).start()
  
    try:
        tunnel_forever(offset=8, delay=0.02)
    except KeyboardInterrupt:
        pass
