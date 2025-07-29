import pyautogui
import time
import threading
from PIL import Image, ImageGrab  # Image ve ImageGrab modüllerini doğru şekilde içe aktarın
import random

# Ekran boyutunu al
screen_width, screen_height = pyautogui.size()

# Efekti uygulamak için renk paleti (RGB formatında)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Ekranın kayma hızını ayarla
scroll_speed = 10  # Kayma miktarı
num_screens = 30  # Ekran sayısı (kaç kez çoğalacak)
alpha = 20  # Saydamlık (pencerenin ne kadar şeffaf olacağı)

# Ekranın çoğaltılması ve kayma işlemi
def create_animated_screens():
    # Ekranı yakala
    screenshot = ImageGrab.grab()

    # Ekranda her şeyi çoğalt
    for i in range(num_screens):
        screen_copy = screenshot.copy()

        # Saydamlıkla renkli bir kare ekle
        color = random.choice(colors)
        colored_square = Image.new("RGBA", (screen_width, screen_height), color + (alpha,))  # Renk + Alpha kanalını ekle

        # Çoğaltılan ekranı ekle
        screen_copy.paste(colored_square, (0, 0), colored_square)

        # Çoğaltılan ekranı göster (her yeni ekran altına doğru kayacak şekilde)
        screen_copy.show()

        # Kayma efekti yaratmak için biraz kaydırma
        move_screen_down(i * scroll_speed)

        time.sleep(0.05)  # Efektin daha yavaş görünmesi için küçük bir gecikme ekliyoruz

# Ekranı kaydırmak için fonksiyon
def move_screen_down(offset):
    pyautogui.scroll(-scroll_speed)  # Ekranı aşağı kaydır

# Ekran çoğaltma ve kayma işlemini başlat
thread = threading.Thread(target=create_animated_screens)
thread.daemon = True
thread.start()

# Program çalışmaya devam etsin
while True:
    time.sleep(1)
