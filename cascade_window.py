import tkinter as tk
from PIL import ImageTk

class CascadeWindow:
    def __init__(self, image, x, y):
        self.window = tk.Toplevel()
        self.window.geometry(f"+{x}+{y}")
        self.window.overrideredirect(True)  # Remove window decorations
        self.window.attributes('-topmost', True)
        
        # Convert PIL image to PhotoImage
        self.photo = ImageTk.PhotoImage(image)
        
        # Create label with the screenshot
        label = tk.Label(self.window, image=self.photo)
        label.pack()
        
        self.y = y
        
    def move_down(self, speed=5):
        """Move window down"""
        self.y += speed
        self.window.geometry(f"+{self.window.winfo_x()}+{self.y}")
        
    def is_offscreen(self, screen_height):
        return self.y > screen_height
        
    def destroy(self):
        self.window.destroy()