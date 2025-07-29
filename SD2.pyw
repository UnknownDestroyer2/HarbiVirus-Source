import pyautogui
import random
import time
from PIL import Image, ImageDraw

# Ekran boyutunu al
screen_width, screen_height = pyautogui.size()

# Rastgele renk üret
def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Rastgele kavisli çizgi çiz
def draw_random_curve(draw):
    x1, y1 = random.randint(0, screen_width), random.randint(0, screen_height)
    x2, y2 = random.randint(0, screen_width), random.randint(0, screen_height)
    x3, y3 = random.randint(0, screen_width), random.randint(0, screen_height)
    x4, y4 = random.randint(0, screen_width), random.randint(0, screen_height)
    
    # Kavisli çizgiyi rastgele renk ile çiz
    draw.line([x1, y1, x2, y2, x3, y3, x4, y4], fill=random_color(), width=2)

# Çizim işlemi
def start_drawing():
    start_time = time.time()
    
    while time.time() - start_time < 15:
        # Ekran görüntüsü al ve üzerine çizim yap
        image = Image.new("RGB", (screen_width, screen_height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Rastgele kavis çiz
        draw_random_curve(draw)
        
        # Çizimi ekranda göster
        image.show()
        time.sleep(0.1)  # 0.1 saniye bekle

    # 15 saniye sonunda ekranı temizle (siyah bir ekran göster)
    image = Image.new("RGB", (screen_width, screen_height), (0, 0, 0))
    image.show()

# Çizimi başlat
start_drawing()
