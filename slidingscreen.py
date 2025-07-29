import tkinter as tk
from screen_capture import capture_screen
from cascade_window import CascadeWindow
import random
import time

class ScreenCascade:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide root window
        
        # Get screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Capture initial screen
        self.screenshot = capture_screen()
        
        # Store cascade windows
        self.windows = []
        
    def create_cascade(self):
        """Create a new cascade window"""
        x = random.randint(-50, 50)  # Small random x offset
        y = -self.screen_height  # Start from top of screen
        
        window = CascadeWindow(self.screenshot, x, y)
        self.windows.append(window)
        
    def update(self):
        """Update window positions"""
        # Move all windows down
        for window in self.windows[:]:
            window.move_down(speed=10)
            if window.is_offscreen(self.screen_height):
                window.destroy()
                self.windows.remove(window)
        
        # Create new cascade randomly
        if len(self.windows) < 20 and random.random() < 0.1:
            self.create_cascade()
            
        # Continue animation
        if len(self.windows) > 0 or len(self.windows) < 50:
            self.root.after(50, self.update)
        
    def start(self):
        time.sleep(1)  # Small delay to prepare
        self.update()
        self.root.mainloop()

if __name__ == "__main__":
    cascade = ScreenCascade()
    cascade.start()