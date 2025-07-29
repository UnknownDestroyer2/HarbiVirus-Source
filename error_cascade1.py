import tkinter as tk
from random import randint
import time

class ErrorWindow:
    def __init__(self, x, y):
        self.window = tk.Tk()
        self.window.geometry(f"300x150+{x}+{y}")
        self.window.title("Error")
        
        # Make window appear on top
        self.window.attributes('-topmost', True)
        
        # Add error message
        label = tk.Label(
            self.window, 
            text="⚠️ System Error", 
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

def create_cascade():
    screen_width = 1200
    screen_height = 800
    windows = []
    
    try:
        for i in range(50):  # Create 50 windows
            # Calculate position with slight offset each time
            x = (i * 30) % (screen_width - 300)
            y = (i * 30) % (screen_height - 150)
            
            # Create new error window
            window = ErrorWindow(x, y)
            windows.append(window)
            
            # Update the screen
            window.window.update()
            time.sleep(0.1)  # Small delay between windows
            
        # Start the main loop
        windows[0].window.mainloop()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_cascade()