import threading
import time
import ctypes
import win32con
import win32gui

import numpy as np
from PIL import Image, ImageTk
import mss
import tkinter as tk

# 1) Ekran boyutları
user32 = ctypes.windll.user32
WIDTH  = user32.GetSystemMetrics(0)
HEIGHT = user32.GetSystemMetrics(1)

# 2) Overlay penceresi (click‑through)
root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry(f"{WIDTH}x{HEIGHT}+0+0")
root.wm_attributes("-transparentcolor", "black")
root.config(bg="black")

label = tk.Label(root, bg="black")
label.pack(fill='both', expand=True)

hwnd = ctypes.windll.user32.GetForegroundWindow()
ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
ex_style |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)

# 3) Yakalama + invert döngüsü
def invert_loop():
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": WIDTH, "height": HEIGHT}
        while True:
            # a) ekranı al
            sct_img = sct.grab(monitor)                         # mss ile gerçek zamanlı al
            arr    = np.array(sct_img)                          # BGRA array
            rgb    = arr[..., :3]                               # RGB kanallar
            inv    = 255 - rgb                                  # invert
            img    = Image.fromarray(inv)                       # PIL Image
            tkimg  = ImageTk.PhotoImage(img)                    # TK Image

            # b) önceki frame’i otomatik siler, çünkü aynı widget’a overwrite
            label.config(image=tkimg)
            label.image = tkimg

            time.sleep(0.02)    # ~50 FPS

# 4) Thread & mainloop
threading.Thread(target=invert_loop, daemon=True).start()
root.mainloop()
