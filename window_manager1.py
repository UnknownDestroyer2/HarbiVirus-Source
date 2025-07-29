import tkinter as tk
from random import randint
import time

class ErrorWindow:
    def __init__(self, x, y):
        self.window = tk.Tk()
        self.window.geometry(f"300x150+{x}+{y}")
        self.window.title("Error")
        self.window.attributes('-topmost', True)
        
        # Add error message
        label = tk.Label(
            self.window, 
            text="⚠️ You got hacked lil bro", 
            font=("Arial", 14, "bold"),
            pady=20
        )
        label.pack()
        
        # Add OK button
        button = tk.Button(
            self.window,
            text="OK",
            command=self.window.destroy,
            width=10
        )
        button.pack()
        
        self.y = y  # Store current y position for animation
        
    def move_down(self, speed=5):
        """Move window down by speed pixels"""
        self.y += speed
        self.window.geometry(f"300x150+{self.window.winfo_x()}+{self.y}")
        
    def is_offscreen(self, screen_height):
        """Check if window is off screen"""
        return self.y > screen_height
