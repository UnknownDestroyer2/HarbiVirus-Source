import tkinter as tk
import random
import subprocess
import sys
import os

root = tk.Tk()
root.overrideredirect(True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

win_width = 600
win_height = 300

start_x = (screen_width - win_width) // 2
start_y = (screen_height - win_height) // 2

root.geometry(f"{win_width}x{win_height}+{start_x}+{start_y}")
root.configure(bg="black")

# Ana pencere widgetları
label = tk.Label(root, text="This is a malware, Run?", fg="red", bg="black", font=("Arial", 28, "bold"))
label.pack(pady=50)

frame = tk.Frame(root, bg="black")
frame.pack()

def shake_forever(window, x, y, intensity=20, delay=10):
    dx = random.randint(-intensity, intensity)
    dy = random.randint(-intensity, intensity)
    window.geometry(f"+{x + dx}+{y + dy}")
    window.after(delay, shake_forever, window, x, y, intensity, delay)

def open_warning():
    label.pack_forget()
    frame.pack_forget()

    warning_label = tk.Label(root, text="Last warning,\ndo you want to start this malware?", fg="yellow", bg="black", font=("Arial", 24, "bold"))
    warning_label.pack(pady=40)

    warning_frame = tk.Frame(root, bg="black")
    warning_frame.pack()

    def on_fix():
        root.destroy()
        print("GG, kapattın lan!")

    def on_start():
        start_py_path = os.path.join(os.getcwd(), "START.py")
        if os.path.exists(start_py_path):
            subprocess.Popen([sys.executable, start_py_path])
        else:
            print("START.py bulunamadı lan!")
        root.destroy()
        print("Malware başlatıldı, gg!")

    btn_fix = tk.Button(warning_frame, text="No", fg="white", bg="gray", width=12, height=2, command=on_fix, font=("Arial", 16, "bold"))
    btn_fix.pack(side="left", padx=30)

    btn_start = tk.Button(warning_frame, text="Yes", fg="white", bg="red", width=12, height=2, command=on_start, font=("Arial", 16, "bold"))
    btn_start.pack(side="right", padx=30)

btn_yes = tk.Button(frame, text="YES", fg="white", bg="red", width=12, height=2, command=open_warning, font=("Arial", 16, "bold"))
btn_yes.pack(side="left", padx=30)

def on_no():
    root.destroy()
    print("GG, kapattın lan!")

btn_no = tk.Button(frame, text="NO", fg="white", bg="gray", width=12, height=2, command=on_no, font=("Arial", 16, "bold"))
btn_no.pack(side="right", padx=30)

shake_forever(root, start_x, start_y)

root.mainloop()
