import tkinter as tk
import os
import time
import platform
import threading

# Animasyon için yazı oluşturucu
def animate_text(label, text, delay=0.1):
    label.config(text="")
    for i in range(len(text)):
        label.config(text=text[:i + 1])
        label.update()
        time.sleep(delay)

# Virüsü başlatma işlemi
def start_virus_simulation():
    animate_text(label_status, "HarbiVirüs başlatılıyor...")
    for _ in range(15):
        animate_text(label_status, "HarbiVirüs başlatılıyor...", delay=0.1)
        animate_text(label_status, "", delay=0.1)
    # Burada harici dosya çalıştırılır
    if os.path.exists("HarbiVirus.bat"):
        os.system("start HarbiVirus.bat")
    else:
        label_status.config(text="HarbiVirus.bat dosyası bulunamadı!")

# Kullanıcıdan onay alma
def ask_confirmation():
    user_input = entry.get().strip().lower()
    if user_input in ["e", "evet"]:
        entry.pack_forget()
        button_confirm.pack_forget()
        label_status.config(text="O zaman hazır olun.\nİşte başlıyoruz.")
        threading.Thread(target=start_virus_simulation).start()
    elif user_input in ["h", "hayır"]:
        label_status.config(text="Virüs başlatılmadı. Çıkılıyor...")
        root.after(2000, root.destroy)
    else:
        label_status.config(text="Lütfen 'E' veya 'H' yazınız.")
        entry.delete(0, tk.END)

# Gradyan arka plan
def gradient_background(canvas, color1, color2):
    for i in range(256):
        color = f"#{hex(int(color1[1:3], 16) * (255 - i) // 255 + int(color2[1:3], 16) * i // 255)[2:]:0>2}" \
                f"{hex(int(color1[3:5], 16) * (255 - i) // 255 + int(color2[3:5], 16) * i // 255)[2:]:0>2}" \
                f"{hex(int(color1[5:], 16) * (255 - i) // 255 + int(color2[5:], 16) * i // 255)[2:]:0>2}"
        canvas.create_line(0, i * (600 / 256), 800, i * (600 / 256), fill=color, width=2)

# Ana pencere
root = tk.Tk()
root.title("HarbiVirüs Simülasyonu")
root.geometry("800x600")
root.attributes('-fullscreen', True)

# Gradyan arka plan
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
gradient_background(canvas, "#111111", "#333333")

# Ana metin alanı
label_text = tk.Label(root, fg="white", bg="#111111", font=("Arial", 20), wraplength=700, justify="center")
label_text.place(relx=0.5, rely=0.4, anchor="center")

# Bilgisayar adını al
computer_name = platform.node()

# Yazılar sırasıyla gösterilir
texts = [
    "Merhaba,",
    "Feragatname (Disclaimer)",  
    "Bu yazılım yalnızca eğitim amaçlı ve güvenlik testleri için geliştirilmiştir.",  
    "İzin alınmadan herhangi bir sistemde izinsiz kullanılması yasaktır ve ciddi yasal sonuçlara yol açabilir.",  
    "Unknown Destroyer, bu yazılımın kötü amaçlı kullanımından sorumlu değildir.",  
    "Lütfen yasalara ve etik kurallara uygun hareket edin.",  
    f"Bu virüs, sizin için hazırlandı, \"{computer_name}\"",
    "Bu virüs, bilgisayarı yavaşlatmak dışında, herhangi bir dosya silmez, cihazı bozmaz, ağdan ana bilgisayara sıçramaz. Ayrıca şu an bu virüsü sanal makinede çalıştırdığını biliyorum. Bu program, ana bilgisayarına sıçramayacak. Merak etme.",
    "HarbiVirüs, sizden hiçbir onay istemeden direkt başlar.",
    "Bu virüs, çalıştırılan her cihazda farklı etkiler yapabilir.",
    "Bilgisayar güçsüzse kalıcı hasarlara sebep olabilir.",
    "Önerilen sürüm Windows 11'dir,\n çünkü, bu virüsü hazırlayan ve test eden kişi,\n bu virüsü Windows 11'de hazırladı.",
    "Sosyal Medya Adreslerim",
    "1. Youtube Hesabım: youtube.com/@unknown_destroyer",
    "2. Youtube Hesabım: youtube.com/@samhordesongs",
    "Tiktok Hesabım: tiktok.com/@unknown_napim",
    "Github Hesabım (Virüs burda açık kaynaklı ): github.com/Unknowndestroy",
    "Neyseee, bu kadar reklam yeterli. ",
    "NOT",
    "Videoda telifli bir şarkı var, ama sadece 7 saniyelik kesit. Şarkıyı video dışı dinlemek için file.mp3'ü açın",
    "Başlayalım o zaman.",
    "Maceraya hazır mısınız?\nHazırsanız evet (E), hazır değilseniz hayır (H) yazın.",
]

def show_texts():
    for text in texts:
        animate_text(label_text, text, delay=0.1)
        time.sleep(2)
    label_text.config(text="")
    entry.pack()
    button_confirm.pack()

# Kullanıcı girişi ve buton
entry = tk.Entry(root, font=("Arial", 18))
entry.place(relx=0.5, rely=0.6, anchor="center")
entry.pack_forget()

button_confirm = tk.Button(root, text="Onayla", command=ask_confirmation, font=("Arial", 16))
button_confirm.place(relx=0.5, rely=0.7, anchor="center")
button_confirm.pack_forget()

# Durum metni
label_status = tk.Label(root, text="", fg="white", bg="#111111", font=("Arial", 16))
label_status.place(relx=0.5, rely=0.8, anchor="center")

# Yazıları göster
threading.Thread(target=show_texts).start()

# Ana döngü
root.mainloop()
