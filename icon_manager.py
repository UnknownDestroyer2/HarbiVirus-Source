import tkinter as tk
from random import randint

class ErrorIcon:
    def __init__(self, parent, x, y):
        self.label = tk.Label(
            parent,
            text="⚠️",
            font=("Arial", 20)
        )
        self.label.place(x=x, y=y)
        
    def destroy(self):
        self.label.destroy()