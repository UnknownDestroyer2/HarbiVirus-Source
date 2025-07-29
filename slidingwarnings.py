import tkinter as tk
from window_manager1 import ErrorWindow
from icon_manager1 import ErrorIcon
import random
import time

class ErrorCascade:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-alpha', 0)  # Hidden root window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.windows = []
        self.icons = []
        
    def spawn_icon(self):
        """Spawn a random error icon"""
        x = random.randint(0, self.screen_width - 50)
        y = random.randint(0, self.screen_height - 50)
        icon = ErrorIcon(self.root, x, y)
        self.icons.append(icon)
        
    def update(self):
        """Update window positions and spawn icons"""
        # Move windows down
        for window in self.windows[:]:
            window.move_down()
            if window.is_offscreen(self.screen_height):
                window.window.destroy()
                self.windows.remove(window)
        
        # Randomly spawn new windows
        if len(self.windows) < 50 and random.random() < 0.1:
            x = random.randint(0, self.screen_width - 300)
            window = ErrorWindow(x, -150)
            self.windows.append(window)
        
        # Randomly spawn icons
        if random.random() < 0.05:
            self.spawn_icon()
            
        # Continue animation
        if self.windows or len(self.icons) < 100:
            self.root.after(50, self.update)
        
    def start(self):
        self.update()
        self.root.mainloop()

if __name__ == "__main__":
    cascade = ErrorCascade()
    cascade.start()
