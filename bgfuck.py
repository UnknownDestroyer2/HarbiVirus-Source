import os
import ctypes
import random
from PIL import Image, ImageDraw, ImageFont

def get_wallpaper_path():
    SPI_GETDESKWALLPAPER = 0x0073
    buffer = ctypes.create_unicode_buffer(260)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 260, buffer, 0)
    return buffer.value

def backup_wallpaper(wallpaper_path, backup_path):
    if os.path.exists(wallpaper_path):
        with open(wallpaper_path, "rb") as fsrc:
            with open(backup_path, "wb") as fdst:
                fdst.write(fsrc.read())
        print(f"Yedek alındı: {backup_path}")
    else:
        print("Wallpaper bulunamadı.")

def karistir_renkler_ve_yaz(image_path, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    # Renkleri karıştırıyoruz lan
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r + random.randint(-150, 150)) % 256
            g = (g + random.randint(-150, 150)) % 256
            b = (b + random.randint(-150, 150)) % 256
            pixels[i, j] = (r, g, b)

    draw = ImageDraw.Draw(img)
    try:
        font_path = "C:/Windows/Fonts/arialbd.ttf"
        font_size = int(height / 15)  # makul bi büyüklük
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    text = "HACKED BY UNKNOWN DESTROYER"

    # Yazının ölçüsünü alıyoruz, tam ortaya koymak için
    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2 - bbox[0]
        y = (height - text_height) // 2 - bbox[1]
    else:
        text_width, text_height = font.getsize(text)
        x = (width - text_width) // 2
        y = (height - text_height) // 2

    shadow_color = (255, 0, 0)
    text_color = (255, 255, 255)
    outline_range = 2

    # Gölge efekti saçmalığı
    for ox in range(-outline_range, outline_range + 1):
        for oy in range(-outline_range, outline_range + 1):
            draw.text((x + ox, y + oy), text, font=font, fill=shadow_color)

    # Asıl beyaz yazı
    draw.text((x, y), text, font=font, fill=text_color)

    img.save(output_path)
    print(f"Karışık renkli ve yazılı arka plan kaydedildi: {output_path}")

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print("Arka plan değiştirildi.")

def main():
    wallpaper_path = get_wallpaper_path()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    backup_path = os.path.join(desktop_path, "wallpaper_backup.bmp")
    output_path = os.path.join(desktop_path, "wallpaper_karisik_hacked.bmp")

    if not wallpaper_path or not os.path.exists(wallpaper_path):
        print("Arka plan resmi bulunamadı.")
        return

    backup_wallpaper(wallpaper_path, backup_path)
    karistir_renkler_ve_yaz(wallpaper_path, output_path)
    set_wallpaper(output_path)

if __name__ == "__main__":
    main()
